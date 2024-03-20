
from recipes.views import home
from django.urls import path


urlpatterns = [
    path ('', home)  # Adicione esta linha para a raiz #pagina inicial
]