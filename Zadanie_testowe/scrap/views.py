from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Text,Author,Stats
from .serializer import TextSerializer,AuthorSerializer,StatsSerializer
from scrap.todb import todb
# Create your views here.

# lists all stack or create a new one
# class TextList(APIView):
#
#     def get(self, request):
#         stats = Text.objects.all()
#         serializer = TextSerializer(stats, many=True)
#         return Response(serializer.data) #JSON.data
#
#     def post(self):
#         pass



class Authors(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data) #JSON.data


class StatsList(APIView):

    def get(self,request):
        stats = Stats.objects.all()
        serializer = StatsSerializer(stats,many=True)
        return Response(serializer.data)


#Dodawanie do bazy danych
# todb()