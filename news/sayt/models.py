from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    is_name = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)

        return super(Category, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField()
    short_description = models.TextField()
    description = models.TextField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
