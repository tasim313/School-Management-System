from rest_framework import permissions

from school_auth.choice import UserRole


class IsSchoolAdmin(permissions.BasePermission):
    """
    Custom permission to only allow school admin to access the view.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_active:
            if request.user.role == UserRole.SCHOOL_ADMIN:
                return True
        else:
            return False


class IsTeacher(permissions.BasePermission):
    """
    Custom permission to only allow teacher to access the view.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_active:
            if request.user.role == UserRole.TEACHER:
                return True
        else:
            return False


class IsStudent(permissions.BasePermission):
    """
    Custom permission to only allow student to access the view.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_active:
            if request.user.role == UserRole.STUDENT:
                return True
        else:
            return False


class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow superuser to access the view.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_active:
            if request.user.is_superuser:
                return True
        else:
            return False
