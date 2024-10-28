import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import logging
from logging.handlers import RotatingFileHandler
import sys

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.secret_key = os.urandom(24)

# Production configurations
if not app.debug:
    # Configure logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/terminal_tasks.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Terminal Tasks startup')

db.init_app(app)

with app.app_context():
    import models
    db.create_all()

@app.route('/')
def index():
    tasks = models.Task.query.order_by(models.Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    content = request.form.get('content')
    if content:
        task = models.Task(content=content)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201
    return jsonify({'error': 'Content is required'}), 400

@app.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    task = models.Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return jsonify(task.to_dict())

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', error='Internal server error'), 500
