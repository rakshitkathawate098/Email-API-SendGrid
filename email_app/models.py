from django.db import models

# Create your models here.


class EMAIL(models.Model):
    from_email=models.CharField(max_length=200)
    to_email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)

    def __str__(self):
        s="\n FROM: "+self.from_email+"\n"+"TO: "+self.to_email+"\n"
        ss=s+"Subject: "+self.subject+"\n"+"Content: "+self.content

        return ss
