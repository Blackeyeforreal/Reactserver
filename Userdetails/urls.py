from django.urls import include, path
from django.conf.urls import  url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', views.LoginView.as_view(), name='user-login'),
]