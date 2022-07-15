from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    url_project = models.URLField(max_length=250, blank=True, null=True, verbose_name="Dirección web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    #Se agrega clase Meta para cambiar nombres de ingles a español
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["created"]
    # Se manda a llamar a srt para que aparezcan el nombre de los proyectos en lugar de projects
    def __str__(self):
        return  self.title