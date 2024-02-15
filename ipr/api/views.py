from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import QuerySet
from rest_framework import decorators, permissions, viewsets
from rest_framework.response import Response

from .filters import TaskFilter, IprFilter
from .serializers import (
    CommentSerializer,
    CreateTaskSerializer,
    TaskSerializer,
    UserSerializer,
    EmployeeSerializer,
    CreateIprSerializer,
    ReadIprSerializer,
    UpdateTaskSerializer
)
from .permissions import (
    IsAuthenticatedReadOnly,
    IsAuthorIpr,
    IsAuthorIprOrIsEmployee,
)
from iprs.models import Ipr, Task
from users.models import User


class UserViewSet(
    viewsets.ReadOnlyModelViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedReadOnly,)

    def get_object(self):
        if self.kwargs['pk'] == 'me':
            return self.request.user
        return super().get_object()

    @decorators.action(
        methods=('get',),
        detail=False,
        pagination_class=None,
        url_name='get_subordinates'
    )
    def get_subordinates(self, request):
        user = request.user
        subordinates: QuerySet['User'] = user.subordinates.all()
        serializer = self.get_serializer(subordinates, many=True)
        return Response(serializer.data)
    
    @decorators.action(
        methods=('get',),
        detail=False,
        serializer_class=EmployeeSerializer
    )
    def subordinates_without_ipr(self, request):
        user = request.user
        subordinates: QuerySet['User'] = user.subordinates.filter(
            ipr_employee=None
        )
        page = self.paginate_queryset(subordinates)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(subordinates, many=True)
        return Response(serializer.data)


class IprViewSet(viewsets.ModelViewSet):
    """
    Текущий пользователь - руководитель - автор ИПР.
    """
    permission_classes = (IsAuthorIpr,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IprFilter
    filterset_fields = (
        'employee__last_name',
        'status'
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadIprSerializer
        return CreateIprSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Ipr.objects.filter(author=self.request.user)


class MyIprViewSet(viewsets.ModelViewSet):
    """
    Текущий пользователь - линейный сотрудник, для которого создали ИПР.
    """
    permission_classes = (IsAuthorIprOrIsEmployee,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IprFilter
    filterset_fields = ('status',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadIprSerializer
        return CreateIprSerializer

    def get_queryset(self):
        return Ipr.objects.filter(employee=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTaskSerializer
        if self.action in ['update', 'partial_update']:
            return UpdateTaskSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        ipr = get_object_or_404(Ipr, id=self.kwargs.get('ipr_id'))
        serializer.save(author=self.request.user, ipr=ipr)

    def get_queryset(self):
        ipr = get_object_or_404(Ipr, id=self.kwargs.get('ipr_id'))
        return ipr.tasks_ipr.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = None

    def perform_create(self, serializer):
        task = get_object_or_404(Task, id=self.kwargs.get('task_id'))
        serializer.save(author=self.request.user, task=task)

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs.get('task_id'))
        return task.comments.all()
