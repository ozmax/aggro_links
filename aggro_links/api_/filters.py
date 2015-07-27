from rest_framework.filters import BaseFilterBackend
from rest_framework.serializers import ValidationError

class IsOwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated():
            return queryset.filter(owner=request.user)
        else:
            raise ValidationError({"detail": "No credentials provided."})
