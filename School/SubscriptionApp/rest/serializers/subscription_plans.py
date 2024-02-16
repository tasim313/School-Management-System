"""Serializers for subscription plan model."""

from rest_framework import serializers

from SubscriptionApp.models import SubscriptionPlan


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = [
            "uid",
            "slug",
            "name",
            "duration_months",
            "price",
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)

        # Add user_created by request user
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)

        # Add user_updated by request user
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
