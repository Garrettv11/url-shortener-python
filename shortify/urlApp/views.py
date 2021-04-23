from django.http.response import Http404
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from urlApp.models import ShortURL
from urlApp.models import ShortURL
from urlApp.serializers import ShortUrlManagerSerializer

# Create your views here.

@api_view(["GET"])
def resolve_url(request, short_path_component):
    try:
        short_url = ShortURL.objects.get(short_path_component=short_path_component)
        serializer = ShortUrlManagerSerializer(short_url, many=False)
        return HttpResponseRedirect(serializer.data["full_url"])
    except ShortURL.DoesNotExist:
        raise Http404


class ShortURLManagerViewSet(ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortUrlManagerSerializer
    http_method_names = ['get', 'post', 'delete', 'head']

