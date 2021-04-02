from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string


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

    def send_contact_submitted_email(self, email_info):
        """
        Send email to me  on successful contact form submission
        """
        try:
            template_dict = {
                'email_info': email_info
            }
            message = render_to_string('emails/contact-submitted.html', template_dict)
            subject = "Portfolio Contact Form Submitted!"
            to_email = [settings.FROM_EMAIL]
            send_mail(subject, message, settings.FROM_EMAIL, to_email)
        except:
            return False

        return True

    def send_confirmation_email(self, email_info):
        """
        Send confirmation email to user on successful contact form submission
        """
        try:
            template_dict = {
                'email_info': email_info
            }
            message = render_to_string('emails/confirmation.html', template_dict)

            subject = "Thanks for getting in touch!"
            to_email = [email_info.email]
            send_mail(subject, message, settings.FROM_EMAIL, to_email)
        except:
            return False

        return True
