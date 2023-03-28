from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import User
from .serializers import UserRegistrSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import JsonResponse

@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.create(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data, status=HTTP_200_OK)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                token = Token.objects.get(user=user).key
                return Response({'token': token}, status=HTTP_200_OK)
            else:
                return Response({'error': 'User is not active.'}, status=HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'error':{
                    'code' : 401,
                    'message' : 'User not found.'
                    }
                }, status=401)
    else:
        return JsonResponse({'error':{
                'code' : 400,   
                'message' : 'Bad request'
                }
            }, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'GET':
        try:
            request.user.auth_token.delete()
            return JsonResponse({'data':{
                    'message' : 'logout'}
                }, status=HTTP_200_OK)
        except:
            return JsonResponse({'error':{
                    'code' : 401,
                    'message' : 'logout failed'
                    }
                }, status=401)
        
    else:
        return JsonResponse({'error':{
                'code' : 400,  
                'message' : 'Bad request'
                }
            }, status=400)
    