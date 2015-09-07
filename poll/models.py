from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pubdate = models.DateTimeField("publication_date", default=timezone.now)

    def was_published_recently(self):
        return timezone.now() < self.pubdate + timedelta(days=1)
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'
    was_published_recently.admin_order = 'pubdate'

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.choice_text
