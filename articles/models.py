from django.db import models
from django.conf import settings
from django.utils import timezone

## A Django model is used in the architecture of the db tables
#   where class is the table and each field is an entity of that table

class Article(models.Model):

    ''' Model for articles '''

    type = models.CharField(
        max_length=1,
        choices=[('T', 'Tutorial'), ('S', 'Story')],
        default='T')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True)
    jupyter_playground = models.FileField()
    image = models.ImageField(blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
