from django.contrib import admin
from django.urls    import path
from Cardapio       import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('CreateProduto/', views.createProduto, name="createProduto"),
    path('UpdateProduto/<int:id_produto>', views.updateProduto, name="updateProduto"),
    path('DeleteProduto/<int:id_produto>', views.deleteProduto, name="deleteProduto")
]