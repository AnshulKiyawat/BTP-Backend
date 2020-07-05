from django.db import models

class Posts(models.Model):
    email = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    date_of_post = models.DateField(blank=True,null=True)


    def __str__(self):
        return 'Email Id: "' + self.email +'" and content = "' + self.content+'"'
