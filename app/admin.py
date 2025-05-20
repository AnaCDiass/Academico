from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, AreaSaber, Curso, Turma, 
    Disciplina, Periodo, CursoDisciplina, Turno, Matricula, AvaliacaoTipo, 
    Avaliacao, Frequencia, Ocorrencia
)

admin.site.register([
    Cidade,
    Ocupacao,
    Pessoa,
    InstituicaoEnsino,
    AreaSaber,
    Curso,
    Turma,
    Disciplina,
    Periodo,
    CursoDisciplina,
    Turno,
    Matricula,
    AvaliacaoTipo,
    Avaliacao,
    Frequencia,
    Ocorrencia,
])
