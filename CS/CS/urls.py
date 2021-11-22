from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from rest_framework import routers,serializers,viewsets
from django.contrib.auth.models import User
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static
from django.conf import settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^Profile/',include('Profile.urls')),
    re_path(r'^Login/',include('Login.urls')),
    re_path(r'^Friend/',include('FriendUser.urls')),
    re_path(r'^Search/',include('Search.urls')),
    url('Api/',schema_view),
]
