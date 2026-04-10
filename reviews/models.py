from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model): 
    
    Movie = models.ForeignKey(
        Movie, 
        on_delete=models.PROTECT,
        related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Nota precisa ser maior que 0 estrelas'),
            MinValueValidator(5, 'Nota precisa ser menor que 5 estrelas')
        ]
    )
    comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title