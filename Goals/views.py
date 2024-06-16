from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer,TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import todo
from rest_framework_simplejwt.authentication import JWTAuthentication

class NewTodoAPI(CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailAPI(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return todo.objects.filter(user=self.request.user)
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]


# Create your views here.
# def newTodoAPI(request):