from rest_framework import status
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


def get_notes(request):
    notes = Note.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_note_detail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


def create_note(request):
    data = request.data
    notes = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response(
        {'message': 'Note was deleted'}, status=status.HTTP_204_NO_CONTENT)
