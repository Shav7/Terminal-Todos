from app import db
from datetime import datetime

class TaskHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_content = db.Column(db.String(200), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # 'created', 'completed', 'reset'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'task_content': self.task_content,
            'action': self.action,
            'timestamp': self.timestamp.isoformat()
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }
