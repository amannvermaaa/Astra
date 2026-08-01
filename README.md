# Astra 🚀 - Interplanetary Travel Booking Concept

Hey everyone! 👋 Welcome to **Astra**, a personal project I built to practice my full-stack development skills. It's a conceptual landing page for a space tourism company (kind of like SpaceX, but for booking actual commercial flights to Mars and beyond!). 

I wanted to focus heavily on the **UI/UX**, making sure it feels super premium and futuristic, while also having a fully functioning backend to process "waitlist" registrations.

## ✨ Features
- **Premium UI:** Custom dark-mode design with sleek typography and smooth fade-in animations on scroll.
- **Mouse Parallax Effect:** The background images subtly move based on where your cursor is, giving it a cool 3D feel.
- **Working Waitlist System:** Users can actually fill out the registration form at the bottom.
- **Python Flask Backend:** A lightweight server that handles form submissions.
- **SQLite Database:** Registrations are saved locally into a real relational database, no messy JSON files!
- **Email Notifications:** (Optional) If configured, the app sends an automatic email notification whenever someone joins the waitlist via `smtplib`.

## 🛠️ Tech Stack
- **Frontend:** Vanilla HTML, CSS, and JavaScript. (No frameworks used here—just pure DOM manipulation and CSS magic to keep things fast).
- **Backend:** Python & Flask.
- **Database:** SQLite.

## 🚀 How to run it locally

If you want to spin this up on your own machine, it's pretty simple:

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/astra.git
   cd astra
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure Email Notifications (Optional):**
   - Copy `backend/.env.example` to `backend/.env`.
   - Add your email and an App Password (if using Gmail) to receive notifications when someone registers. If you skip this, it just logs a warning but the database still works perfectly.

5. **Run the server:**
   ```bash
   python backend/app.py
   ```
   *The server will automatically map the frontend folder and serve the website.*

6. **View the site:**
   Open your browser and go to `http://localhost:5000`

## 💡 What I learned
Building this was super fun! Getting the mouse parallax effect to feel *just right* without being too dizzying took some tweaking. I also got to dive into setting up SQLite with Flask and handling environment variables securely.

Feel free to fork this, use the design for your own projects, or submit a PR if you have any cool ideas! 

---
*Disclaimer: This is just a conceptual project. Unfortunately, I cannot actually fly you to Mars... yet.* 😉
