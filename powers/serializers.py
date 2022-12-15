from rest_framework import serializers
from .models import Power


class PowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # works alongside permissions.py to obtain owner in comparison to profile
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Power
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'speed', 'flight', 'strength', 'vision',
            'fire', 'lasers', 'is_owner'
        ]
