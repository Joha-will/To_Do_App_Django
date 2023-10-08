from django.db import models


class Task(models.Model):

    task = models.CharField(max_length=254)
    is_completed = models.BooleanField(default=False)
    create_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task