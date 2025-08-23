"""
Docstring for bio.admin
"""

from django.contrib import admin

from bio.models import (
    Publication,
    Profile,
    ExtracurricularActivity,
    Education,
    WorkExperience,
    SocialMediaLink,
    Skill,
    Project,
    Certification,
    Testimonial,
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(ExtracurricularActivity)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(SocialMediaLink)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Certification)
admin.site.register(Testimonial)

admin.site.site_header = "Bio Admin"
admin.site.site_title = "Bio Admin Portal"
