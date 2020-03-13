from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

API_KEY="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"


'''
1. Export environment Variables :
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env

2. Install library
pip install sendgrid
'''

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def send_email_to_user(request):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email='rakshitkathawate098@gmail.com',
        to_emails='kathawaterb@rknec.edu',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        for i in range(1):
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        return HttpResponse("Successful")
    except Exception as e:
        print(e.message)
        return HttpResponse("UN- Successful"+e.message)
