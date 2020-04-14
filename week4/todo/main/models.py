from django.db import models
from datetime import datetime
from auth_.models import MyUser
from django.contrib import admin


# Create your models here.
class TodoListManager(models.Model):
    def for_user(self, user):
        return self.filter(owner=user)


class ToDoList(models.Model):
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)
    objects = TodoListManager()

    class Meta:
        verbose_name = 'TodoList'
        verbose_name_plural = 'TodoLists'



class ToDoManager(models.Model):
    pass


class ToDo(models.Model):
    name = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(default=datetime.now)
    finish_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')

    objects = ToDoManager

    class Meta:
        verbose_name = "Todo  task"
        verbose_name_plural = "Todo tasks"

    def __str__(self):
        return f'{self.name}, in {self.todo_list}'




