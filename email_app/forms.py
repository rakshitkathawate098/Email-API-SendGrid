from django import forms

class NameForm(forms.Form):
    from_email = forms.CharField(label='Email from ', max_length=100)
    to_email= forms.CharField(label='Email To', max_length=100)
    subject= forms.CharField(label='Subject', max_length=100)
    content= forms.CharField(label='Content', max_length=1000)
