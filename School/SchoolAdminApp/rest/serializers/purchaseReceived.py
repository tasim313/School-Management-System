from rest_framework import serializers

from SchoolAdminApp.models import PurchaseReceived, Vendor, Product, PurchaseRequest
from common.models import SchoolInformationOnBoarding


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