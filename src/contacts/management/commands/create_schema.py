from django.core.management.base import BaseCommand
from contacts.models import Tenant


class Command(BaseCommand):
    help = "Create new tenant schema"

    def add_arguments(self, parser):
        parser.add_argument("schema", type=str, help="Schema name (e.g. acme)")
        parser.add_argument("name", type=str, help="Tenant name")

    def handle(self, *args, **options):
        schema = f"contact_{options['schema']}"
        name = options["name"]

        if Tenant.objects.filter(schema_name=schema).exists():
            self.stdout.write(self.style.WARNING("Tenant already exists"))
            return

        tenant = Tenant(schema_name=schema, name=name)
        tenant.save()
        self.stdout.write(self.style.SUCCESS(f"Tenant created: {name} ({schema})"))
