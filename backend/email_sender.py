import smtplib
from email.mime.text import MIMEText
from config import Config
import openai

openai.api_key = Config.OPENAI_API_KEY

def generate_phishing_email(target_email):
    """Use GPT-4 to generate a realistic phishing email."""
    prompt = f"Generate a phishing email that looks like a legitimate company email, targeting {target_email}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def send_email(target_email):
    """Send phishing email using SMTP."""
    email_body = generate_phishing_email(target_email)
    msg = MIMEText(email_body, "html")
    msg["Subject"] = "Important Security Update"
    msg["From"] = Config.SMTP_EMAIL
    msg["To"] = target_email

    try:
        server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
        server.starttls()
        server.login(Config.SMTP_EMAIL, Config.SMTP_PASSWORD)
        server.sendmail(Config.SMTP_EMAIL, target_email, msg.as_string())
        server.quit()
        return {"status": "success", "message": "Email sent!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
