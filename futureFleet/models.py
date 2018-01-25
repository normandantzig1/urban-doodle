import datetime
from django.utils import timezone

from django.db import models

# Create your models here.

#--comics--
class Comic(models.Model):
    #title
    comic_title_text = models.CharField(max_length=200)
    #date
    comic_pub_date = models.DateTimeField('comic date published')
    #image
    comic_location = models.CharField(max_length=200)
    #explanation
    comic_explanation_text = models.CharField(max_length=400, blank=True)
    #comic number
    #comic_number = models.pr

    def __str__(self):
        return self.comic_title_text

    def was_published_recently(self):
        return self.comic_pub_date >= timezone.now() - datetime.timedelta(days=1)


#--Blog--
class Blog(models.Model):
    #title
    blog_title_text = models.CharField(max_length=200)
    #date
    blog_pub_date = models.DateTimeField('blog date published')
    #content
    blog_content_text = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_title_text

"""

#---------------------------------
# from example
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#----------------------------------------------
"""
