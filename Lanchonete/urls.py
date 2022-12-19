from django.contrib import admin
from django.urls    import path
from Cardapio       import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('buscaCardapio/', views.buscaProduto, name="buscaCardapio"),
    path('buscaChefe/', views.buscaChefe, name="buscaChefe"),
    # Path de PRODUTOS
    path('CreateProduto/', views.createProduto, name="createProduto"),
    path('UpdateProduto/<int:id_produto>', views.updateProduto, name="updateProduto"),
    path('DeleteProduto/<int:id_produto>', views.deleteProduto, name="deleteProduto"),
    # Path de CHEFE
    path('CreateChefe/', views.createChefe, name="createChefe"),
    path('UpdateChefe/<int:id_chefe>', views.updateChefe, name="updateChefe"),
    path('DeleteChefe/<int:id_chefe>', views.deleteChefe, name="deleteChefe"),
]