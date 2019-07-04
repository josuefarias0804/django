import datetime
import json

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def to_json(self):
        return {"id": 1, "question_text": "esto es una pregunta", "pub_date": "2012-04-23T18:25:43.511Z", "choices": [{id: 1, "choice_text": "opcion", "votes": 2}, {id: 2, "choice_text":'' }]}


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.choice_text} {self.question} {self.votes}'


