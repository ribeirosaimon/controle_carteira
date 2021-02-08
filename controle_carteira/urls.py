from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from compras.views import CompraViewSet
from vendas.views import VendaViewSet
from core.views import AcaoModelViewSet
from core.view.patrimonioviewset import PatrimonioViewSet
from core.view.acaoviewset import AcaoViewSet
from core.view.relatorioviewset import RelatorioViewSet
from controle_variacoes.views import RelatorioCompletoViewSet
from controle_variacoes.models import RelatorioCompletoModel

router = routers.DefaultRouter()
router.register('compra', CompraViewSet) #Essa vai ser a URL pra fazer a Compra
router.register('venda',VendaViewSet)    #Essa vai ser a URL pra fazer a Venda
router.register('carteira', AcaoViewSet, basename='AcaoModel')
router.register('impostoderenda', RelatorioViewSet, basename='AcaoModel')
router.register('patrimonio',PatrimonioViewSet, basename='AcaoModel')
router.register('relatoriocompleto',RelatorioCompletoViewSet, basename='RelatorioCompletoModel')
router.register('acaoviewset',AcaoModelViewSet, basename='AcaoModel')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
