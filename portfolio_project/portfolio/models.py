from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    """Model to represent services offered."""
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

class Project(models.Model):
    """Model to represent a portfolio project."""

    class Category(models.TextChoices):
        WEB_DEVELOPMENT = 'WEB', _('Web Development')
        AI_VISUALS = 'AI', _('AI Visuals & Videos')
        VIDEO = 'VID', _('Video Editing')
        COMMUNITY_MANAGEMENT = 'CM', _('Community Management')

    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='projects/', verbose_name=_("Image"))
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name=_("Project Link"))
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.WEB_DEVELOPMENT,
        verbose_name=_("Category")
    )
    technologies_used = models.CharField(max_length=200, blank=True, verbose_name=_("Technologies Used"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creation Date"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-created_at']

class ContactMessage(models.Model):
    """Model to store contact form messages."""
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Received Date"))

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")
        ordering = ['-created_at']
