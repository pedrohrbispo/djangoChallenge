from rest_framework import viewsets, generics
from .import models
from . import serializer

class ArticlesViewSet(viewsets.ModelViewSet):
    """Crud Articles"""
    queryset = models.Articles.objects.all()
    serializer_class = serializer.ArticleSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    """Crud Authors"""
    queryset = models.Authors.objects.all()
    serializer_class = serializer.AuthorSerializer

class ArticleAuthor(generics.ListAPIView):
    """Get article's author"""
    def get_queryset(self):
        queryset = models.Authors.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = serializer.ArticleAuthorSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializer.RegistrationSerializer

class ListaUsuarios(generics.ListAPIView):
    def get_queryset(self):
        queryset = models.Usuario.objects.all()
        return queryset
    serializer_class = serializer.RegistrationSerializer