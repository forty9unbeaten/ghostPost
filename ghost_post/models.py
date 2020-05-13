from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    is_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
