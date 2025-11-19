from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # /tasks/?completed=True
    filterset_fields = ['completed']

    # /tasks/?search=buy
    search_fields = ['title', 'description']

    # /tasks/?ordering=title or -title or completed
    ordering_fields = ['title', 'completed', "id"]

    # Default ordering
    ordering = ['id']