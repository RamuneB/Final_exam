import uuid
from django.db import models
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User




class Uzrasas(models.Model):
    title = models.CharField('Pavadinimas', max_length=200)
    kategorija = models.ForeignKey('Kategorija', on_delete=models.SET_NULL, null=True, related_name='uzrasai')
    summary = models.TextField('Tekstas', max_length=1000)
    #genre = models.ManyToManyField('Genre')
    cover = models.ImageField('Viršelis', default="default.png", upload_to='covers')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Užrašas'
        verbose_name_plural = 'Užrašai'

  

    def kategorija_name(self):
        if self.kategorija:
            return self.kategorija.first_name
        else:
            return '-'

   


class Kategorija(models.Model):
   
    first_name = models.CharField('Vardas', max_length=100)
    #description = models.TextField('Aprašymas', max_length=2000, default='')
    description = HTMLField()

    def __str__(self):
        return f'{self.first_name}'

    def display_uzrasai(self):
        return ', '.join(uzrasas.title for uzrasas in self.uzrasai.all()[:3])

    display_uzrasai.short_description = 'Užrašai'


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)
