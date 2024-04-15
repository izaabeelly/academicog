from django.shortcuts import render
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class PessoasView(View):
    def get(self, request):
        pessoa = Pessoas.objects.all()
        return render(request, 'pessoa.html', {'pessoa':pessoa})    
    
class OcupacaoView(View):
    def get(self, request):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao}) 
    
class CidadesView(View):
    def get(self, request):
        cidade = Cidades.objects.all()
        return render(request, 'cidade.html', {'cidade':cidade}) 
    
class InstitucaoView(View):
    def get(self, request):
        institucao = Institucao.objects.all()
        return render(request, 'instituicao.html', {'instituicao':institucao}) 
    
class AreaView(View):
    def get(self, request):
        area = Area.objects.all()
        return render(request, 'area_do_saber.html', {'area_do_saber':area}) 
    
class CursosView(View):
    def get(self, request):
        curso = Cursos.objects.all()
        return render(request, 'curso.html', {'curso':curso}) 
    
class  DisciplinasView(View):
    def get(self, request):
        disciplina =  Disciplinas.objects.all()
        return render(request, 'disciplina.html', {'disciplina': disciplina}) 
    
class  PeriodosView(View):
    def get(self, request):
        periodo =  Periodos.objects.all()
        return render(request, 'periodo.html', {'periodo': periodo}) 
    
class  MatriculaView(View):
    def get(self, request):
        matricula =  Matricula.objects.all()
        return render(request, 'matricula.html', {'matricula': matricula}) 

class  AvaliacoesView(View):
    def get(self, request):
        avaliacao =  Avaliacoes.objects.all()
        return render(request, 'avaliacao.html', {'avaliacao': avaliacao}) 
    
class  FrequenciaView(View):
    def get(self, request):
        frequencia =  Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencia': frequencia}) 

class  TurmasView(View):
    def get(self, request):
        turma =  Turmas.objects.all()
        return render(request, 'turma.html', {'turma': turma}) 
    
class  OcorrenciaView(View):
    def get(self, request):
        ocorrencia =  Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencia': ocorrencia}) 
    
class  Manter_avalicaoView(View):
    def get(self, request):
        manter_avalicao=  Manter_avalicao.objects.all()
        return render(request, 'manter_avalicao.html', {'manter_avalicao': manter_avalicao}) 
    
class  Disciplina_Por_CursoView(View):
    def get(self, request):
        disciplinacurso=   Disciplina_Por_Curso.objects.all()
        return render(request, 'disciplinacurso.html', {'disciplinacurso': disciplinacurso}) 