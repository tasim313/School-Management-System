from rest_framework.response import Response

from core.models import Blog, BlogTag, BlogImage, BlogCategory
from core.rest.serializers.blog import (
    BlogListDetailSerializer,
    BlogPostSerializer,
    BlogTagSerializer,
    BlogTagPostSerializer,
    BlogCategorySerializer,
    BlogCategoryPostSerializer,
)

from common.custom_views import (
    CustomListCreateAPIView,
    CustomRetrieveUpdateDestroyAPIView,
)


class BlogListCreateAPIView(CustomListCreateAPIView):
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogListDetailSerializer
        else:
            return BlogPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = BlogListDetailSerializer(queryset, many=True)
        return Response(serializer.data)


class BlogRetrieveUpdateDestroyAPIView(CustomRetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BlogListDetailSerializer
        else:
            return BlogPostSerializer


class BlogTagListCreateView(CustomListCreateAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

    def get_serializer_class(self):
        if self.request.method != "POST":
            return super().get_serializer_class()
        else:
            return BlogTagPostSerializer


class BlogTagRetrieveUpdateView(CustomRetrieveUpdateDestroyAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method != "POST":
            return super().get_serializer_class()
        else:
            return BlogTagPostSerializer


class BlogCategoryListCreateView(CustomListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    def get_serializer_class(self):
        if self.request.method != "POST":
            return super().get_serializer_class()
        else:
            return BlogCategoryPostSerializer


class BlogCategoryRetrieveUpdateView(CustomRetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method != "POST":
            return super().get_serializer_class()
        else:
            return BlogCategoryPostSerializer
