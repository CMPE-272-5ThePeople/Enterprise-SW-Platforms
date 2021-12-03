from rest_framework import viewsets, parsers
from .models import Document
from .serializers import DocumentSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
