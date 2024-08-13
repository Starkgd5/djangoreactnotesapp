from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import (create_note, delete_note, get_note_detail, get_notes,
                    update_note)


@api_view(["GET"])
def get_routes(request):

    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes"
        },
        {
            "Endpoint": "/notes/",
            "method": "POST",
            "body": "string",
            "description": "Creates new note with data sent in post request"
        },
        {
            "Endpoint": "/notes/id/",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object"
        },
        {
            "Endpoint": "/notes/id/",
            "method": "PUT",
            "body": "string",
            "description": "Creates an existing note with data sent in post request"
        },
        {
            "Endpoint": "/notes/id/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note"
        },
    ]

    return Response(routes, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def list_create_note(request):
    if request.method == "GET":
        return get_notes(request)

    if request.method == "POST":
        return create_note(request)


@api_view(["GET", "PUT", "DELETE"])
def retrieve_update_delete_note(request, pk):
    if request.method == "GET":
        return get_note_detail(request, pk)

    if request.method == "PUT":
        return update_note(request, pk)

    if request.method == "DELETE":
        return delete_note(request, pk)
