from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- import this
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # <-- add this line

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json

    subject = f"New Contact Form Submission from {data['name']}"
    body = f"""
    Name: {data['name']}
    Email: {data['email']}
    Company: {data.get('company', 'N/A')}
    Interest: {data['interest']}
    Message: {data['message']}
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "galheprathmesh1@gmail.com"
    msg['To'] = "prathmeshgalhe9@gmail.com"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("galheprathmesh1@gmail.com", "xbvm mgyc hovf kmlj")  # your app password
        server.sendmail("galheprathmesh1@gmail.com", "prathmeshgalhe9@gmail.com", msg.as_string())
        server.quit()
        return jsonify({"success": True, "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
