from django.dispatch import receiver
from django.db.models.signals import post_save
from numpy import base_repr
from activity.models import Person

@receiver(post_save, sender=Person)
def save_profile(sender, instance, created,**kwargs):
	# print('test')
	print(created)
	if created:
		id = instance.id
		temp_id = base_repr(id, 36)
		instance.person_id = temp_id.zfill(10)
		instance.save()
