from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework import filters


from ...models import SchoolInformationOnBoarding

from ..serializers import schoolInformation


class SchoolInformationOnBoardingCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = SchoolInformationOnBoarding.objects.all()
    serializer_class =  schoolInformation.SchoolInformationOnBoardingCreateSerializer


    def post(self, request, format=None, **kwargs):
        serializer = schoolInformation.SchoolInformationOnBoardingCreateSerializer(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class SchoolInformationOnBoardingList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SchoolInformationOnBoarding.objects.all()
    serializer_class = schoolInformation.SchoolInformationOnBoardingListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields =  ['name', 'phone', 'school_type']

    def get_queryset(self):
        return SchoolInformationOnBoarding.objects.all()


class SchoolInformationOnBoardingRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = SchoolInformationOnBoarding.objects.all()
    serializer_class = schoolInformation.SchoolInformationOnBoardingUpdateSerializer
    lookup_field = 'uid'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        lookup_value = self.kwargs[self.lookup_field]
        queryset = self.filter_queryset(self.get_queryset())
        obj = generics.get_object_or_404(queryset, **{self.lookup_field: lookup_value})
        self.check_object_permissions(self.request, obj)
        return obj