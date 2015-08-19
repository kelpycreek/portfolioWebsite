from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Drawing
# Create your views here.

def index(request):
    allDrawings = Drawing.objects.order_by('date')
    template = loader.get_template('home/gallery.html')
    context = RequestContext(request, {
        'allDrawings' : allDrawings
        })

    return HttpResponse(template.render(context))

def closeUp(request, pictureName):
    try: #could also use get_object_or_404
        drawing = Drawing.objects.get(name=pictureName)
    except Drawing.DoesNotExist:
        raise Http404("Sorry, we couldnt find the art you were looking for")
    context = {'drawing' : drawing}
    return render(request, 'home/picture.html', context)
