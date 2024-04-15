from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
path('admin/', admin.site.urls),
path('', IndexView.as_view(), name='index'),
path('cidade/', CidadesView.as_view(), name='cidade'),
path('pessoa/', PessoasView.as_view(), name='pessoa'),
path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
path('instituicao/', InstitucaoView.as_view(), name='institucao'),
path('area_do_saber/', AreaView.as_view(), name='area_do_saber'),
path('curso/', CursosView.as_view(), name='curso'),
path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
path('matricula/', MatriculaView.as_view(), name='matricula'),
path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
path('turma/', TurmasView.as_view(), name='turma'),
path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
path('periodo/', PeriodosView.as_view(), name='periodo'),
path('Manter_avalicao/', Manter_avalicaoView.as_view(), name='Manter_avalicao'),
path('disciplinacurso/',  Disciplina_Por_CursoView.as_view(), name='disciplinacurso'),
]
