import secret
import smtplib


my_email = "yesmanvong@gmail.com"
password = secret.password

def email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="gudiedryan@gmail.com", 
            msg=f"Subject:ISS Sighting\n\nLook up! The ISS is overhead and it's dark out!"
        )