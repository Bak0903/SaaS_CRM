from django.db import connection
from django.http import JsonResponse
# from app.models import Tenant
from django.utils.deprecation import MiddlewareMixin


class SchemaMiddleware(MiddlewareMixin):
    def process_request(self, request):
        schema = request.headers.get("X-SCHEMA")
        if not schema:
            return JsonResponse({"detail": "Missing X-SCHEMA header"}, status=400)

        # Временно просто ставим search_path — не проверяя, существует ли схема
        schema_name = f"contact_{schema}"

        try:
            connection.set_schema(schema_name)
            request.tenant = schema_name  # можно будет заменить на объект
        except Exception:
            return JsonResponse({"detail": "TENANT_NOT_FOUND"}, status=404)
