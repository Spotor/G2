from django.contrib import admin
from lpc_eleicao.models import *

admin.site.register(Candidato)
admin.site.register(Vaga)
admin.site.register(Eleitor)
admin.site.register(Eleicao)
admin.site.register(Token)
admin.site.register(Votar)
admin.site.register(Resultado)
