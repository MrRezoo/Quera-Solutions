from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from projects.models import Project, ProjectMembership


def active_project(request, project_id):
    user = request.user
    project = get_object_or_404(Project, id=project_id)
    membership = ProjectMembership.objects.filter(user=user, project=project).first()
    if not membership:
        raise Http404("Project or membership not found")

    with transaction.atomic():
        ProjectMembership.objects.filter(user=user).update(is_current=False)
        membership.is_current = True
        membership.save()
    return redirect('index')
