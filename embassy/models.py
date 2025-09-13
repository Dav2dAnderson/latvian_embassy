from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser
# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Meeting(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='meetings')
    meet_time = models.DateTimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.customer.username
    



    