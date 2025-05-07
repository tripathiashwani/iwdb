from rest_framework.viewsets import ModelViewSet
from .models import WebsiteInfo
from .serializers import WebsiteInfoSerializer

class ItemListCreateView(ModelViewSet):
    queryset = WebsiteInfo.objects.all()
    serializer_class = WebsiteInfoSerializer