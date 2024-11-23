from django.db import models

# Create your models here.
from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='tracks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
