import os
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
frontend_folder = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app = Flask(__name__, static_folder=frontend_folder, static_url_path='')
CORS(app)

DB_FILE = 'database.db'

# Email Configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SMTP_EMAIL = os.getenv('SMTP_EMAIL')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

# Database Initialization
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            destination TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Save to SQLite Database
def save_registration(name, email, destination):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO registrations (name, email, destination)
        VALUES (?, ?, ?)
    ''', (name, email, destination))
    conn.commit()
    conn.close()

# Send Email Notification
def send_email_notification(name, email, destination):
    if not SMTP_EMAIL or not SMTP_PASSWORD or SMTP_EMAIL == 'your_email@gmail.com':
        print("Warning: Email credentials not configured in .env. Skipping email notification.")
        return False

    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_EMAIL
        msg['To'] = SMTP_EMAIL
        msg['Subject'] = f"🚀 New Astra Registration: {name}"

        body = f"""
        A new user has joined the Astra waitlist!

        Name: {name}
        Email: {email}
        Destination: {destination}
        Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SMTP_EMAIL, SMTP_EMAIL, text)
        server.quit()
        
        print(f"Email notification sent for {name}.")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# Routes
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        name = data.get('name')
        email = data.get('email')
        destination = data.get('destination')
        
        if not name or not email or not destination:
            return jsonify({'message': 'All fields are required.'}), 400
            
        # 1. Save to SQLite Database
        save_registration(name, email, destination)
        
        # 2. Send Email Notification
        send_email_notification(name, email, destination)
        
        return jsonify({
            'message': f'Welcome aboard, {name}! Your seat for the {destination} mission is confirmed.'
        }), 201
        
    except Exception as e:
        print(f"Error saving registration: {e}")
        return jsonify({'message': 'Server error.'}), 500

if __name__ == '__main__':
    print("Initializing Database...")
    init_db()
    print("Starting Astra Server...")
    print(f"Frontend folder mapped to: {app.static_folder}")
    if SMTP_EMAIL == 'your_email@gmail.com' or not SMTP_EMAIL:
        print("\n[WARNING] Please update backend/.env with your real email credentials to enable email notifications.\n")
    print("Visit http://localhost:5000 to view the website.")
    app.run(host='0.0.0.0', port=5000, debug=True)
