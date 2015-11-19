from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import logging
logger = logging.getLogger(__name__)

from .models import Coordinate

class entryExit(object):

    def __init__(self, f):
        self.__f = f

    def __call__(self, *args, **kwgs):
        logger.info("Entering %s"%( self.__f.__name__))
        return self.__f(*args, **kwgs)


@entryExit
def index(request):
    import traceback
    logger.debug(traceback.extract_stack(None, 2)[0][2])
    logger.debug("index")
    list_coords = Coordinate.objects.all()
    logger.warning("warn_index")
    logger.error(list_coords)
    template = loader.get_template('map/index.html')
    context = RequestContext(request, {
        'coords': [[11.22, 22.11], [11.55, 22.55]],
        'list': list_coords,
    })
    return HttpResponse(template.render(context))
