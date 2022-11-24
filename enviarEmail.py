import smtplib
import email.message

def enviarEmail(error, dbname):  
    PASSWORD = 'ignwgninwzafrlbo' 
    EMAIL = 'pedronovetech@gmail.com'
    
    corpo_email = f"""
    <h1>Erro na carga das vacinas</h1>
    <h3>Erro no banco {dbname}</h3>
    <p>{error}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "ERRO nas cargas das vacinas!"
    msg['From'] = EMAIL
    msg['To'] = 'piterhenou@gmail.com'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(EMAIL, PASSWORD)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado.')