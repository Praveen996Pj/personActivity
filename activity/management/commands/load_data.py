import sys
import random
import pytz
from datetime import date, timedelta, datetime

from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import transaction

from ...models import Timezone, Person, PersonActivity

class Command(BaseCommand):

	def handle(self, *args, **options):
		try:
			with transaction.atomic():
				first_names = ['Jim', 'Joen', 'Joy', 'James', 'Jon', 'Chris']
				last_names = ['Smith', 'Lock', 'Diesel', 'Walker', 'Gadot', 'Pine']
				Timezone.populate()
				for i in range(0, 10):
					first_name = first_names[i%len(first_names)]
					last_name = last_names[i%len(last_names)]
					user = User.objects.create(
						username = '{}{}{}'.format(first_name, last_name, i),
						first_name = first_name,
						last_name = last_name,
						email = '{}{}{}@test.com'.format(first_name, last_name, i)
					)
					user.set_password('demo')
					user.save()
					_timezone = random.choice(Timezone.objects.all())
					person = Person.objects.create(
						user = user,
						tz = _timezone
					)

					for i in (0, 3):
						start_time = datetime(
							2020, random.randrange(1, 13), random.randrange(1,31),
							random.randrange(0, 24), random.randrange(1, 61), random.randrange(1, 61)
						)
						end_time = start_time + timedelta(minutes=random.randrange(50, 200))
						PersonActivity.objects.create(
							person = person,
							start_time = start_time,
							end_time = end_time
						)
		except Exception as e:
			print(e)
