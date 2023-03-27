from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Problem(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    score = models.PositiveIntegerField(default=100)


class Submission(models.Model):
    participant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name="submissions"
    )

    submitted_time = models.DateTimeField()
    code = models.URLField()
    score = models.PositiveIntegerField(default=0)
