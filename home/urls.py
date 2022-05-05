from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from api.views import AssignmentViewSetFBV


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('assignments/', include('api.assignments.urls')),
    path('assignment/fbv/', AssignmentViewSetFBV),
    path('graded-assignments/', include('api.graded_assignments.urls')),
    path('users/', include('users.urls')),
    path('upload/', include('api.upload.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
