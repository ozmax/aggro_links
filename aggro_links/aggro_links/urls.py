from django.conf.urls import url, include
from rest_framework import routers
from api_.views import LinkViewSet, ContactViewSet, CategoryViewSet, \
    CustomRegistrationView, CustomRootView, GroupViewSet, CustomUserView
from aggro_links.views import activation_frontend
from djoser.views import LoginView, LogoutView, ActivationView, UserView, \
    SetPasswordView, PasswordResetView, PasswordResetConfirmView


router = routers.DefaultRouter()
router.register(r'links', LinkViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
authpatterns = [
    url(
        r'^auth/$',
        CustomRootView.as_view(),
        name='auth_home'),
    url(
        r'^auth/me/$',
        CustomUserView.as_view(),
        name='user_info'),
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
        r'^auth/password/$',
        SetPasswordView.as_view(),
        name='login'),
    url(
        r'^auth/password/reset/$',
        PasswordResetView.as_view(),
        name='login'),
    url(
        r'^auth/password/reset/confirm/$',
        PasswordResetConfirmView.as_view(),
        name='login'),
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
