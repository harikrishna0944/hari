from django.db import models
from django.urls import reverse

# Create your models here.
class json(models.Model):
    end_year=models.CharField(max_length=100)
    intensity=models.IntegerField()
    sector=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    insight=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    start_year=models.CharField(max_length=100)
    impact=models.CharField(max_length=100)
    added=models.CharField(max_length=100)
    published=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    relevance=models.IntegerField()
    pestle=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    likelihood=models.IntegerField()


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('deatial',kwargs={'pk':self.pk})
    
    
