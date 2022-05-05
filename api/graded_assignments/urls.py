from django.urls import path
from api.views import GradedAssignmentListView, GradedAssignmentCreateView, GradedAssignmentByTeacherListView, \
    GradedAssignmentListViewFBV

urlpatterns = [
    path('', GradedAssignmentListView.as_view()),
    path('fbv/', GradedAssignmentListViewFBV),
    path('by_teacher/', GradedAssignmentByTeacherListView.as_view()),
    path('create/', GradedAssignmentCreateView.as_view()),
]
