import uuid

from django_tenants.models import TenantMixin
from django.db import models


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    auto_create_schema = True

    class Meta:
        tenant_model = False


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"
