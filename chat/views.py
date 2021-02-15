from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Contact


def index(request):
    return render(request, "chat/index.html")


@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def user(request):
    username = request.data.get("username", None)
    if username is not None:
        Contact.objects.get_or_create(username=username)
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
