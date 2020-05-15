from django.db import models
from django.utils import timezone
from ghost_post.utils import generate_secret_id

# Create your models here.


class Post(models.Model):
    is_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    secret_id = models.CharField(
        max_length=6,
        default=generate_secret_id
    )

    def __str__(self):
        return self.content
