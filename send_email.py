# Referenced the notifications example file
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

message = Mail(
    from_email= MY_ADDRESS,
    to_emails= input("Enter your email"),
    subject='Your Receipt From Happy Foods',
    html_content= format_text(selected_ids)
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)
except Exception as e:
    print("OOPS",e.message)




