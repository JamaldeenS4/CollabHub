from rest_framework import serializers
from .models import Team, TeamMembership


class TeamSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = [
            "id",
            "name",
            "users",
        ]


class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = [
            "id",
            "user",
            "team",
            "role",
            "date_added",
        ]
        read_only_fields = ["date_added"]