from rest_framework import serializers

from SchoolAdminApp.models import (
    PurchaseReceived,
    Vendor,
    Product,
    ProductCategory,
    PurchaseRequest,
)
from common.models import SchoolInformationOnBoarding


class CategorySlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            "uid",
            "slug",
            "name",
        ]


class SchoolInformationOnBoardingSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolInformationOnBoarding
        fields = [
            "uid",
            "slug",
            "name",
            "address",
            "phone",
            "school_type",
            "username"
        ]


class VendorSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "uid",
            "slug",
            "name",
            "address",
            "phone_number",
        ]


class ProductSlimSerializer(serializers.ModelSerializer):
    category = CategorySlimSerializer()

    class Meta:
        model = Product
        fields = [
            "uid",
            "slug",
            "name",
            "description",
            "category",
        ]


class PurchaseRequestSlimSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseRequest
        fields = [
            "uid",
            "slug",
            "purchase_request_status",
            "order_date",
            "delivery_date",
            "amount_tax",
            "payment_method",
        ]
        read_only_fields = ["uid", "slug"]


class PurchaseReceivedSerializer(serializers.ModelSerializer):
    school_purchase_received = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    purchase_received_vendor = serializers.SlugRelatedField(
        queryset=Vendor.objects.all(),
        slug_field="uid",
    )
    purchase_request = serializers.SlugRelatedField(
        queryset=PurchaseRequest.objects.all(),
        slug_field="uid",
    )
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="uid",
        many=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = PurchaseReceived
        fields = [
            "uid",
            "slug",
            "purchase_received_status",
            "order_date",
            "delivery_date",
            "partially_received",
            "all_received",
            "amount_tax",
            "payment_method",
            "note_private",
            'note_public',
            'school_purchase_received',
            'purchase_received_vendor',
            "purchase_request",
            'product'

        ]
        read_only_fields = ["uid", "slug"]

    def create(self, validated_data):
        products_data = validated_data.pop('product', None)
        instance = super().create(validated_data=validated_data)

        if products_data:
            for product_data in products_data:
                instance.product.add(product_data)

        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])
        return instance

    def update(self, instance, validated_data):
        products_data = validated_data.pop('product', None)
        instance = super().update(instance, validated_data=validated_data)

        if products_data is not None:
            instance.product.set(products_data)

        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])
        return instance


class PurchaseReceivedListSerializer(serializers.ModelSerializer):
    school_purchase_received = SchoolInformationOnBoardingSlimSerializer()
    purchase_received_vendor = VendorSlimSerializer()
    purchase_request = PurchaseRequestSlimSerializer()
    product = ProductSlimSerializer(many=True)

    class Meta:
        model = PurchaseReceived
        fields = [
            "uid",
            "slug",
            "purchase_received_status",
            "order_date",
            "delivery_date",
            "partially_received",
            "all_received",
            "amount_tax",
            "payment_method",
            "note_private",
            'note_public',
            'school_purchase_received',
            'purchase_received_vendor',
            "purchase_request",
            'product'

        ]
        read_only_fields = ["uid", "slug"]