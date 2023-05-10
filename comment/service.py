from django.db.models import Q
from user.models import GuestUser


def guest_get_or_create(validated_data):
    guest = validated_data['guest']
    username = guest['username']
    email = guest['email']
    try:
        guest = GuestUser.objects.get(Q(username=username) | Q(email=email))
    except GuestUser.DoesNotExist:
        guest = GuestUser.objects.create(username=username, email=email)
    return guest
