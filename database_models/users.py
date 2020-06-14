from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200,default='')
    middle_name =models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    profile_description = models.CharField(max_length=1000,default='')
    gender = models.CharField(max_length=25,default='')
    date_of_birth = models.DateField(blank=True,null=True)


    def __str__(self):
        return 'Email Id: "' + self.email +'"'
