from django.db import models

class CV(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    skills = models.TextField(help_text="Comma-separated list of skills")
    projects = models.TextField(help_text="Comma-separated list of project names or descriptions")
    contacts = models.TextField(help_text="Store contact info like email, phone, links")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"