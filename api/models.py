from django.db import models
from api.helpers import SaveMediaFiles

class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft'
    PUBLISH = 'pb', 'Publish'

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField()
    listen = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    username = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()

    def __str__(self):
        return self.get_full_name()

class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft'
    PUBLISH = 'pb', 'Publish'

class Albom(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    description = models.TextField()
    listen = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()

    def __str__(self):
        return self.title


class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft'
    PUBLISH = 'pb', 'Publish'

class Songs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    image = models.URLField(max_length=1000)
    listen = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoice.choices, default=StatusChoice.PUBLISH)
    artist = models.ForeignKey(Albom, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == 'pb':
            self.status = 'df'
            self.save()


    def __str__(self):
        return self.title


class SongsAlbom(models.Model):
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Songs)
