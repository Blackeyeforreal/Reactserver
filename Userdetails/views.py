from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,views,permissions , generics,response,authentication
from django.contrib.auth import login
from .serializers import UserSerializer, Loginserializer, postserializer
from .models import Users, Posts

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UserSerializer


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        serializer = Loginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('id')
    serializer_class = postserializer