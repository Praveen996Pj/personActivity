from django.http import HttpResponse
import json
from activity.models import PersonActivity, Person

def test(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	try:
		persons = Person.objects.select_related(
			'user', 'tz'
		).filter(personactivity__isnull=False)
		members = []
		for person in persons:
			data = {
				'id': person.person_id,
				'real_name': '{} {}'.format(
					person.user.first_name, person.user.last_name),
				'tz': person.tz.tz
			}
			activity_periods = []
			personActivities = PersonActivity.objects.filter(person=person)
			for personActivity in personActivities:
				activity_periods.append({
					'start_time' : personActivity.start_time.strftime('%b %d %Y  %I:%M%p'),
					'end_time' : personActivity.end_time.strftime('%b %d %Y  %I:%M%p')
				})
			data['activity_periods'] = activity_periods
			members.append(data)
		return HttpResponse(
			json.dumps({'ok': True, 'members': members}),
			content_type='application/json'
		)
	except Exception as e:
		print(e)

	return HttpResponse(
		json.dumps({'success': False}),
		content_type='application/json'
	)
