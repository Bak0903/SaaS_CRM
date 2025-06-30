from django_tenants.models import TenantMixin
from django.db import models

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    auto_create_schema = True
