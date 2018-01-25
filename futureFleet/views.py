from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Comic, Blog


"""
def index(request):
    latest_comic = Comic.objects.order_by('-comic_pub_date')[:1]
    template = loader.get_template('futureFleet/index.html')
    context = {
        'latest_comic': latest_comic,
    }
    return HttpResponse(template.render(context, request))
"""



def index(request):
    ####Controls
    newest_comic = Comic.objects.last()
    first_comic = 1
    #####
    current_comic = Comic.objects.order_by('-comic_pub_date').first()
    if current_comic.id == first_comic:
        previous_comic = 1
        next_comic = current_comic.id + 1
    elif current_comic.id == newest_comic.id:
        previous_comic = current_comic.id - 1
        next_comic = newest_comic.id
    else:
        previous_comic = current_comic.id - 1
        next_comic = current_comic.id + 1
    context = {'current_comic': current_comic, 'previous_comic': previous_comic, 'next_comic': next_comic}
    return render(request, 'futureFleet/index.html', context)


def comic(request, comic_id):
#    return HttpResponse("You are looking at comic %s" % comic_id)  # this might be wrong
    ####Controls
    newest_comic = Comic.objects.last()
    first_comic = 1

    #latest_comic = Comic.objects.all().filter(id=comic_id)
    current_comic = Comic.objects.get(id=comic_id)

    if current_comic.id == first_comic:
        previous_comic = 1
        next_comic = current_comic.id + 1
    elif current_comic.id == newest_comic.id:
        previous_comic = current_comic.id - 1
        next_comic = newest_comic.id
    else: #current_comic.id != first_comic or newest_comic.id:
        previous_comic = current_comic.id - 1
        next_comic = current_comic.id + 1
    context = {'current_comic': current_comic, 'previous_comic': previous_comic, 'next_comic': next_comic}
    return render(request, 'futureFleet/index.html', context)


def test(request):
    return HttpResponse("This is a test.  Only a Test")


def blog(request, blog_id):
    return HttpResponse("You are looking at blog %s" % blog_id)  # this might be wrong


"""Variables are surrounded by {{ and }} like this:

My first name is {{ first_name }}. My last name is {{ last_name }}.

With a context of {'first_name': 'John', 'last_name': 'Doe'}, this template renders to:"""