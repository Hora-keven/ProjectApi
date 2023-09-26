
import os 
import smtplib
import email.message
from senha import senha


EMAIL_ADDRESS = 'lexluthor810@gmail.com'
EMAIL_PASSWORD = senha
corpo_email = '''
    <p>Olá</>
    <p>Segue o email!</>

'''
mensagem  = email.message.Message()
mensagem['Subject'] = 'Testando'
mensagem['From'] = 'lexluthor810@gmail.com'
mensagem['To'] = 'kevensantos993@gmail.com'
mensagem.add_header("Context-Type", 'text.html')

mensagem.set_payload(corpo_email)

s = smtplib.SMTP_SSL('smtp.gmail.com', 25) 
s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
s.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string().encode("utf-8"))
s.quit()
print('email enviado')