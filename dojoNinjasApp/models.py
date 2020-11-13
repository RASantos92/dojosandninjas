from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    guild = models.CharField(max_length=45)
    desc = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name="ninja", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


