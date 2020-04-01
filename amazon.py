import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

print("===========================================================================================")
print("                A M A Z O N      P R O D U C T    P R I C E     T R A C K E R                          ")
print("===========================================================================================")
print("")
url = input("Enter the amazon product URL : ")
URL = 'https://www.amazon.in/boAt-BassHeads-225-Special-Headphones/dp/B01MF8MB65/ref=gbph_img_m-2_7a61_c3b55cc7?smid=A14CZOWI0VEHLG&pf_rd_p=4209a139-79dc-49eb-9e25-6cab2dc57a61&pf_rd_s=merchandised-search-2&pf_rd_t=101&pf_rd_i=1388921031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=TG42FRP27KJCAV3V5418'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

print("================================")
print("     Y O U R   P R O D U C T   ")
print("=================================")
c = 0
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
print(title.strip())
if (soup.find(id="priceblock_dealprice")):
    d_price = soup.find(id="priceblock_dealprice").get_text()
    print("Deal Price : " + d_price)
if (soup.find(id="priceblock_ourprice")):
    o_price = soup.find(id="priceblock_ourprice").get_text()
    print("Original Price : " + o_price)


# o_price = soup.find(id="priceblock_ourprice").get_text()

# converted_price = float(price[2:5])
g=input("Enter the email address from which the mail has to be sent: ")
h=input("Enter the password: ")
j=input("Enter the email address to receive the notification: ")


def check_price(c):
    page = requests.get(url, headers=headers)
    o, d = 0, 0
    deal_price, our_price = 0, 0
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    if (soup.find(id="priceblock_dealprice")):
        deal_price = soup.find(id="priceblock_dealprice").get_text()
        # print(d_price)
        if (deal_price == d_price):
            d = 1

        else:
            print("Deal-" + deal_price)
    if (soup.find(id="priceblock_ourprice")):
        our_price = soup.find(id="priceblock_ourprice").get_text()
        # print(d_price)
        if (our_price == o_price):
            o = 1

        else:
            print("Original" + our_price)

    if (o == 1 or d == 1):
        print("Price Changed!")
        send_mail()

        if (c == 0):
            ch = int(input("\nPress 1 to check if the price is within your budget : "))
            if (ch == 1):
                if (o == 1 and d == 0):
                    desired(our_price)

                elif (d == 1 and o == 0):
                    desired(deal_price)
                elif (d == 1 and o == 1):
                    desired(deal_price)
                c = 1

                # print(o_price)
    # print(title.strip())
    # if(our_price != o_price):
    #   print("Price Changed!")
    #  send_mail()


def send_mail():
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(g, h)

    subject = 'price changed!'
    body = 'Check the amazon link' + url
    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(g, j, msg)
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()


def send_mail_desired():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    g=input("Enter the email address: ")
    h=input("Enter the password ")
    server.login(g, h)

    subject = 'You can buy ' + title
    body = 'Check the amazon link ' + url
    msg = f"subject: {subject}\n\n{body}"
    j=input("Enter the email address you want notification update: ")
    server.sendmail(g, j, msg)
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()


def desired(price):
    des_price = float(input("Enter your budget : "))
    cov_price = re.sub(",", "", price)
    c_price = float(cov_price[2:])
    # print(type(c_price))
    # print(type(des_price))
    if (des_price < c_price):
        send_mail_desired()


while (True):
    check_price(c)
    c = 1
    time.sleep(30)