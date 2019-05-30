from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	git_url=models.URLField()
	date=models.DateTimeField()

	def __str__(self):
		return self.title
