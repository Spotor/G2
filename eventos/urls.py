from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from lpc_evento.views import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'Candidato', CandidatoViewSet)
router.register(r'Vaga', VagaViewSet)
router.register(r'Eleitor', EleitorViewSet)
router.register(r'Eleicao', EleicaoViewSet)
router.register(r'Token', TokenViewSet)
router.register(r'Votar', VotarViewSet)
router.register(r'Resultado', ResultadoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^all/',CandidatoViewSet, name='all'),
    url(r'^all/',VagaViewSet, name='all'),
    url(r'^all/',EleitorViewSet, name='all'),
    url(r'^all/',EleicaoViewSet, name='all'),
    url(r'^all/',TokenViewSet, name='all'),
    url(r'^all/',VotarViewSet, name='all'),
    url(r'^all/',ResultadoViewSet, name='all'),

]
