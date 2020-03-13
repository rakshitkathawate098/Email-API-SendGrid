from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('send_email/',views.send_email_to_user,name='send_email'),
    path('get_email/',views.get_email,name="get_email")
]
