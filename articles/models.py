from django.db import models
from django.contrib.auth.models import AbstractUser

class Articles(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=50, null=False)
    summary = models.TextField(max_length=200)
    firstParagraph = models.TextField(max_length=400)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, null=False)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Authors(models.Model):
    name = models.CharField(max_length=30, null=False)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Usuario(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.SlugField(max_length=255)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']