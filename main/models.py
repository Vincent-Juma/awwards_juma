from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    '''
    This model will contain the fields for the user uploaded projects
    '''
    title = models.CharField(max_length=40)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='site_photos/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'

class Rating(models.Model):
    '''
    This model will contain the ratings for diffrent categories
    '''
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} {self.project.title} Rating'
