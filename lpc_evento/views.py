from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from lpc_eleicao.models import *
from lpc_eleicao.serializers import *

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class VotarViewSet(viewsets.ModelViewSet):
    queryset = Votar.objects.all()
    serializer_class = VotarSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
