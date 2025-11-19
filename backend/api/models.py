from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

# /auth/register/

# /auth/login/ (JWT)

# /auth/logout/

# /auth/refresh/

# protect endpoints like /tasks/

class AuthenticatedModel(models.Model):
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True