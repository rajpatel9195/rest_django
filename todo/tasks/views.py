from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status

class taskAPI(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response({'status':200,'message':serializer.data})

    def post(self,request):
        serializer = TaskSerializer( data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
        serializer.save()    
        return Response({'status':200,'message':serializer.data})
        
    
    def put(self,request):
        try:
            task = Task.objects.get(id = request.data['id'])
            serializer = TaskSerializer( task,data=request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()    
            return Response({'status':200,'message':serializer.data})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
    
    
    def patch(self,request):
        try:
            task = Task.objects.get(id = request.data['id'])
            serializer = TaskSerializer( task,data=request.data)
            if not serializer.is_valid():
                return Response({'status':403,'error':serializer.errors,'message':'something went wrong'})
            serializer.save()    
            return Response({'status':200,'message':serializer.data})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
        
        
    def delete(self,request):
        try:
            task = Task.objects.get(id = request.data['id'])
            task.soft_delete()
            return Response({'status':200,'message':"deleted"})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
        
@api_view(['GET'])    
def taskall(request):
        tasks = Task.deletedall.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response({'status':200,'message':serializer.data})  
    