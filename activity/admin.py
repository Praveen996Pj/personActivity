from django.contrib import admin
from .models import Person, PersonActivity, Timezone
# Register your models here.

admin.site.register(Person)
admin.site.register(PersonActivity)
admin.site.register(Timezone)
