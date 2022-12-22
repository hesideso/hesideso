from django.db import models
from django.utils.text import slugify


class Produit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='image_cat')
    description = models.TextField(null=True, blank=True)

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Profil(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_profil')


class Terms(models.Model):
    content = models.TextField()
