from django.db import models


# Create your models here.
class Projects(models.Model):
    """
    Stores project details
    """
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
