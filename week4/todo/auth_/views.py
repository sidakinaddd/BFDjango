from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from ..auth_.serializers import UserSerializer
from ..auth_.models import MyUser

class RegisterUser(APIView):
    http_method_names = ['post']
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return MyUser.objects.all()
# @csrf_exempt
# def login(request):
#     body = json.loads(request.body.decode('utf-8'))
#     username = body.get('username')
#     password = body.get('password')
#
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return JsonResponse({'message': 'logged in '}, status=200)
#     else:
#         return JsonResponse({'message': 'user not found'}, status=404)
#
#
# @csrf_exempt
# def logout(request):
#     user = auth.logout(request)
#     return JsonResponse({'message': 'logged out'}, status=200)
#
#
# @csrf_exempt
# def register(request):
#     body = json.loads(request.body.decode('utf-8'))
#     username = body.get('username')
#     password = body.get('password')
#
#     user = MyUser.objects.create_user(username=username)
#     user.set_password(password)
#     user.save()
#
#     return JsonResponse({'message': f'user with username {user.username} created'}, status=200)
#
