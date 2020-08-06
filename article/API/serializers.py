from rest_framework import  serializers
from article.models import article


class artserializer(serializers.ModelSerializer):
    class Meta:
        model=article
        fields=[
            'title',
            'body',
            'pic',

        ]

