from django.db import models
from django.utils import timezone


class Todo(models.Model):
	task = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.task



class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skill = models.CharField(max_length=100)


class Education(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.TextField()

class Project(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    achievement1 = models.TextField()
    achievement2 = models.TextField()
