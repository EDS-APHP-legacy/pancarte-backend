from django.http import JsonResponse
from rest_framework import status


def already_exists():
    return JsonResponse({'error': 'Object already exists (409)'}, status=status.HTTP_409_CONFLICT)


def does_not_exists():
    return JsonResponse({'error': 'Object does not exists (404)'}, status=status.HTTP_404_NOT_FOUND)
