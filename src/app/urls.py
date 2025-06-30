from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from contacts.api import router as contacts_router

api = NinjaAPI()

api.add_router("contacts", contacts_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
