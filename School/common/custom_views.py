from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response


from core.choice import Status


class CustomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Custom view for retrieving, updating, and deleting an object.
    """

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request.

        This method is responsible for deleting the object.
        If the instance's status is to be set as 'Inactive', it updates the status.
        Otherwise, it performs the regular deletion.
        """

        # Get the object instance
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "successfully!"}, status=status.HTTP_204_NO_CONTENT
        )

        # try:
        #     # Attempt to update the status to 'Inactive'
        #     instance.status = Status.Inactive
        #     instance.save()  # Save the changes to the instance
        #     return Response(
        #         {"message": "Successful!"}, status=status.HTTP_204_NO_CONTENT
        #     )  # Return success response for 'Inactive' update
        # except Exception as e:
        #     # If there's an exception (e.g., status field not available or saving fails), perform regular deletion
        #     self.perform_destroy(instance)
        #     return Response(
        #         {"message": "Successful!"}, status=status.HTTP_204_NO_CONTENT
        #     )

    def update(self, request, *args, **kwargs):
        """
        Handle PUT request for updating the object.
        """

        # Call the parent class method to perform the update
        super().update(request, *args, **kwargs)

        # Get the updated instance
        updated_instance = self.get_object()

        # Serialize the updated instance
        serialized_data = self.get_serializer(updated_instance).data

        # Return a response with success message and serialized data
        return Response(
            {"message": "Successful!", "data": serialized_data},
            status=status.HTTP_200_OK,
        )


class CustomListCreateAPIView(ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "successful!", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
