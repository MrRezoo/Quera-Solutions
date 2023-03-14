from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    pass
