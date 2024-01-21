"""Serializers for Library Model"""

from rest_framework import serializers

from SchoolAdminApp.models import Library


class LibraryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            "uid",
            "slug",
            "school_library",
            "library_department",
            "library_class",
            "book_id",
            "book_name",
            "language",
            "book_type",
            "book_status",
        ]
        read_only_fields = ["uid", "slug"]
