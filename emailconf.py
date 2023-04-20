import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(text):
    # Configurar los detalles del correo electrónico
    sender_email = "#"
    sender_password = "#"
    receiver_email = "#"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "TEST MACC SERVER EMAIL"

    # Agregar el cuerpo del mensaje
    message.attach(MIMEText(text, "plain"))

    # Iniciar la conexión al servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
