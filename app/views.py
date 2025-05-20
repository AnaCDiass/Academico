from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class InstituicoesView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})

class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'areas': areas})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class PeriodosView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all()
        return render(request, 'periodo.html', {'periodos': periodos})

class CursoDisciplinasView(View):
    def get(self, request, *args, **kwargs):
        curso_disciplinas = CursoDisciplina.objects.all()
        return render(request, 'curso_disciplina.html', {'curso_disciplinas': curso_disciplinas})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacaoTiposView(View):
    def get(self, request, *args, **kwargs):
        tipos = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacao_tipo.html', {'tipos': tipos})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})

class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})

class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})
