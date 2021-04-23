from rest_framework import serializers
from django.db import transaction
from urlApp.models import ShortURL

CHARACTER_SPACE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(CHARACTER_SPACE)



class ShortUrlManagerSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ShortURL
        fields = ["id", "full_url", "short_path_component", "short_url"]
        read_only_fields = ("id", "short_path_component", "short_url")
    
    
    def encode(self, id: int) -> str:
        short_resource = []
        while id > 0:
            character_index = id % BASE
            short_resource.append(CHARACTER_SPACE[character_index])
            id //= BASE
        return "".join(short_resource[::-1])

    
    @transaction.atomic
    def save(self, **kwargs):
        res = super().save(**kwargs)
        short_path_component = self.encode(res.id)
        self.validated_data["short_path_component"] = short_path_component
        return super().save(**kwargs)


