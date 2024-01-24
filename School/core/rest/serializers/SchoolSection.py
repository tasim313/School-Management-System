from rest_framework import serializers
from core.models import SchoolClass

from core.models import SchoolClass, SchoolSection

class SchoolSectionSerializer(serializers.ModelSerializer):
    school_class = serializers.SlugRelatedField(
        queryset=SchoolClass.objects.all(),
        slug_field="uid",
    )

    
    class Meta:
        model = SchoolSection
        fields = [
            "uid",
            "slug",
            "name",
            'school_class'
        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)
        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])

        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data=validated_data)
        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])

        return instance
