import pytest
from contacts.models import Tenant
from django.test import Client


@pytest.mark.django_db
def test_request_without_schema_header():
    client = Client()

    response = client.get("/api/contacts", content_type="application/json")

    assert response.status_code == 400
    assert response.json()["detail"] == "Missing X-SCHEMA header"


@pytest.mark.django_db
def test_cross_tenant_isolation():
    Tenant.objects.create(schema_name="contact_alpha", name="Alpha Inc")
    Tenant.objects.create(schema_name="contact_bravo", name="Bravo LLC")

    client = Client()

    resp_a = client.post(
        "/api/contacts/",
        data={"name": "Alice", "email": "alice@alpha.com", "phone": "+100"},
        content_type="application/json",
        HTTP_X_SCHEMA="alpha"
    )
    assert resp_a.status_code == 201
    id_a = resp_a.json()["id"]

    resp_b = client.post(
        "/api/contacts/",
        data={"name": "Bob", "email": "bob@bravo.com", "phone": "+200"},
        content_type="application/json",
        HTTP_X_SCHEMA="bravo"
    )
    assert resp_b.status_code == 201
    id_b = resp_b.json()["id"]

    cross_1 = client.get(f"/api/contacts/{id_a}", HTTP_X_SCHEMA="bravo")
    assert cross_1.status_code == 404

    cross_2 = client.get(f"/api/contacts/{id_b}", HTTP_X_SCHEMA="alpha")
    assert cross_2.status_code == 404


@pytest.mark.django_db
def test_email_uniqueness_per_schema():
    Tenant.objects.create(schema_name="contact_alpha", name="Alpha Inc")
    Tenant.objects.create(schema_name="contact_bravo", name="Bravo LLC")

    client = Client()

    payload = {
        "name": "User",
        "email": "duplicate@example.com",
        "phone": "+123456789"
    }

    resp_1 = client.post("/api/contacts/", data=payload, content_type="application/json", HTTP_X_SCHEMA="alpha")
    resp_2 = client.post("/api/contacts/", data=payload, content_type="application/json", HTTP_X_SCHEMA="bravo")

    assert resp_1.status_code == 201, resp_1.content
    assert resp_2.status_code == 201, resp_2.content
    assert resp_1.json()["email"] == resp_2.json()["email"]
