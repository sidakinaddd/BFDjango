from django.shortcuts import render
import json
# Create your views here.
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo.auth_.models import MyUser
