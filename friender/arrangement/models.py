from django.db import models

SEX = [
    ('m','male'),
    ('f','female')
]
class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices= SEX)
    email = models.EmailField(null=True,unique=True)
    city = models.CharField(max_length=100,default='Minsk')

def __str__(self):
    return self.name



CATEGORY = [
    ('r','restaurant'),
    ('c','cafe'),
    ('p','pub')
]
class Establishments(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40,choices=CATEGORY)
    addres = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

def __str__(self):
    return self.name