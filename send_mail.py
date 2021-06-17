from smtplib import SMTP, SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import config as cfg


def set_conection():
    # Conexión al servidor SMTP
    servidor_smtp = SMTP(host=cfg.mail_host, port=cfg.mail_port)
    servidor_smtp.ehlo()
    servidor_smtp.starttls()
    servidor_smtp.ehlo()
    servidor_smtp.login(cfg.mail_account, cfg.mail_pwd)

    return servidor_smtp


def send_mail(to_addr):
    # configuración del correo
    mime_msg = MIMEMultipart()
    mime_msg['From'] = cfg.mail_from
    mime_msg['To'] = to_addr
    mime_msg['Subject'] = cfg.mail_subject

    # añadimos el cuerpo del mensaje
    part = MIMEText(cfg.mail_body, "plain")
    mime_msg.attach(part)

    # añadimos adjuntos
    for mail_file in cfg.mail_attach_files:
        part = MIMEApplication(open(mail_file[0], "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=mail_file[1])
        mime_msg.attach(part)

    # envío del correo
    smtp.sendmail(cfg.mail_account, to_addr.split(), mime_msg.as_string())


if __name__ == "__main__":
    mail_counter = 0

    try:
        smtp = set_conection()

        for mail_to_file in cfg.mail_to_files:
            with open(mail_to_file) as f:
                receptores = f.read().split("\n")

            for receptor in receptores:
                print(receptor)
                send_mail(receptor)
                mail_counter += 1

        smtp.quit()

    except FileNotFoundError as err:
        print(f"ERROR: No se ha encontrado el archivo de direcciones de correo: {err}")
    except TimeoutError as err:
        print(f"ERROR: Se ha producido un error al conectar con el servidor SMTP: {err}")
    except SMTPAuthenticationError as err:
        print(f"ERROR: El usuario y/o la password no son correctas: {err}")
    finally:
        print(f"Envío de correos terminado. \nMensajes enviados = {mail_counter}")
