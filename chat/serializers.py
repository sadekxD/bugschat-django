from rest_framework import serializers
from .models import Message

# from .utils import get_user_contact


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
