from rest_framework import permissions


class IsActive(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.user.is_authenticated() and request.user.is_active):
            return True


class CanLogin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_active:
            return True
