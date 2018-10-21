from django.db import models
from datetime import date
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date_time = models.DateTimeField(auto_now = False)