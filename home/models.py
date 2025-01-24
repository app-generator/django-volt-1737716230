# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    first name = models.CharField(max_length=255, null=True, blank=True)
    last name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email address = models.CharField(max_length=255, null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Licence(models.Model):

    #__Licence_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    #__Licence_FIELDS__END

    class Meta:
        verbose_name        = _("Licence")
        verbose_name_plural = _("Licence")


class Developer(models.Model):

    #__Developer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)

    #__Developer_FIELDS__END

    class Meta:
        verbose_name        = _("Developer")
        verbose_name_plural = _("Developer")


class Software(models.Model):

    #__Software_FIELDS__
    code_developer = models.CharField(max_length=255, null=True, blank=True)
    commercial = models.BooleanField()
    supported_os = models.IntegerField(null=True, blank=True)

    #__Software_FIELDS__END

    class Meta:
        verbose_name        = _("Software")
        verbose_name_plural = _("Software")


class Modelinformation(models.Model):

    #__Modelinformation_FIELDS__
    material_behaviour = models.IntegerField(null=True, blank=True)
    input_parameters = models.TextField(max_length=255, null=True, blank=True)
    output_parameters = models.TextField(max_length=255, null=True, blank=True)
    chaining_support = models.BooleanField()

    #__Modelinformation_FIELDS__END

    class Meta:
        verbose_name        = _("Modelinformation")
        verbose_name_plural = _("Modelinformation")


class Implementationdetail(models.Model):

    #__Implementationdetail_FIELDS__
    source_code = models.CharField(max_length=255, null=True, blank=True)
    documentation = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE)
    in_main = models.BooleanField()
    supported_os = models.IntegerField(null=True, blank=True)
    gpu_support = models.IntegerField(null=True, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    #__Implementationdetail_FIELDS__END

    class Meta:
        verbose_name        = _("Implementationdetail")
        verbose_name_plural = _("Implementationdetail")


class Modelsuitability(models.Model):

    #__Modelsuitability_FIELDS__
    minimum_size = models.CharField(max_length=255, null=True, blank=True)
    maximum_size = models.CharField(max_length=255, null=True, blank=True)
    nature = models.IntegerField(null=True, blank=True)

    #__Modelsuitability_FIELDS__END

    class Meta:
        verbose_name        = _("Modelsuitability")
        verbose_name_plural = _("Modelsuitability")


class Contactmodel(models.Model):

    #__Contactmodel_FIELDS__
    model_type = models.IntegerField(null=True, blank=True)
    nature = models.IntegerField(null=True, blank=True)
    shape_suitability = models.IntegerField(null=True, blank=True)
    damping_model = models.IntegerField(null=True, blank=True)
    dimensionality = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    implementation = models.ForeignKey(ImplementationDetail, on_delete=models.CASCADE)
    information = models.ForeignKey(ModelInformation, on_delete=models.CASCADE)
    suitability = models.ForeignKey(ModelSuitability, on_delete=models.CASCADE)

    #__Contactmodel_FIELDS__END

    class Meta:
        verbose_name        = _("Contactmodel")
        verbose_name_plural = _("Contactmodel")


class Record(models.Model):

    #__Record_FIELDS__
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    contact_model = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(Developer, on_delete=models.CASCADE)
    is_draft = models.BooleanField()

    #__Record_FIELDS__END

    class Meta:
        verbose_name        = _("Record")
        verbose_name_plural = _("Record")


class Revisionhistory(models.Model):

    #__Revisionhistory_FIELDS__
    revision = models.IntegerField(null=True, blank=True)
    date_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)
    contact_model = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    submitted_by = models.CharField(max_length=255, null=True, blank=True)

    #__Revisionhistory_FIELDS__END

    class Meta:
        verbose_name        = _("Revisionhistory")
        verbose_name_plural = _("Revisionhistory")


class Relatedpublications(models.Model):

    #__Relatedpublications_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    pub_type = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    pub_name = models.CharField(max_length=255, null=True, blank=True)
    volume = models.CharField(max_length=255, null=True, blank=True)
    issue = models.CharField(max_length=255, null=True, blank=True)
    pages = models.CharField(max_length=255, null=True, blank=True)
    doi = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    accessed = models.CharField(max_length=255, null=True, blank=True)
    submitted_by = models.ForeignKey(Developer, on_delete=models.CASCADE)

    #__Relatedpublications_FIELDS__END

    class Meta:
        verbose_name        = _("Relatedpublications")
        verbose_name_plural = _("Relatedpublications")



#__MODELS__END
