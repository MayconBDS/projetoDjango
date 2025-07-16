from django.contrib import admin
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('app02.urls')),
    path('produtos/', include('cadastroP.urls')),
    path('cadastro/', include('cadastroUser.urls')),
]
