from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from .models import EMAIL

from django.shortcuts import render

from .forms import NameForm
from django.http import HttpResponseRedirect

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os

API_KEY="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"


'''
1. Export environment Variables :
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env

2. Install library
pip install sendgrid

3. make migrations

4. run server
'''


def get_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data)
            message=Mail(
            from_email=form.cleaned_data["from_email"],
            to_emails=form.cleaned_data['to_email'],
            subject=form.cleaned_data["subject"],
            html_content="<strong>"+form.cleaned_data["content"]+"</strong>"
            )
            try:
                for i in range(1):
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                    response = sg.send(message)
                    # print(response.status_code)
                    # print(response.body)
                    # print(response.headers)
                return HttpResponse("Email sent Successfully")
            except Exception as e:
                print(e.message)
                return HttpResponse("UN- Successful"+e.message)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'email_app/send_email.html', {'form': form})


def index(request):

    return HttpResponse("Successful")


def send_email_to_user(request):



    message = Mail(
        from_email='rakshitkathawate098@gmail.com',
        to_emails='kathawaterb@rknec.edu',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    print(request)
    try:
        for i in range(1):
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        return HttpResponse("Email sent Successfully")
    except Exception as e:
        print(e.message)
        return HttpResponse("UN- Successful"+e.message)
