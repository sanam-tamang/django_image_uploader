from django.db import models
import uuid

class NewsFeed(models.Model):
    id = models.UUIDField(primary_key= True,default=uuid.uuid4)
    caption = models.TextField(max_length=5000,null=True)
    image = models.ImageField(null= True, upload_to='media/')
