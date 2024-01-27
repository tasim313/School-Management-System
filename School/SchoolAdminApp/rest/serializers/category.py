from rest_framework import serializers

from SchoolAdminApp.models import ProductCategory

from common.models import SchoolInformationOnBoarding


class ProductCategoryListSerializer(serializers.ModelSerializer):
    school_product_category = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    
    class Meta:
        model = ProductCategory
        fields = [
            "uid",
            "slug",
            "name",
            "school_product_category",
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
