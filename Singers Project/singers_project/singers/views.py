from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import SingersSerializer
from . models import Singers

# Create your views here.

class SingerListCreateView(APIView):

    serializer_class = SingersSerializer

    def get(self,request,*args,**kwargs):

        singers = Singers.objects.all()

        singer_serializer = self.serializer_class(singers,many=True)

        data = {'singers' : singer_serializer.data}

        return Response(data=data,status=200)
    
    
    def post(self,request,*args,**kwargs):

        singer_serializer = self.serializer_class(data=request.data)

        if singer_serializer.is_valid():

            singer_serializer.save()

            return Response(data={'msg': 'singer created successfully'},status = 200)

        return Response(data=singer_serializer.errors,status=400)
    

class SingersRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        data = {'uuid':uuid,'msg':'this is retrieve view'}

        return Response(data=data,status=200)