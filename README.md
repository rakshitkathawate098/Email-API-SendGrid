# Email-API-SendGrid
This is the EMAIL API to send Emails

1. Export environment Variables :
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env

2. Install library
pip install sendgrid

3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver 8080

6. copy the url seen in the terminal after above step
