from django.db import models


class user_register(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)
    img=models.FileField()


class add_song(models.Model):
    m_id=models.CharField(max_length=200)
    songname=models.CharField(max_length=200)
    descp=models.CharField(max_length=200)
    artistname=models.CharField(max_length=200)
    audio=models.FileField()
    cover=models.FileField()
    