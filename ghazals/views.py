from django.shortcuts import render
from .models import Ghazal,Discussion,Reaction
from rest_framework import generics
from .serializers import GhazalSerializer,DiscussionSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
# Create your views here.


class GhazalCreateAndRead(generics.ListCreateAPIView):
    serializer_class = GhazalSerializer
    queryset = Ghazal.objects.all()
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class GhazalGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GhazalSerializer
    queryset = Ghazal.objects.all()


class DiscussionCreate(generics.CreateAPIView):
    serializer_class = DiscussionSerializer
    queryset = Discussion.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        ghazal_id = self.request.data.get('ghazal')
        ghazal_instance = get_object_or_404(Ghazal, pk=ghazal_id)
        serializer.save(commented_by=self.request.user, ghazal=ghazal_instance)


class DiscussionRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscussionSerializer
    queryset = Discussion.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAuthenticated()]