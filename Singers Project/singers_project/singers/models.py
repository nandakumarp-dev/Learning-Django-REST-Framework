from django.db import models
import uuid

# Base abstract model

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True, default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        abstract = True

# Genre choices

class GenreChoices(models.TextChoices):

    POP = 'Pop', 'Pop'
    ROCK = 'Rock', 'Rock'
    CLASSICAL = 'Classical', 'Classical'
    HIP_HOP = 'Hip-Hop', 'Hip-Hop'
    JAZZ = 'Jazz', 'Jazz'
    FOLK = 'Folk', 'Folk'
    COUNTRY = 'Country', 'Country'
    EDM = 'EDM', 'Electronic Dance Music'
    OTHER = 'Other', 'Other'

# Gender choices

class GenderChoices(models.TextChoices):

    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHER = 'Other', 'Other'

# Singer model

class Singers(BaseClass):

    name = models.CharField(max_length=50)

    date_of_birth = models.DateField(blank=True, null=True)

    gender = models.CharField(max_length=15, choices=GenderChoices.choices, blank=True)

    number_of_songs = models.PositiveIntegerField(default=0)

    nationality = models.CharField(max_length=100, blank=True)

    genre = models.CharField(max_length=50, choices=GenreChoices.choices, default=GenreChoices.OTHER)

    class Meta:

        verbose_name = 'Singer'

        verbose_name_plural = 'Singers'

    def __str__(self):

        return f'{self.name} - {self.genre} - {self.nationality}'
