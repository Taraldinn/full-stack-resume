from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class ExtracurricularActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='extracurricular_activities')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='educations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    results = models.TextField(blank=True, null=True)

class workExperience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class socialMediaLink(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='social_media_links')
    platform = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.url}"

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.level})"

class Certification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    technologies_used = models.TextField(blank=True, null=True)  # JSON field to store technologies
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Award(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='awards')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_received = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='testimonials')
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(blank=True, null=True)
    author_position = models.CharField(max_length=255, blank=True, null=True)
    author_company = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Testimonial by {self.author_name}"

class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Profile(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.username


# base auth settings.AUTH_USER_MODEL model
# abstract settings.AUTH_USER_MODEL model
# custom settings.AUTH_USER_MODEL model