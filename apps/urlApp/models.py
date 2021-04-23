"""model declarations for url app"""
from django.db import models

# Create your models here.
MAX_URL_SIZE = 2000

class ShortURL(models.Model):
    """django model representing a ShortURL"""

    full_url = models.URLField(max_length=MAX_URL_SIZE)
    short_path_component = models.CharField(max_length=8)

    @property
    def short_url(self):
        """dynamic property added as a convenience to display the relative resolver url

        Returns:
            str: The relative path of the resolvable url. EX: http://localhost:8000/{short_url}/
        """
        path = "/urls/r/{}".format(self.short_path_component)
        return path

    class Meta:
        """model meta defining fields to index"""
        indexes = [
            models.Index(fields=["short_path_component"])
        ]
