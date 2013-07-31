from rest_framework import viewsets

from timers.models import Timer, Interval


class TimerViewSet(viewsets.ModelViewSet):
    """
    Timers
    """
    model = Timer


class IntervalViewSet(viewsets.ModelViewSet):
    """
    Intervals during which timers were active
    """
    model = Interval
