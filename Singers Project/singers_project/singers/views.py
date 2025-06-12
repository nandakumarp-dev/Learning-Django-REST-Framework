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

    serializer_class = SingersSerializer

    def get(self,request,*args,**kwargs):
        uuid = kwargs.get('uuid')
        singer = Singers.objects.get(uuid=uuid)
        singer_serializer = self.serializer_class(singer)
        return Response(data=singer_serializer.data,status=200)

    def put(self,request,*args,**kwargs):
        uuid = kwargs.get('uuid')
        singer = Singers.objects.get(uuid=uuid)
        singer_serializer = self.serializer_class(instance=singer,data=request.data,partial=True)
        if singer_serializer.is_valid():
            singer_serializer.save() 
            return Response(data={'msg':'Singer updated successfully'},status=200)
        return Response(data=singer_serializer.errors,status=400)
    
    def delete(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        singer = Singers.objects.get(uuid=uuid)
        singer.delete()
        return Response(data={'msg':'Singer deleted successfully'}, status=204)
    