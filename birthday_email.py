import smtplib
import pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

db = pymysql.connect(host="localhost", user="root", password="root", db="birthday_db")

def send_birthday_email(name, email):
    sender_email = "samy.test.404@gmail.com"  
    receiver_email = email  
    password = "rsii thyw iqxf uwqb"  

    subject = "Happy Birthday!"
    body = f"Dear {name},\n\nWishing you a very Happy Birthday! "

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email sent to {name} ({email})")
    except Exception as e:
        print(f" Error sending email to {name}: {e}")

def check_and_send_birthday_emails():
    today = datetime.today().strftime('%m-%d')  
    
    print(f"Today's date (MM-DD): {today}")

    cursor = db.cursor()
    query = "SELECT name, email, birthday FROM users"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        if not results:
            print("No users found in the database.")
        else:
            for name, email, birthday in results:
                print(f" User: {name}, Email: {email}, Birthday: {birthday} (Type: {type(birthday)})")

                if birthday.strftime('%m-%d') == today:
                    print(f"Found birthday match: {name} ({email})")
                    send_birthday_email(name, email)
                else:
                    print(f"No birthday today for: {name} ({email})")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    check_and_send_birthday_emails()
    db.close()
