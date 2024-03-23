import uuid

from django.db import transaction

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from core.models import Blog, BlogImage, BlogTag, BlogCategory

from common.rest.serializers.schoolInformation import (
    SchoolInformationOnBoardingListSerializer,
)
from common.models import SchoolInformationOnBoarding


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ("blog_info", "slug", "image")


class BlogTagSerializer(ModelSerializer):
    school_blog_tag = SchoolInformationOnBoardingListSerializer(read_only=True)

    class Meta:
        model = BlogTag
        fields = [
            "uid",
            "name",
            "school_blog_tag",
        ]


class BlogCategorySerializer(ModelSerializer):
    school_blog_category = SchoolInformationOnBoardingListSerializer(read_only=True)

    class Meta:
        model = BlogCategory
        fields = [
            "uid",
            "name",
            "school_blog_category",
        ]


class BlogTagPostSerializer(ModelSerializer):
    school_blog_tag = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = BlogTag
        fields = [
            "id",
            "uid",
            "name",
            "school_blog_tag",
        ]


class BlogCategoryPostSerializer(ModelSerializer):
    school_blog_category = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )

    class Meta:
        model = BlogCategory
        fields = [
            "uid",
            "name",
            "school_blog_category",
        ]


class BlogListDetailSerializer(ModelSerializer):
    school_blog = SchoolInformationOnBoardingListSerializer(read_only=True)
    tags = BlogTagSerializer(read_only=True, many=True)
    categories = BlogCategorySerializer(read_only=True, many=True)
    blog_image_information = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            "uid",
            "slug",
            "school_blog",
            "title",
            "content",
            "publish_date",
            "categories",
            "tags",
            "blog_image_information",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    school_blog = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    blog_image_information = serializers.ImageField(required=False)
    tags = serializers.CharField(allow_blank=True, required=False)
    categories = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Blog
        fields = [
            "uid",
            "slug",
            "title",
            "school_blog",
            "content",
            "publish_date",
            "categories",
            "tags",
            "blog_image_information",
        ]

    @transaction.atomic
    def create(self, validated_data):
        tags_data = validated_data.pop("tags", "")
        categories_data = validated_data.pop("categories", "")
        images_data = validated_data.pop("blog_image_information", None)

        blog = Blog.objects.create(**validated_data)

        if tags_data:
            tag_uuids = [
                uuid.UUID(tag.strip()) for tag in tags_data.split(",") if tag.strip()
            ]
            tags = BlogTag.objects.filter(uid__in=tag_uuids)
            blog.tags.set(tags)

        if categories_data:
            category_uuids = [
                uuid.UUID(category.strip())
                for category in categories_data.split(",")
                if category.strip()
            ]
            categories = BlogCategory.objects.filter(uid__in=category_uuids)
            blog.categories.set(categories)

        if images_data:
            BlogImage.objects.create(blog_info=blog, image=images_data)

        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags", "")
        categories_data = validated_data.pop("categories", "")
        images_data = validated_data.pop("blog_image_information", None)

        blog = super().update(instance, validated_data)

        if tags_data:
            tag_uuids = [
                uuid.UUID(tag.strip()) for tag in tags_data.split(",") if tag.strip()
            ]
            tags = BlogTag.objects.filter(uid__in=tag_uuids)
            blog.tags.set(tags)
        else:
            blog.tags.set([])

        if categories_data:
            category_uuids = [
                uuid.UUID(category.strip())
                for category in categories_data.split(",")
                if category.strip()
            ]
            categories = BlogCategory.objects.filter(uid__in=category_uuids)
            blog.categories.set(categories)
        else:
            blog.categories.set([])

        if images_data:
            BlogImage.objects.create(blog_info=blog, image=images_data)

        return blog
