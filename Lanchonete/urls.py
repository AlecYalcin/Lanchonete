
from django.contrib import admin
from django.urls    import path
from Cardapio       import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cardapio/', views.index),
]