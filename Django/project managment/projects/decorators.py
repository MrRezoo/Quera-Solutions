from functools import wraps

from django.http import HttpResponseForbidden, HttpResponseNotFound

from projects.models import ProjectMembership


# noinspection PyPep8Naming
class projects_panel(object):
    def __init__(self, permissions=None):
        self.permissions = permissions

    def __call__(self, view_func):
        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            memberships = ProjectMembership.objects.filter(user=request.user)
            if not memberships.exists():
                return HttpResponseNotFound("No projects found")

            request.memberships = memberships
            current_membership = memberships.filter(is_current=True).first()
            if not current_membership:
                current_membership = memberships.order_by('id').first()
                current_membership.is_current = True
                current_membership.save()

            request.current_membership = current_membership
            request.project = current_membership.project

            if self.permissions:
                for permission in self.permissions:
                    if not current_membership.has_permission(permission):
                        return HttpResponseForbidden("You do not have permission to perform this action")
            return view_func(request, *args, **kwargs)

        return _wrapper_view
