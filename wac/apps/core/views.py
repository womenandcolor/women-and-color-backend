from django.shortcuts import render
from django.views import View

from django import http
from django.core.serializers.json import DjangoJSONEncoder

from wac.apps.accounts.models import Profile
from wac.apps.core.models import Topic, Location
from wac.apps.contact_speaker.models import ContactForm

from collections import Counter
from dateutil.relativedelta import relativedelta

import json
import datetime

def json_response(objects):
    data = json.dumps(objects, cls=DjangoJSONEncoder)
    return http.HttpResponse(data, 'application/json')

class StatsView(View):
    def get(self, request):
        data = { "cities": {}, "registrations": {}, "messages_sent": {} }

        speaker_count = Profile.objects.filter(status=Profile.APPROVED).count()
        topics = Profile.objects.filter(status=Profile.APPROVED).values_list("topics", flat=True)
        topics_count = Topic.objects.filter(id__in=topics).distinct().count()
        top_10_topics_ids = [ topic[0] for topic in Counter(topics).most_common(10) ]
        top_10_topics_objects = Topic.objects.filter(id__in=top_10_topics_ids)
        top_topics = [topic.topic for topic in top_10_topics_objects]
        women_count = Profile.objects.filter(status=Profile.APPROVED, woman=True).count()
        poc_count = Profile.objects.filter(status=Profile.APPROVED, poc=True).count()
        woc_count = Profile.objects.filter(status=Profile.APPROVED, poc=True, woman=True).count()

        locations = Location.objects.all()
        for location in locations:
            location_count = Profile.objects.filter(status=Profile.APPROVED, location=location).count()
            data["cities"][location.city] = location_count

        start_date = datetime.datetime(2018, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)
        end_date = datetime.datetime.now(datetime.timezone.utc)

        start_window = start_date
        end_window = start_window + relativedelta(months=+1)

        while end_window < end_date:
            registrations_count = Profile.objects.filter(status=Profile.APPROVED, created_at__gt=start_window, created_at__lte=end_window).count()
            data["registrations"][start_window.strftime('%B %Y')] = registrations_count

            messages_count = ContactForm.objects.filter(created_at__gt=start_window, created_at__lte=end_window).count()
            data["messages_sent"][start_window.strftime('%B %Y')] = messages_count

            start_window = end_window
            end_window = start_window + relativedelta(months=+1)

        data["speakers"] = { "count": speaker_count }
        data["topics"] = { "count": topics_count, "most_frequently_used": top_topics }
        data["women"] = { "count": women_count }
        data["people_of_color"] = { "count": poc_count }
        data["women_of_color"] = { "count": woc_count }

        return json_response(data)

