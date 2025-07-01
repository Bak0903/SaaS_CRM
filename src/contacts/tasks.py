import logging
from datetime import timedelta
from django.utils import timezone
from django_tenants.utils import get_tenant_model, schema_context
from .models import Contact
from app.celery import app

logger = logging.getLogger(__name__)


@app.task
def find_old_contacts():
    cutoff = timezone.now() - timedelta(days=90)

    tenant_model = get_tenant_model()
    for tenant in tenant_model.objects.all():
        with schema_context(tenant.schema_name):
            old_contacts = Contact.objects.filter(date_created__lt=cutoff)
            for contact in old_contacts:
                logger.info(f"[{tenant.schema_name}] Old contact: {contact.id}")
