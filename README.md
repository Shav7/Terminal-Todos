# Terminal Todos

A retro terminal-styled to-do list application built with Flask and Vanilla JS, featuring task management, progress tracking, and a built-in timer.

## Features

- Terminal-styled interface
- Task management (add, complete, reset)
- Visual progress tracking
- Built-in timer with reset functionality
- Task history tracking
- Responsive design

## Local Development Setup

1. **Prerequisites**
   - Python 3.11 or higher
   - PostgreSQL database

2. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd terminal-todos
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the project root with the following variables:
   ```
   DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
   PGHOST=<database-host>
   PGPORT=<database-port>
   PGUSER=<database-user>
   PGPASSWORD=<database-password>
   PGDATABASE=<database-name>
   ```

5. **Initialize Database**
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   ```

6. **Run the Development Server**
   ```bash
   python main.py
   ```
   The application will be available at `http://localhost:5000`

## Replit Deployment

1. **Fork the Project**
   - Visit the project on Replit
   - Click "Fork" to create your own copy

2. **Configure Environment Variables**
   - Go to "Secrets" in your Replit project
   - Add all required environment variables (DATABASE_URL, etc.)

3. **Deploy**
   - Replit will automatically install dependencies from `requirements.txt`
   - Click "Run" to start the application
   - The application will be available at your Replit URL

## Project Structure

```
terminal-todos/
├── app.py           # Main Flask application
├── models.py        # Database models
├── static/
│   ├── css/        # Stylesheets
│   ├── js/         # JavaScript files
│   └── favicon.*   # Application icons
├── templates/       # HTML templates
├── requirements.txt # Project dependencies
└── main.py         # Application entry point
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.
