from pyexpat import model
from statistics import mode
from django.db import models


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    wiki_title = models.CharField(max_length=200, unique=True)
    fk_target_lang = models.ForeignKey(to=Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.wiki_title


class Sentence(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    fk_project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    original_sentence = models.CharField(max_length=500, null=True)
    translated_sentence = models.CharField(max_length=500, null=True,default="")