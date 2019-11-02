import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?keywords=sony+a7&qid=1566928063&s=gateway&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2]+price[4:6]+price[7:10])
    if(converted_price<160000):
        send_mail()
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aishubhrani@gmail.com', 'biesudecxlufzngr')
    subject = 'The price fell down'
    body = 'Check the amazon link https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?keywords=sony+a7&qid=1566928063&s=gateway&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'aishubhrani@gmail.com',
        'bhumikam24@gmail.com',
        msg
    )
    print("Email has been sent")
    server.quit()
while(True):
    check_price()
    time.sleep(60*60)