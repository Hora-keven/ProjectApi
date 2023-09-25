import os
import smtplib
from email.message import EmailMessage


caminho_email = "lexluthor810@gmail.com"
senha = 'godblessyou_forever'

mensagem = EmailMessage()
mensagem['Subject'] = "Mensagem teste"
mensagem['From'] = 'lexluthor810@gmail.com'
mensagem['To'] = 'kevensantos993@gmail.com'
mensagem.set_content("Mensagem teste para testar")

with smtplib.SMTP_SSL("stmp.gmail.com", 587) as stmp:
    stmp.login(caminho_email, senha)
    stmp.send_message(mensagem)