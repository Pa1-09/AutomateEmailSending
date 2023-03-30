import speech_recognition as sr # for taking inputs from us
import pyttsx3  # talking to us
import smtplib  # for sending mails
import time

# for structuring emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

listener = sr.Recognizer()
engine = pyttsx3.init()

# taking input from user
def get_info_from_user():
    try:
        with sr.Microphone() as source:
            print("listening... please speak..!")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info.lower())
            return info.lower()

    except Exception:
        pass


# talking to user
def talk_to_user(text):
    engine.say(text)
    time.sleep(10)
    engine.runAndWait()


def get_email_info():
    talk_to_user("Please mention recipient name")
    receiver = get_info_from_user()


    mails = {"pawan": "ndlvrpavankumar09@gmail.com",
     "bhaskar": "ndlvrbhaskar664@gmail.com",
     "haritha": "hk.andalavari@gmail.com"}

    if receiver in mails.keys():
        receiver_mail = mails[receiver]
        print(mails[receiver])

    # talk_to_user(f"So , confirm if you want to send email for {mails[receiver]}")
    # confirmation = get_info_from_user()
    #
    # if confirmation=="yes":
    #     receiver = mails[receiver]

    talk_to_user("Please mention your subject")
    subject = get_info_from_user()

    talk_to_user("Please mention body of the email")
    body = get_info_from_user()

    send_mail(to_whom=receiver_mail, subject=subject, body_text=body)
    talk_to_user("Email Sent")
    talk_to_user("Do you want to send another email")
    value = get_info_from_user()
    if value == "yes":
        get_email_info()
    elif value =="no":
        talk_to_user("Bye")



def send_mail(to_whom, subject, body_text):
    # email layout
    msg = MIMEMultipart()

    # header information
    msg['From'] = "ndlvrpavankumar09@gmail.com"
    msg['To'] = to_whom
    msg['Subject'] = subject

    # body information
    msg.attach(MIMEText(body_text))
    msg = msg.as_string()

    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.ehlo()
            server.starttls()
            server.login("ndlvrpavankumar09@gmail.com", "scyxbnkjnbcskaro")
            server.sendmail("ndlvrpavankumar09@gmail.com", to_whom, msg)
            server.quit()
    except TimeoutError:
        print("Connection Timed out")



get_email_info()

