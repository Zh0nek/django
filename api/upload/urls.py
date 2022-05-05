import django
from django.conf.urls import url
from django.urls import include
from rest_framework import routers, serializers, viewsets

class Photo(django.db.models.Model):
    file = django.db.models.ImageField()

    def __str__(self):
        return self.file.name

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'file')   # <-- HERE

class PhotoViewSet(viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)

api_urlpatterns = ([
    url('', include(router.urls)),], 'api')


urlpatterns = [
    url(r'', include(api_urlpatterns)),
]