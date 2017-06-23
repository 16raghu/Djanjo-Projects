#from django.http import Http404
import logging
from django.shortcuts import render, get_object_or_404
from . models import  Album,Song


logger = logging.getLogger(__name__)
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}

    return render(request,'music/index.html',context)


def detail(request, album_id):
    album = get_object_or_404(Album,pk=album_id)

    # try:
    #   album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #   raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})

def fav(request, album_id):

    album = get_object_or_404(Album, pk=album_id)
    print(album)
    try:
        print("ho");
        print("ho:"+request.POST['song'])
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': 'You did not select a valid song',
        })
    else:
        selected_song.is_fav = True
        print(selected_song)
        print(selected_song.is_fav)
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

































