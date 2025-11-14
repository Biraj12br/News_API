import requests
import smtplib, ssl
import os
from email.message import EmailMessage


api_key='cd4fea836806407281d2607d11bd05eb'
topic='apple'
url=("https://newsapi.org/v2/everything?"
     f"q={topic}&"
     "from=2025-10-13&"
     "sortBy=publishedAt&"
     "apiKey=cd4fea836806407281d2607d11bd05eb&"
     "language=en")

#url='https://newsapi.org/v2/everything?q=apple&from=2025-11-12&to=2025-11-12&sortBy=popularity&apiKey=cd4fea836806407281d2607d11bd05eb&language=en'

#Make a request
response=requests.get(url)
#content=response.text

#Get data in form of dictionary
content=response.json()
#print(content)
#print(type(content))
news=''
for i in content['articles']:
    #print(i['title'])
    #print(i['description'])
    news= news + i['title'] +'\n'+ i['description'] + '\n' + i['url'] + 2*'\n'
#news=news.encode('utf-8')

'''def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sahoosubham351@gmail.com"
    password = "dzkl pzta hbxx xgpg"

    receiver = "mohantysatwikprasad@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email(news)'''


#create EmailMessage object
msg = EmailMessage()

msg['Subject'] = 'News about Tesla'
msg['From'] = 'sahoosubham351@gmail.com'
msg['To'] = 'sahoosubham351@gmail.com'
# For multiple recipients, use a comma-separated string:
# msg['To'] = 'recipient1@example.com, recipient2@example.com'

body=news
msg.set_content(body)

# Replace with your SMTP server details and credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'sahoosubham351@gmail.com'
password = 'dzkl pzta hbxx xgpg'

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Use for port 587 (TLS)
    # server = smtplib.SMTP_SSL(smtp_server, 465) # Use for port 465 (SSL)
    server.login(username, password)
    server.send_message(msg)





































