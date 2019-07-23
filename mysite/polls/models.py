from django.http import StreamingHttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
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
        # my_dict = [{self.id, "choice_text": choice_text_tojson, "votes": }, {self.id, "choice_text": choice_text_tojson}]
        # a = Question(id=None, question_text="This is a test", pub_date=date(2005, 7, 27), choice=c)

        timestampStr = self.pub_date.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        return json.dumps({"id": self.id, "question_text": self.question_text, "pub_date": timestampStr, "choices": self.choice })



class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    choice = (question, choice_text, votes)

    def __str__(self):
       return f'{self.id}: {self.choice_text} {self.question} {self.votes}'

    def to_json(self):
        return json.dumps({"id": self.id, "choice_text": self.choice_text, "votes": self.votes})