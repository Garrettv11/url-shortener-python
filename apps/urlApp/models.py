from django.db import models

# Create your models here.
MAX_URL_SIZE = 2000

class ShortURL(models.Model):

    
    full_url = models.URLField(max_length=MAX_URL_SIZE)
    short_path_component = models.CharField(max_length=8)

    @property
    def short_url(self):
        path = "/urls/r/{}".format(self.short_path_component)
        return path

    class Meta:
        pass
        indexes = [
            models.Index(fields=["short_path_component"])
        ]