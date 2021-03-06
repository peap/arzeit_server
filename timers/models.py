from datetime import datetime, timedelta

from django.db import models
from django.utils.timezone import now

from categories.models import Category
from tags.models import Tag


class Timer(models.Model):

    category = models.ForeignKey(Category)

    name = models.CharField(
        max_length=100,
    )

    active = models.BooleanField(
        default=False,
    )

    def start(self):
        interval = Interval()
        interval.timer = self
        interval.save()

        self.active = True
        self.save()

    def stop(self):
        interval = Interval.objects.get(
            timer=self,
            end=None,
        )
        interval.end = now()
        interval.save()

        self.active = False
        self.save()

    @property
    def today(self):
        """
        Total time for today as a datetime.timedelta object.
        """
        today = now()
        intervals = Interval.objects.filter(
            timer=self,
            start__year=today.year,
            start__month=today.month,
            start__day=today.day,
        )
        total = timedelta(0)
        for interval in intervals:
            total += interval.length
        return total

    @property
    def last_week(self):
        """
        Total time for last_week as a datetime.timedelta object.
        """
        year, week, dow = (now() - timedelta(days=7)).isocalendar()
        intervals = Interval.objects.filter(
            timer=self,
            start__year=year,
            week=week,
        )
        total = timedelta(0)
        for interval in intervals:
            total += interval.length
        return total


class Interval(models.Model):

    timer = models.ForeignKey(Timer)

    week = models.IntegerField(
        db_index=True,
    )

    year = models.IntegerField(
        db_index=True,
    )

    start = models.DateTimeField(
        auto_now_add=True,
    )

    end = models.DateTimeField(
        blank=True,
        null=True,
    )

    tags = models.ManyToManyField(Tag,
        blank=True,
        null=True,
        db_index=True,
    )

    notes = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )

    def __init__(self, *args, **kwargs):
        today = now()
        year, week, dow = today.isocalendar()
        kwargs['week'] = week
        kwargs['year'] = today.year
        kwargs['start'] = now()
        super().__init__(*args, **kwargs)

    @property
    def length(self):
        """
        Length of the interval. Returns datetime.timedelta object.
        """
        if self.end is None:
            length = now() - self.start
        else:
            length = self.end - self.start
        return length
