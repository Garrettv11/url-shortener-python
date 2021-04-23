"""Serializer definitions for ShortURL CRUD operations
"""
from rest_framework import serializers
from django.db import transaction
from apps.urlApp.models import ShortURL

CHARACTER_SPACE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(CHARACTER_SPACE)

def encode(shorturl_id: int) -> str:
    """Converts the auto incremented id of a ShortURL object and turns it into a shorturl hash

    Args:
        id (int): Takes in the auto incremented id of a ShortURL and generates a hash

    Returns:
        str: the short url hash
    """
    short_resource = []
    while shorturl_id > 0:
        character_index = shorturl_id % BASE
        short_resource.append(CHARACTER_SPACE[character_index])
        shorturl_id //= BASE
    return "".join(short_resource[::-1])

class ShortUrlManagerSerializer(serializers.ModelSerializer):
    """Model serializer for the ShortURL model
    """

    class Meta:
        """
        Class meta for ShortUrlManagerSerializer
        """
        model = ShortURL
        fields = ["id", "full_url", "short_path_component", "short_url"]
        read_only_fields = ("id", "short_path_component", "short_url")

    @transaction.atomic
    def save(self, **kwargs):
        """
        Overrides the save to initially save to get the id
        then computes the shorturl hash and saves it to the model
        within a transaction context
        """
        res = super().save(**kwargs)
        short_path_component = encode(res.id)
        self.validated_data["short_path_component"] = short_path_component
        return super().save(**kwargs)
