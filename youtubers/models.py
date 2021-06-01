from django.db import models
from datetime import datetime
from  ckeditor.fields import RichTextField
# Create your models here.

class youtuber(models.Model):



    crew_choice = (
        ('solo','solo'),
        ('small','small up to 10 people'),
        ('medium','medium up to 50 people')
    ) 
    category_choice = (
        ('comedy','comedy'),
        ('coding','coding'),
        ('reviews','reviews'),
        ('film making ','film making'),
        ('other','other')
    )

    camera_choice = (
        ('canon','canon'),
        ('nikon','nikon'),
        ('red','red'),
        ('fuji  ','fuji'),
        ('other','other')
    )
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = "media/ytubers/%Y")
    city =  models.CharField(max_length=255)
    desc =  RichTextField()
    crew =  models.CharField( choices=crew_choice ,max_length=255)
    subs_count =  models.CharField(max_length=255)
    category =  models.CharField(choices=category_choice,max_length=255)
    price = models.IntegerField()
    age = models.IntegerField()
    height = models.IntegerField()
    camera_type =  models.CharField(choices=camera_choice,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    youtube_links = models.CharField(max_length=255)


    def __str__(self):
        return self.name
