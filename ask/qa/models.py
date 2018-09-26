# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
        def new():                                                              
                pass                                                            
        def popular():                                                          
                pass 
          
class Question(models.Model):
  objects = QuestionManager() 
  title = models.CharField(max_length = 255)
  text = models.TextField()
  added_at = models.DateField(blank = True)
  rating = models.IntergerField()
  author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  likes = models.ManyToManyField(Likes)
  
  def __str__(self):
    return self.title
  def get_absolute_url(self):
    return '/question/%d/' %self.pk

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(blank = True)
  question = models.ForeignKey(Question, null = True, on_delete = models.SET_NULL)
  author = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  
  def __str__(self):
    return self.text
