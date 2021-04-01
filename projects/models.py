from django.db import models


# Create your models here.
class Projects(models.Model):
    """
    Stores project details
    """
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to='projects')
    link = models.URLField(max_length=500, blank=False)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Messages(models.Model):
    """
    Stores details of messages received from contact form
    """
    name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return f'{self.name} = {self.subject}'
