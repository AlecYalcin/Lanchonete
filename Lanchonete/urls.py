
from django.contrib import admin
from django.urls    import path
from Cardapio       import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CreateCardapio/', views.index, name="cardapio"),
    path('UpdateCardapio/<int:id_produto>', views.update, name="update"),
    path('DeleteCardapio/<int:id_produto>', views.delete, name="delete"),
]