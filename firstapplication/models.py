from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.IntegerField(default=0,unique= True)
    username = models.CharField(max_length=10)
    useraddress = models.CharField(max_length=50)
    usercontactnumber = models.IntegerField(default = 999)
    def __str__(self):
        return self.username


class Project(models.Model):
    userid = models.IntegerField(default=0)
    username = models.CharField(max_length=10)
    projectname = models.CharField(max_length=10)
    projectdetails = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class ProjectHrs(models.Model):
    username = models.CharField(max_length=10)
    projectname = models.CharField(max_length=10)
    startdate = models.DateField()
    enddate = models.DateField()
    def __str__(self):
        return self.username


