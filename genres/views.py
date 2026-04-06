import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': g.id, 'name': g.name} for g in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        response = {'id': new_genre.id, 'name': new_genre.name}
        return JsonResponse(response, status=201)


@csrf_exempt
def genre_detail_view(request, pk):
    if request.method == 'GET':
        # genre = Genre.objects.get(pk=pk)
        genre = get_object_or_404(Genre, pk=pk)
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
