from django.db import models

# Create your models here.

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class UsuarioModel(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    dtNasc = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    email = models.EmailField('E-mail', max_length=100)
    renda = models.DecimalField('Renda', max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.nome} {self.sexo} {self.dtNasc}'