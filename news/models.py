from __future__ import unicode_literals
from django.db import models
from cat.models import Cat  # Import from the correct app

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12,default="00:00")
    picname = models.TextField()
    picurl = models.TextField(default="-",blank=True)
    picture = models.ImageField(upload_to='images/', default='-')
    # pic=models.ImageField()
    writer = models.CharField(max_length=100)
    catname = models.CharField(max_length=100, default="-")   # default="-" for charfield
    catid = models.IntegerField(default=0)
    # ocatid = models.IntegerField(default=0)  # ocatid means original cat id.for count news
    ocatid = models.ForeignKey(
    Cat,  # This references the 'cat' model
    on_delete=models.SET_NULL,  # Or another appropriate on_delete action
    null=True,  # If you want to allow NULL values
    blank=True,  # If you want to allow blank in forms
    default=None,  # Adjust default as needed
    verbose_name='Category',  # Optional: more descriptive name
    db_column='ocatid'  # Optional: keep the same DB column name
)
    created_at = models.DateTimeField(auto_now_add=True)
    show = models.IntegerField(default=0)   # default=0 for integer field-when i use this in existing models
    tag = models.TextField(default="")   # For tag (Filtering)
    act = models.IntegerField(default=0)  # For Publish News
    rand = models.IntegerField(default=0)  # For Random Number of the News

        
    def __str__(self):
        return self.name