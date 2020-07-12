from django.db import models

class ProjectOwners(models.Model):
    email =models.CharField(max_length=20,default='')
    project_id = models.IntegerField(primary_key=True)


    def __str__(self):
        return 'Email Id: "' + self.email +'"'

class Projects(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    skills_required = models.CharField(max_length=200)
    mentor = models.CharField(max_length=200,default='')
    description =models.CharField(max_length=200,default='')
    project_id = models.IntegerField(primary_key=True)
    members = models.IntegerField()


    def __str__(self):
        return 'Project Id: "' + str(self.project_id) +'"'
