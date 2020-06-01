
############################################################
#   Version     Description
#   1.0         First working version, completing the basic functionality.
#   1.1         Replaced FOR loop with basic assignment to avoid over computation.
#   1.2         Generating stock name dynamically instead of hardcoding it.
#   1.3         Encrypting mail-id and password by fetching them from machine's environment variables.
#
#
#
#
############################################################








#importing useful libraries
import requests
import bs4
import lxml
import smtplib
from email.message import EmailMessage
import os



#defining SMTP variables and assigning them
smtp_server = ''
smtp_port = 587

#defining login credentials
mail_user = os.environ.get('gmail_username')
mail_pass = os.environ.get('gmail_pass')



#defining variables for stock websites and assigning them values
stock1 = 'https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/indusindbank/IIB'

stock2 = 'https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/tatapowercompany/TPC'

stock3 = 'https://www.moneycontrol.com/india/stockpricequote/finance-investments/cpseetf/CPS01'

stock4 = 'https://www.moneycontrol.com/india/stockpricequote/diversified/generalinsurancecorporationindia/GIC12'

stock5 = 'https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01'

stock6 = 'https://www.moneycontrol.com/india/stockpricequote/miscellaneous/hdfclifeinsurancecompanylimited/HSL01'

stock7 = 'https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/larsentoubro/LT'

stock8 = 'https://www.moneycontrol.com/india/stockpricequote/computers-software-training/zeelearn/ZL01'



#creating a new request to get above mentioned HTML page
myreq_stock1 = requests.get(stock1)
myreq_stock2 = requests.get(stock2)
myreq_stock3 = requests.get(stock3)
myreq_stock4 = requests.get(stock4)
myreq_stock5 = requests.get(stock5)
myreq_stock6 = requests.get(stock6)
myreq_stock7 = requests.get(stock7)
myreq_stock8 = requests.get(stock8)



#creating a BeautifulSoup object to store data we got in the previous step
mysoup_stock1 = bs4.BeautifulSoup(myreq_stock1.text, 'lxml')
mysoup_stock2 = bs4.BeautifulSoup(myreq_stock2.text, 'lxml')
mysoup_stock3 = bs4.BeautifulSoup(myreq_stock3.text, 'lxml')
mysoup_stock4 = bs4.BeautifulSoup(myreq_stock4.text, 'lxml')
mysoup_stock5 = bs4.BeautifulSoup(myreq_stock5.text, 'lxml')
mysoup_stock6 = bs4.BeautifulSoup(myreq_stock6.text, 'lxml')
mysoup_stock7 = bs4.BeautifulSoup(myreq_stock7.text, 'lxml')
mysoup_stock8 = bs4.BeautifulSoup(myreq_stock8.text, 'lxml')




#initializing and assigning extract from BeautifulSoup
i = mysoup_stock1.select('.txt15B')
price_stock1 = i[0].text

i = mysoup_stock2.select('.txt15B')
price_stock2 = i[0].text

i = mysoup_stock3.select('.txt15B')
price_stock3 = i[0].text

i = mysoup_stock4.select('.txt15B')
price_stock4 = i[0].text

i = mysoup_stock5.select('.txt15B')
price_stock5 = i[0].text

i = mysoup_stock6.select('.txt15B')
price_stock6 = i[0].text

i = mysoup_stock7.select('.txt15B')
price_stock7 = i[0].text

i = mysoup_stock8.select('.txt15B')
price_stock8 = i[0].text


#Generating stock names dynamically
stockname_html = mysoup_stock1.select('.pcstname')
stockname1 = stockname_html[0].text

stockname_html = mysoup_stock2.select('.pcstname')
stockname2 = stockname_html[0].text

stockname_html = mysoup_stock3.select('.pcstname')
stockname3 = stockname_html[0].text

stockname_html = mysoup_stock4.select('.pcstname')
stockname4 = stockname_html[0].text

stockname_html = mysoup_stock5.select('.pcstname')
stockname5 = stockname_html[0].text

stockname_html = mysoup_stock6.select('.pcstname')
stockname6 = stockname_html[0].text

stockname_html = mysoup_stock7.select('.pcstname')
stockname7 = stockname_html[0].text

stockname_html = mysoup_stock8.select('.pcstname')
stockname8 = stockname_html[0].text








#defining list of recepients
contacts = os.environ.get('office_mail_id')


#subject line of mail
mail_subject = 'Indian Stock price (BSE) information!'


#body of mail
hello = "Hello Myself,"
text_stock1 = "Stock price of " + stockname1 + " is : " + price_stock1
text_stock2 = "Stock price of " + stockname2 + " is : " + price_stock2
text_stock3 = "Stock price of " + stockname3 + " is : " + price_stock3
text_stock4 = "Stock price of " + stockname4 + " is : " + price_stock4
text_stock5 = "Stock price of " + stockname5 + " is : " + price_stock5
text_stock6 = "Stock price of " + stockname6 + " is : " + price_stock6
text_stock7 = "Stock price of " + stockname7 + " is : " + price_stock7
text_stock8 = "Stock price of " + stockname8 + " is : " + price_stock8






#Compiling mail
mail_msg = f'Subject: {mail_subject}\n\n{hello}\n\n{text_stock1}\n{text_stock2}\n{text_stock3}\n{text_stock4}\n{text_stock5}\n{text_stock6}\n{text_stock7}\n{text_stock8}'


#using SMTP method to send mail
with smtplib.SMTP(smtp_server,smtp_port) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(mail_user,mail_pass)
	smtp.sendmail(mail_user,contacts,mail_msg)
