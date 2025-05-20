from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('area_saber/', AreasSaberView.as_view(), name='area_saber'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('periodo/', PeriodosView.as_view(), name='periodo'),
    path('curso_disciplina/', CursoDisciplinasView.as_view(), name='curso_disciplina'),
    path('turno/', TurnosView.as_view(), name='turno'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('avaliacao_tipo/', AvaliacaoTiposView.as_view(), name='avaliacao_tipo'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
]
