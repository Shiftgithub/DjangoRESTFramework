# from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import *


@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called GET method',
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called POST method',
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called PATCH method',
        })
    else:
        return Response({
            'status': 400,
            'message': 'Yes! Django rest framework is working !!!',
            'method_called': 'You called invalid method',
        })

# @api_view(['GET'])
# def get_home(request):
#     return Response({
#         'status': 200,
#         'message': 'Yes! Django rest framework is working !!!'
#     })


@api_view(['GET'])
def Get_Todo(request):
    todo_objs = Todo.objects.all()
    seriazlier = TodoSerializer(todo_objs, many=True)
    return Response(
        {
            'status': True,
            'message': 'Todo fetched',
            'data': seriazlier.data
        }
    )


@api_view(['POST'])
def Post_Todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({
                'status': True,
                'message': 'Success Todo Created.',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'Invalid data',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'something went worng',
    })
