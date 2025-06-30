from django.db import connection
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class SchemaMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        schema = request.headers.get("X-SCHEMA")
        if not schema:
            return JsonResponse({"detail": "Missing X-SCHEMA header"}, status=400)

        schema_name = f"contact_{schema}"
        try:
            connection.set_schema(schema_name)
            request.tenant_schema = schema_name
        except Exception:
            return JsonResponse({"detail": "TENANT_NOT_FOUND"}, status=404)

    @staticmethod
    def process_response(request, response):
        connection.set_schema_to_public()
        return response
