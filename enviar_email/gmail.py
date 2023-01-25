import os
import smtplib
from email.message import EmailMessage

def envia_email():
    #configurar email, senha
    EMAIL_ADDRESS = 'os.environ["EMAIL"]'
    EMAIL_PASSWORD = 'os.environ["DISCORD_TOKEN"]'

    msg = EmailMessage()
    msg['Subject'] = 'Calculadora de Pitágoras'
    msg['From'] = 'os.environ["EMAIL"]'
    msg['To'] = 'os.environ["EMAIL"]'
    msg.set_content('Acabam de clicar em informações na calculadora de Pitágoras')


    # Enviar email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)