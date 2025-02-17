from flask import Flask, jsonify, render_template
from resend import Resend
import os
from datetime import datetime


app = Flask(__name__)
resend = Resend(os.getenv("RESEND_API_KEY"))

# SAMPLE DATA
DAILY_CONTENT = {
    "quote": "The only way to do great work is to love what you do. - Steve Jobs",
    "advice": "Take 5 minutes today to practice deep breathing. It reduces stress and improves focus.",
    "habit": "20-minute afternoon walk: Boosts creativity and improves cardiovascular health.",
    "recipe_name": "Quinoa Salad",
    "recipe_content": "Mix cooked quinoa, cherry tomatoes, cucumber, feta cheese, and olive oil. Add lemon dressing.",
    "unsubscribe_url": "https://yourdomain.com/subscribe"
}

@app.route('/api/send-daily-emails', metthod = ['POST'])
def send_daily_emails():
    # in production, get suscribers from database
    subscribers = ["jlcaclosada@gmail.com", "wysso10@gmail.com"]
    html_content = render_template('email_tempalte.html', **DAILY_CONTENT)

    for email in subscribers:
        resend.emails.send({
            "from": "Newsletter <newsletter@yourdomain.com>",
            "to": email,
            "subject": f"Your Daily Wellness Digest - {datetime.now().strftime('%B %d, %Y')}",
            "html": html_content
        })


    return jsonify({"status": "success", "message": f"Emails sent to {len(subscribers)} subscibers"})

if __name__ == '__main__':
    app.run()