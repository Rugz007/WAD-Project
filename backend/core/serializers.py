from pyexpat import model
from unittest.mock import sentinel
from django.db.models import fields
from rest_framework import serializers
from django.db import models
from .models import Project, Sentence, Language


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SentenceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ["sentence_id", "translated_sentence"]


class ProjectSerializer(serializers.ModelSerializer):
    sentences = serializers.SerializerMethodField()
    language_code = serializers.SerializerMethodField()
    language_name = serializers.SerializerMethodField()

    def get_sentences(self, obj):
        temp = Sentence.objects.filter(fk_project=obj)
        return SentenceSerializer(temp, many=True).data

    def get_language_code(self, obj):
        return obj.fk_target_lang.code

    def get_language_name(self, obj):
        return obj.fk_target_lang.name

    class Meta:
        model = Project
        fields = ["wiki_title", "project_id", "fk_target_lang", "sentences", "language_code", "language_name"]


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["wiki_title", "fk_target_lang"]
