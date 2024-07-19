from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
# Create your models here.

STATUS = (
    ("rascunho", "Rascunho"),
    ("desabilitado", "Desabilitado"),
    ("publicado", "Publicado")
)

class Categoria(models.Model):
    cid = ShortUUIDField(unique=True, length=5, max_length=10, alphabet="abcdef12345")
    titulo = models.CharField(max_length=50,help_text="Categoria do Produto")
    imagem = models.ImageField(upload_to="categoria")

    class Meta:
        verbose_name_plural = "categorias"

    def categoria_image(self):
        return mark_safe('<img src="%s" width="50" heigth="50"/>'%(self.imagem.url))
    def __str__(self):
        return self.titulo