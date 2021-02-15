from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_length(value):
    print(value)
    if len(value) <= 4:
        raise ValidationError(
            _("Username must be unique and 4-15 characters in length")
        )


class Contact(models.Model):
    username = models.CharField(
        max_length=30, unique=True, validators=[validate_length]
    )

    def __str__(self):
        return self.username


class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.username
