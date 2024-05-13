from django.db import models

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Musico(models.Model):
    nombre = models.CharField(max_length=255)
    instrumento = models.CharField(max_length=100)
    genero_primario = models.ForeignKey(GeneroMusical, on_delete=models.SET_NULL, null=True, related_name='musico_genero_primario')
    genero_secundario = models.ForeignKey(GeneroMusical, on_delete=models.SET_NULL, null=True, blank=True, related_name='musico_genero_secundario')

    def __str__(self):
        return self.nombre

class Banda(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pertenece(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    fecha_unido = models.DateField(auto_now_add=True)

class SolicitudUnirseBanda(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aceptada = models.BooleanField(default=False)

    def __str__(self):
        return f'Solicitud de {self.musico.nombre} a {self.banda.nombre}'

