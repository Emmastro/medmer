from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permissiob to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        #Read permissions allowed to any request,
        #so we'll always allow GET, HEAD or OPTIONS request

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user