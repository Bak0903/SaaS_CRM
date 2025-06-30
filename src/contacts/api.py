from ninja import Router, Schema
from typing import List, Optional
from uuid import UUID
from django.shortcuts import get_object_or_404
from contacts.models import Contact
from datetime import datetime

router = Router()


class ContactIn(Schema):
    name: str
    email: str
    phone: Optional[str] = None


class ContactOut(ContactIn):
    id: UUID
    date_created: datetime


@router.post("/", response={201: ContactOut})
def create_contact(request, data: ContactIn):
    contact = Contact.objects.create(**data.dict())
    return 201, contact


@router.get("/", response=List[ContactOut])
def list_contacts(request, email: Optional[str] = None):
    qs = Contact.objects.all()
    if email:
        qs = qs.filter(email=email)
    return qs


@router.get("/{contact_id}", response=ContactOut)
def get_contact(request, contact_id: UUID):
    contact = get_object_or_404(Contact, id=contact_id)
    return contact


@router.put("/{contact_id}", response=ContactOut)
def update_contact(request, contact_id: UUID, data: ContactIn):
    contact = get_object_or_404(Contact, id=contact_id)
    for attr, value in data.dict().items():
        setattr(contact, attr, value)
    contact.save()
    return contact


@router.delete("/{contact_id}", response={204: None})
def delete_contact(request, contact_id: UUID):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return 204, None
