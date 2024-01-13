from rest_framework import serializers

from ...models import User

from ...choice import UserRole, UserStatus

from common.rest.serializers import schoolInformation


class UserSerializer(serializers.ModelSerializer):
    school = schoolInformation.SchoolInformationOnBoardingListSerializer(
        many=False, read_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "role",
            "is_active",
            "user_status",
            "firstName",
            "lastName",
            "school",
        ]
