from django.db import models


# Create your models here.
class PersonalDetails(models.Model):
    """
    Stores personal details
    """
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    job_title = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=50, blank=False)
    about = models.TextField(max_length=2000, blank=False)
    github_url = models.URLField(blank=False)
    facebook_url = models.URLField(blank=False)
    instagram_url = models.URLField(blank=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


class ProfessionalSkills(models.Model):
    """
    Stores personal skills
    """
    skill = models.CharField(max_length=50, blank=False)
    percentage_completed = models.PositiveIntegerField(blank=False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.skill} - {self.percentage_completed}%'


class WorkExperience(models.Model):
    """
    Stores work experience details
    """
    company = models.CharField(max_length=50, blank=False)
    date_from = models.DateField(blank=False)
    date_to = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=2000, blank=False)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.company


class Education(models.Model):
    """
    Stores education details
    """
    title = models.CharField(max_length=500, blank=False)
    qualification_type = models.CharField(max_length=50, blank=False)
    date_from = models.DateField(blank=False)
    date_to = models.DateField(blank=True, null=True)
    awarding_body = models.CharField(max_length=50, blank=False)
    grade = models.CharField(max_length=20, blank=True, null=True)
    details = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f'{self.title} - {self.qualification_type}'
