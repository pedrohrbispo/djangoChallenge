from django.contrib import admin
from django.urls import path, include
from articles.views import ArticlesViewSet, AuthorsViewSet, ArticleAuthor, UsuariosViewSet, ListaUsuarios
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/articles', ArticlesViewSet, basename='Articles')
router.register('api/authors', AuthorsViewSet, basename='Authors')
router.register('api/sign-up', UsuariosViewSet, basename='Sign-up')

urlpatterns = [
    path('', include(router.urls) ),
    path('api/admin/', admin.site.urls),
    path('api/articles/<int:pk>/author', ArticleAuthor.as_view()),
    path('api/sign-up', ListaUsuarios.as_view()),
]
