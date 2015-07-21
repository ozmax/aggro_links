from django.conf.urls import url
from rest_framework import routers
from api_.views import LinkViewSet, ContactViewSet, \
    CustomRegistrationView, CustomRootView
from aggro_links.views import activation_frontend
from djoser.views import LoginView, LogoutView, ActivationView, UserView


router = routers.DefaultRouter()
router.register(r'links', LinkViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = []
authpatterns = [
    url(
        r'^auth/$',
        CustomRootView.as_view(),
        name='auth_home'),
    url(
        r'^auth/me/$',
        UserView.as_view(),
        name='user'),
    url(
        r'^auth/register/$',
        CustomRegistrationView.as_view(),
        name='register'),
    url(
        r'^auth/activate/',
        ActivationView.as_view(),
        name='activate'),
    url(
        r'^auth/activate_front/(?P<uid>\w{2,3})\/(?P<token>.*)',
        activation_frontend,
        name='activate_front'),
    url(
        r'^auth/login/$',
        LoginView.as_view(),
        name='login'),
    url(
        r'^auth/logout/$',
        LogoutView.as_view(),
        name='logout'),
]

urlpatterns += authpatterns
