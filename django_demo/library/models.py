import uuid
from django.db import models


class Uzrasas(models.Model):
    """Modelis reprezentuoja knygą (bet ne specifinę knygos kopiją)"""
    title = models.CharField('Pavadinimas', max_length=200)
    kategorija = models.ForeignKey('Kategorija', on_delete=models.SET_NULL, null=True, related_name='uzrasai')
    summary = models.TextField('Tekstas', max_length=1000)
    #genre = models.ManyToManyField('Genre')
    cover = models.ImageField('Viršelis', upload_to='covers', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Užrašas'
        verbose_name_plural = 'Užrašai'

   # def display_genre(self):
    #    return ', '.join(genre.name for genre in self.genre.all()[:3])

    def kategorija_name(self):
        if self.kategorija:
            return self.kategorija.first_name
        else:
            return '-'

    #display_genre.short_description = 'Žanras'

'''
class UzrasasInstance(models.Model):
    """Modelis, aprašantis konkrečios knygos kopijos būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    uzrasas = models.ForeignKey('Uzrasas', on_delete=models.SET_NULL, null=True) 
    due_back = models.DateField('Bus prieinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.uzrasas.title})'

'''
class Kategorija(models.Model):
   
    first_name = models.CharField('Vardas', max_length=100)
    description = models.TextField('Aprašymas', max_length=2000, default='')

    def __str__(self):
        return f'{self.first_name}'

    def display_uzrasai(self):
        return ', '.join(uzrasas.title for uzrasas in self.uzrasai.all()[:3])

    display_uzrasai.short_description = 'Užrašai'

'''
class Genre(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)

    def __str__(self):
        return self.name
        '''
