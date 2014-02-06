# utf-8
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group