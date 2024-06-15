from rest_framework import serializers

from .models import Invitation


class InvitationCodesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Invitation
        fields = [
            'sub_code',
            'accept_code'
        ]

