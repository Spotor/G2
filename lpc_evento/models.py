from django.db import models
from django.contrib.auth.models import User

class Candidato(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    nome = models.CharField(max_length=128)
    cargaHoraria = models.CharField(max_length=20)
    candidato =  models.ForeignKey(Candidato, null=True, blank=False)

    def __str__(self):
        return self.nome

class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=20)
    Votou = models.BooleanField('Sim')

    def __str__(self):
        return self.nome

class Eleicao(models.Model):
    nome = models.CharField(max_length=128)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    vagas models.ForeignKey(Vagas, null=True, blank=False)
    eleitor = models.ForeignKey(Eleitor, null=True, blank=False)

class Token(models.Model):
    cod = models.CharField(max_length=20)
    eleitor = models.ForeignKey(Eleitor, null=True, blank=False)

    def __str__(self):
        return self.cod

class Votar(models.Model):
    token models.ForeignKey(Token, null=True, blank=False)

    voto = (
        (1, "Em branco"),
        (2, "Em candidato"),
    )
    votou = models.CharField(max_length=1, choices=voto)

    def __str__(self):
        return self.votou

class Resultado(models.Model):
    resultado = models.ForeignKey(Votar, null=True, blank=False)

    def __str__(self):
        return self.Resultado
