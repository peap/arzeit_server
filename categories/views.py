from rest_framework import viewsets

from categories.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Categories a timer may belong to.
    """
    model = Category
