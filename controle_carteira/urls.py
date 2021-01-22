from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from compras.views import CompraViewSet
from vendas.views import VendaViewSet
from core.views import AcaoViewSet

router = routers.DefaultRouter()
router.register('compra', CompraViewSet) #Essa vai ser a URL pra fazer a Compra
router.register('venda',VendaViewSet)    #Essa vai ser a URL pra fazer a Venda
router.register('carteira', AcaoViewSet, basename='AcaoModel')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
