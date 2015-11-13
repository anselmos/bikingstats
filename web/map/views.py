from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Coordinate

def index(request):
    list_coords = Coordinate.objects.all()
    import logging
    logging.error(list_coords)
    template = loader.get_template('map/index.html')
    context = RequestContext(request, {
        'coords': [[11.22, 22.11], [11.55, 22.55]],
        'list': list_coords,
    })
    return HttpResponse(template.render(context))
