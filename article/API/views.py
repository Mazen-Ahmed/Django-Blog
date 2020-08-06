from rest_framework.generics import ListAPIView,RetrieveAPIView
from article.models  import article
from .serializers import artserializer



class listpa(ListAPIView):
    queryset = article.objects.all()
    serializer_class = artserializer

class DetailAPI(RetrieveAPIView):
    queryset = article.objects.all
    serializer_class = artserializer