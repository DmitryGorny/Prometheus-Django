from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class Author(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)


class Article(models.Model):
    DRAFT = True
    RELEASE = False
    CHOICES = (
        (DRAFT, 'DRAFT'),
        (RELEASE, 'RELEASE'),
    )
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    header = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(choices=CHOICES, default=CHOICES)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('Prometheus:article', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
