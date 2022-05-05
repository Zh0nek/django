import json
from venv import logger

from requests import Response
from rest_framework import viewsets, views, status
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def user_change(self, request):
        logger.info('user change')
        data = json.loads(request.body)
        user = User.objects.get(id=data['pk'])
        user.is_student = False
        user.is_teacher = True
        user.save()
        return Response({"status": "not student"}, status=status.HTTP_200_OK)


