from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_routes, name="get-routes"),
    path("notes/", views.list_create_note, name="get-create-notes"),
    path("notes/<str:pk>/", views.retrieve_update_delete_note,
         name="retrieve-update-delete-note"),
]
