from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
from rest_framework.views import APIView

from .models import Assignment, GradedAssignment, Question
from .serializers import AssignmentSerializer, GradedAssignmentSerializer, QuestionSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_queryset(self):
        queryset = Assignment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(teacher__username=username)
        return queryset

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer
    querysetTest = GradedAssignment.test_teachers.all()
    print("Test", querysetTest)

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(student__username=username)
        return queryset


def GradedAssignmentListViewFBV(request):
    if request.method == 'GET':
        data = list(GradedAssignment.objects.values())
        username = request.GET.get('username')
        if username is not None:
            data = list(GradedAssignment.objects.filter(assignment__teacher__username=username).values())
        return JsonResponse(data, safe=False)
    else:
        pass


def AssignmentViewSetFBV(request):
    if request.method == 'GET':
        data = list(Assignment.objects.values())
        username = request.GET.get('username')
        if username is not None:
            data = list(Assignment.objects.filter(teacher__username=username).values())
        return JsonResponse(data, safe=False)
    else:
        pass


class GradedAssignmentByTeacherListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(assignment__teacher__username=username)
        return queryset


class GradedAssignmentCreateView(CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()

    def post(self, request):
        print(request.data)
        serializer = GradedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class QuestionAssignmentCreateView(CreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_view_name(self, request):
        pass

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
