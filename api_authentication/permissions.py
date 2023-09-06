from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Kiểm tra nếu người dùng là superuser
        if request.user.is_superuser:
            return True
        return False