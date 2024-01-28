from rest_framework import serializers

from SchoolAdminApp.models import PurchaseRequest, Vendor, Product
from common.models import SchoolInformationOnBoarding


class PurchaseRequestSerializer(serializers.ModelSerializer):
    
    school_purchase_request = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    purchase_request_vendor = serializers.SlugRelatedField(
        queryset=Vendor.objects.all(),
        slug_field="uid",
    )
    product_request = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="uid",
        many=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = PurchaseRequest
        fields = [
            "uid",
            "slug",
            "purchase_request_status",
            "order_date",
            "delivery_date",
            "quantity",
            "amount_tax",
            "payment_method",
            "note_private",
            'note_public',
            'school_purchase_request',
            'purchase_request_vendor',
            'product_request'

        ]
        read_only_fields = ["uid", "slug"]


    def create(self, validated_data):
        products_data = validated_data.pop('product_request', None) 
        instance = super().create(validated_data=validated_data)

        if products_data: 
            for product_data in products_data:
                instance.product_request.add(product_data) 

        instance.user_created = self.context["request"].user
        instance.save(update_fields=["user_created"])
        return instance


    def update(self, instance, validated_data):
        products_data = validated_data.pop('product_request', None) 
        instance = super().update(instance, validated_data=validated_data)

        if products_data is not None: 
            instance.product_request.set(products_data)  

        instance.user_updated = self.context["request"].user
        instance.save(update_fields=["user_updated"])
        return instance