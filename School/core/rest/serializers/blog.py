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
        fields = ("id", "blog_info", "slug", "image")


class BlogListDetailSerializer(ModelSerializer):
    school_blog = SchoolInformationOnBoardingListSerializer(read_only=True)
    blog_image_information = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "uid",
            "slug",
            "school_blog",
            "content",
            "publish_date",
            "categories",
            "tags",
            "blog_image_information",
        ]


class BlogPostSerializer(ModelSerializer):
    school_blog = serializers.SlugRelatedField(
        queryset=SchoolInformationOnBoarding.objects.all(),
        slug_field="uid",
    )
    blog_image_information = serializers.ImageField(required=False)

    class Meta:
        model = Blog
        fields = [
            "id",
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

    def create(self, validated_data):
        categories_data = validated_data.pop("categories", None)
        tags = validated_data.pop("tags", None)
        images_data = validated_data.pop("blog_image_information", None)

        blog = Blog.objects.create(**validated_data)

        if categories_data:
            blog.categories.set(categories_data)

        if tags:
            blog.categories.set(tags)

        if images_data:
            BlogImage.objects.create(blog_info=blog, image=images_data)

        return blog

    def update(self, instance, validated_data):
        self.validated_data.pop("blog_image_information", None)
        return super().update(instance, validated_data)


class BlogTagSerializer(ModelSerializer):
    school_blog_tag = SchoolInformationOnBoardingListSerializer(read_only=True)

    class Meta:
        model = BlogTag
        fields = [
            "id",
            "uid",
            "name",
            "school_blog_tag",
        ]


class BlogCategorySerializer(ModelSerializer):
    school_blog_category = SchoolInformationOnBoardingListSerializer(read_only=True)

    class Meta:
        model = BlogCategory
        fields = [
            "id",
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
            "id",
            "uid",
            "name",
            "school_blog_category",
        ]
