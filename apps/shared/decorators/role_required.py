from django.core.exceptions import PermissionDenied
from functools import wraps

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied("User not authenticated")
            if not request.user.groups.filter(name=role_name).exists():
                raise PermissionDenied(f"User lacks role: {role_name}")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

coordinator_required = role_required("Coordinador")
teacher_required = role_required("Docente")