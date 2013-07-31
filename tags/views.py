from rest_framework import viewsets

from tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    """
    Tags describing Interval objects.
    """
    model = Tag
