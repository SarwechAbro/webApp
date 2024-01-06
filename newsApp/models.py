from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=250)
   
    def __str__(self):
         return self.name
     
class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    def __str__(self):
          return self.body


class News(models.Model): 
    topics = models.ManyToManyField(Topic, related_name='news')
    body = models.TextField(null=True, blank=True)
    def __str__(self):
         return self.body
           