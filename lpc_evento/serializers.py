from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from lpc_eleicao.models import *

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

    def create(self, dados):
        return Candidato.objects.create(**dados)

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    candidato = CandidatoSerializer(many = False)
    class Meta:
        model = Vaga
        fields = '__all__'

    def create(self, dados):
        candidato_data = validated_data.pop('candidato')
        c = Candidato.objects.create(**candidato_data)
        ca = Vaga.objects.create(candidato = c, **validated_data)
        return ca

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleitor
        fields = '__all__'

    def create(self, dados):
        return Eleitor.objects.create(**dados)

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    eleitor = EleitorSerializer(many = False)
    class Meta:
        model = Eleicao
        fields = '__all__'

    def create(self, dados):
        eleitor_data = validated_data.pop('eleitor')
        e = Eleitor.objects.create(**eleitor_data)
        el = Eleicao.objects.create(eleicao = e, **validated_data)
        return el

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    eleitor = EleitorSerializer(many = False)
    class Meta:
        model = Token
        fields = '__all__'

    def create(self, dados):
        eleitor_data = validated_data.pop('eleitor')
        t = Eleitor.objects.create(**eleitor_data)
        to = Token.objects.create(eleitor = t, **validated_data)
        return to

class VotarSerializer(serializers.HyperlinkedModelSerializer):
    token = TokenSerializer(many = False)
    class Meta:
        model = Votar
        fields = '__all__'

    def create(self, dados):
        token_data = validated_data.pop('token')
        v = Token.objects.create(**token_data)
        vo = Votar.objects.create(token = v, **validated_data)
        return vo

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    votar = VotarSerializer(many = False)
    class Meta:
        model = Resultado
        fields = '__all__'

    def create(self, dados):
        votar_data = validated_data.pop('votar')
        r = Votar.objects.greate(**votar_data)
        re = Resultado.objects.create(votar = r, **validated_data)
        return re
