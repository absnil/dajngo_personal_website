from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to='files/')
    desc=models.TextField()
    date=models.DateTimeField()


    def __str__(self):
        return self.title
