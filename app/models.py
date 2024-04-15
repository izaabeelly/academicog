from django.db import models

class Ocupacao(models.Model):
   
    nome = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Ocupação"
    
    def __str__(self):
        return self.nome

class Cidades(models.Model):
    
    nome = models.CharField(max_length = 100)
    uf =  models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Cidades"

    def __str__(self):
        return f'{self.nome} {self.uf}'

class Pessoas(models.Model):

    nome = models.CharField(max_length = 100)
    nome_do_pai = models.CharField(max_length = 100)
    nome_da_mae = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 100)
    data_nasc = models.DateField()
    email = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pessoa"

    def __str__(self):
        return f'{self.nome} {self.nome_do_pai} {self.nome_da_mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade} {self.ocupacao}'
        
class Institucao(models.Model):

    nome = models.CharField(max_length = 100)
    site = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Instituições"

    def __str__(self):
        return f'{self.nome} - {self.site} - {self.telefone} - {self.cidade}'
    
class Area(models.Model):
    
    nome = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Áreas do Saber"

    def __str__(self):
        return self.nome


class Cursos(models.Model):
    
    nome = models.CharField(max_length = 100)
    carga_horaria_total =  models.CharField(max_length = 100)
    duracao_meses = models.CharField(max_length = 100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Institucao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nome} - {self.carga_horaria_total} - {self.duracao_meses} - {self.area} - {self.instituicao}'

class Disciplinas(models.Model):

    nome = models.CharField(max_length = 100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f'{self.nome} {self.area}'
    
class Periodos(models.Model):

    nome = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Períodos"
    def __str__(self):
        return self.nome
    

class Matricula(models.Model):

    instituicao = models.ForeignKey(Institucao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio = models.DateField(max_length = 100)
    data_termino = models.DateField(max_length = 100)
    
    class Meta:
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f'{self.instituicao, self.curso, self.pessoa, self.data_inicio, self.data_termino}'

class Avaliacoes(models.Model):

    descricao = models.CharField(max_length = 100)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f'{self.descricao} - { self.curso} - {self.disciplina}'
    

class Frequencia(models.Model):

    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    numero_faltas= models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Frequência"

    def __str__(self):
        return f'{self.curso, self.disciplina, self.pessoa, self.numero_faltas}'
    
class Turmas(models.Model):

    nome = models.CharField(max_length = 100)
    turno = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Turmas"

    def __str__(self):
        return f'{self.nome, self.turno}'
    
class Ocorrencia(models.Model):

    descricao = models.CharField(max_length = 100)
    data = models.DateField(max_length = 100)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Ocorrência"
        
    def __str__(self):
        return f'{self.descricao, self.data, self.curso, self.disciplina, self.pessoa}'

class Disciplina_Por_Curso(models.Model):

    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    carga_horaria_total =  models.CharField(max_length = 100)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Disciplina Por Curso"

    def __str__(self):
        return f'{self.disciplina, self.carga_horaria_total, self.curso, self.periodo}'

class Manter_avalicao(models.Model):

    nome = models.CharField(max_length = 100)
    class Meta:
        verbose_name_plural = "Manter Avalições"

    def __str__(self):
        return self.nome






