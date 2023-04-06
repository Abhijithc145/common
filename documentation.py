from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from activities.models import *


# Swagger documentation for form fields creation :
activity_api_documentation = swagger_auto_schema(
    operation_description="Form Fields Create/Update API",
    responses={400: "Bad Request", 200: "Success"},
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "source_id": openapi.Schema(type=openapi.TYPE_STRING),
            "source_type": openapi.Schema(type=openapi.TYPE_STRING),
            "name": openapi.Schema(type=openapi.TYPE_STRING),
            "description": openapi.Schema(type=openapi.TYPE_STRING),
            "type": openapi.Schema(type=openapi.TYPE_STRING),
            "due_date": openapi.Schema(type=openapi.TYPE_STRING),
            "outcome": openapi.Schema(type=openapi.TYPE_STRING),
            "comment": openapi.Schema(type=openapi.TYPE_STRING),
            "participants": openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_STRING,
                ),
            ),
        },
    ),
)
