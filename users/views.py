from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.generics import ListCreateAPIView

from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


    def create(self,validated_data):
        username = validated_data.get('username')
        #testing query
        query = User.objects.filter(is_staff=True)
        print(query)
        user = User.objects.create(username=username)
        return user

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)