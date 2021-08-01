from django.db import models


# Create your models here.

class Team(models.Model):
    # TODO creating a model for Exec team
    # img/full name/jobTitle/facebookLink/googleLink
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # todo change ui
    def __str__(self):
        return self.first_name
