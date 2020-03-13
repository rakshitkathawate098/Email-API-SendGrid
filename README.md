# Email-API-SendGrid
This is the EMAIL API to send Emails
CLONE OR DOWNLOAD THE COMPLETE PROJECT
and then run following steps

a. Export environment Variables :
  1. echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
  2. echo "sendgrid.env" >> .gitignore
  3. source ./sendgrid.env

b. Install library : ```pip install sendgrid```

c. ```python manage.py makemigrations```

d. ```python manage.py migrate```

e. ```python manage.py runserver 8080```

f. copy the url seen in the terminal after above step ex: http://127.0.0.1:8080/ in web broeser

g. now extend the url with address http://127.0.0.1:8080/email/get_email to see the email form
