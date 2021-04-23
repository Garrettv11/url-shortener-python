"""
View definitions for the urlApp
"""
from django.http.response import Http404
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from apps.urlApp.models import ShortURL
from apps.urlApp.serializers import ShortUrlManagerSerializer

# Create your views here.

@api_view(["GET"])
def resolve_url(request, short_path_component: str):
    """Takes the short path component and resolves it to the original URL

    Args:
        request (HttpRequest): Django request context
        short_path_component (str): shortened url path component

    Raises:
        Http404: raises a 404 if the short url is not found

    Returns:
        HttpResponseRedirect: returns a redirect response to the original URL
    """
    try:
        short_url = ShortURL.objects.get(short_path_component=short_path_component)
        serializer = ShortUrlManagerSerializer(short_url, many=False)
        return HttpResponseRedirect(serializer.data["full_url"])
    except ShortURL.DoesNotExist:
        raise Http404


class ShortURLManagerViewSet(ModelViewSet):
    """ModelViewSet for the ShortURL model
    """
    queryset = ShortURL.objects.all()
    serializer_class = ShortUrlManagerSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
