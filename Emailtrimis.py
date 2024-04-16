#DIRECTOR EMAIL
import os
import ssl
import smtplib
from email.message import EmailMessage
def mail(tip_alerta,stare_alerta):
	# Setup
  smtp_port = 587
  smtp_server = "smtp.gmail.com"
  email_from = "statiemeteolicenta10@gmail.com"
  email_to = "mikemike2669@gmail.com"
  pswd = "iiblemnsegpxptah"
  subject = f"Atentie, {tip_alerta}"  
  message_body = f"Atentie! A fost {tip_alerta} - {stare_alerta}."

  
  # creare de mail
  # create the email
  message = EmailMessage()
  message.set_content(message_body)
  message["Subject"] = subject
  message["From"] = email_from
  message["To"] = email_to

  #stabilim conextiunea SISTEM-SMTP-USER
  #establish the connection sys-smtp-user
  simple_email_context = ssl.create_default_context()

  try:
      print("Conectare...")
      TIE_server = smtplib.SMTP(smtp_server, smtp_port)
      TIE_server.starttls(context=simple_email_context)
      TIE_server.login(email_from, pswd)
      print("Conectat!")

      print()
      print(f"Trimitem mail catre {email_to}")
      TIE_server.send_message(message)
      print(f"S-a trimis mail catre {email_to}")

  except Exception as e:
      print(e)
  finally:
      TIE_server.quit()

