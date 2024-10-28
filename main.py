from app import app

if __name__ == "__main__":
    # In production, use Gunicorn
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
