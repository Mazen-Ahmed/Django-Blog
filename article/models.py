from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class article(models.Model):
    title=models.CharField(max_length=100)
    body=RichTextUploadingField(max_length=900)
    pic=models.ImageField(upload_to='pics',default='')
    date=models.DateTimeField(auto_now=False,auto_now_add=True)
    User=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20]+'...'
