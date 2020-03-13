from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('send_email/',views.send_email_to_user,name='send_email')
]
