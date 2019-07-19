from django.http import StreamingHttpResponse
from django.utils import timezone
from datetime import datetime
from urllib.request import urlopen


from django.db import models
import json




class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def to_json(self):
        # choice_text_tojson = Choice.objects.filter(question__pub_date__year=timezone.now().year)
        my_dict = [{self.id, "choice_text": choice_text_tojson, "votes": 2}, {self.id: 2, "choice_text": choice_text_tojson}]
        timestampStr = self.pub_date.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        return json.dumps({"id": self.id, "question_text": self.question_text, "pub_date": timestampStr, "choices": str(my_dict)})



class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
       return f'{self.id}: {self.choice_text} {self.question} {self.votes}'

    def to_json(self):
        return json.dumps({"id": self.id, "choice_text": self.choice_text, "votes": self.votes})