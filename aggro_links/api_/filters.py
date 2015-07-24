from rest_framework.filters import BaseFilterBackend

class IsOwnerFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
