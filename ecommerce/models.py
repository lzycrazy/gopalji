
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

    


# Create your models here.
class Carausel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title 

 

class Categary(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name 



class Products(models.Model):
    categary = models.ForeignKey(Categary,on_delete=CASCADE)
    name = models.CharField(max_length=100)
    price = models.TextField()
    photo = models.ImageField(upload_to='images')
    slug=models.SlugField() 


    def __str__(self):
        return self.name 


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title 


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.email          


class Usercreationform(UserCreationForm):
    email=forms.EmailField(required=True, label='Email',error_messages={'exists': 'This is allready exist'})

    class Meta:
        model=User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.emailv=self.cleaned_data['email']
        if commit:
            user.save()
        return user
    def clean_email(self):
        if User.objects.filter(email=self.clean_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']





    
    




