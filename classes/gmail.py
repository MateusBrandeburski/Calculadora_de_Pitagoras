import smtplib
from email.message import EmailMessage


class Email():
    
    def __init__(self, EMAIL_ADDRESS, EMAIL_PASSWORD):
        self.__EMAIL_ADDRESS = EMAIL_ADDRESS
        self.__EMAIL_PASSWORD = EMAIL_PASSWORD
    
    def envia_email(self):
        # configurar email, senha
        EMAIL_ADDRESS = self.__EMAIL_ADDRESS
        EMAIL_PASSWORD = self.__EMAIL_PASSWORD

        msg = EmailMessage()
        msg['Subject'] = 'Calculadora de Pitágoras'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'mateus.brandeburski92@gmail.com'
        msg.set_content('Acabam de clicar em informações na calculadora de Pitágoras')


        # envia o email
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


# quando estiver em POO, deve ser executado assim:

# enviar = Email("mateus@trovale.com.br", "karateka30")
# enviar.envia_email()
