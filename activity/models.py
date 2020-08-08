from django.db import models
from django.contrib.auth.models import User
import pytz
# Create your models here.

class Timezone(models.Model):
	tz = models.CharField(max_length=20)

	@classmethod
	def populate(cls):
		timezones = pytz.all_timezones
		for tz in timezones:
			cls.objects.get_or_create(tz=tz)

	def __str__(self):
		return self.tz

class Person(models.Model):
	person_id = models.CharField(max_length=10, unique=True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	tz = models.ForeignKey(Timezone, on_delete = models.PROTECT)

	class Meta:
		unique_together = ('user', 'tz')

class PersonActivity(models.Model):
	person = models.ForeignKey(Person, on_delete = models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
