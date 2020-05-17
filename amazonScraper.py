import smtplib
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    'Content-Type': 'text/html; charset="iso-8859-1"'
}
# Url from item you want to track
URL = ""
# Email to sen and receive information
my_email = ""
# Password for email
password = ""
# Your max offer for the item (Change this value)
my_price = 0


def send_mail(title, price):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(my_email, password)

    subject = "Price fell down!"
    body = f"""
        {title}
        At only: {price}
        Check the amazon link: {URL}"""
    msg = f"Subject: {subject}\n\n{body}"

    # You need to encode all msg, ignore helps whit strange characters
    try:
        server.sendmail(my_email, my_email, msg.encode("iso-8859-1", 'ignore'))
    except smtplib.SMTPException as err:
        print("Error sending email: ", err)

    server.quit()
    print("Email has been sent")


def check_price():
    page = requests.get(URL, headers=headers)
    if page.status_code > 500:
        print("Page was blocked")
        raise SystemExit(0)

    # Only works whit html5lib on amazon
    soup = BeautifulSoup(page.content, "html5lib")
    title = soup.find(id="productTitle")
    if not title:
        print("Change user agent")
        raise SystemExit(0)

    title = title.get_text().strip()
    print(title)
    price = soup.find(id="priceblock_ourprice")
    price = price.get_text()
    # You need to replace "," for "." so you can convert to float
    try:
        converted_price = float(price.split()[0].replace(",", "."))
    except TypeError as err:
        print("You didn't get a number: ", err)
    print(price)
    if converted_price <= my_price:
        send_mail(title, price)


while True:
    check_price()
    # Once at day in seconds
    time.sleep(60*60*24)
