from rest_framework import permissions
from ne_sop_api.models import Item

class IsManagerPermission(permissions.BasePermission):
    """
    This will be reimplemented when OpenID will be fully functionnal.

    This permission is given to one or many users that are allowed to
    CRUD everything in app because they belong to Manager group.
    """
    message = 'Current user is not in Manager group.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()


class IsManagerOrReadOnlyPermission(permissions.BasePermission):
    """
    This will be reimplemented when OpenID will be fully functionnal.

    This permission is given to one or many users that are allowed to
    CRUD everything in app because they belong to Manager group.
    If they don't belong to Manager group, they can only view
    """
    message = 'Current user is not in Manager group.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Manager').exists()


class IsManagerOrReadUpdatePermission(permissions.BasePermission):
    """
    This will be reimplemented when OpenID will be fully functionnal.

    This permission allow everything but POST and DELETE. Only Manager group is
    allowed to POST
    """
    message = 'Current user is not in Manager group.'

    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'DELETE']:
            return request.user.groups.filter(name='Manager').exists()
        return True

def isAllowedRegadingEntitiesAndItemId(user, item_id):
    Item.objects.get(item_id).support.values_list("id", flat=True)
    user.entities.values_list("id", flat=True)