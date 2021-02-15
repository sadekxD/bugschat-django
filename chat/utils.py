from .models import Message, Contact
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


def get_last_10_messages():
    return Message.objects.order_by("-timestamp")[:10]


def get_user_contact(username):
    return get_object_or_404(Contact, username=username)
