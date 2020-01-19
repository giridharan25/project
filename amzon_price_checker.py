'''
  REPLACE MY AGENT ID'
          SENDER MAIL ID
          2 STEP VERIFICATION PASSWORD
           
  BEFORE EXECUTING THIS CODE
'''  
  






import requests
from bs4 import BeautifulSoup
import smtplib

URL =str(input("Enter the link : "))

headers={'User-Agent':'YOUR MY AGENT ID'}

def check_price():
    expected_price=int(input("Enter the expected price : "))
    page=requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content,'html.parser')
    
    title=soup.find(id='productTitle').get_text()
    
    price=soup.find(id='priceblock_dealprice').get_text() #some products will have a tag priceblock_ourprice
    
    converted_price=price[2:]
    
    if("," in converted_price):
        converted_price=converted_price.replace(",","")
        
    l=len(converted_price)
    converted_price=converted_price[:l-3]
    
    converted_price=int(converted_price)

    if(converted_price < expected_price):
        send_mail()
    else:
        print("SORRY, THE PRICE IS HIGHER THAN WHAT YOU EXPECT")
    print(title.strip())
    print(converted_price)

def send_mail():
    receiver_mail_id=str(input("Enter your Mail id : "))
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('SENDER MAIL ID','2 STEP VERIFICATION PASSWORD')
    subject='price fell down!'
    body='check the amazon link',URL
    msg=f"subject:{subject}\n\n{body}"
    server.sendmail(
        "SENDER MAIL ID",
        receiver_mail_id,
        msg
        )
    print('\n\nHEY EMAIL HAS BEEN SENT')
    server.quit()
    
    

check_price()
