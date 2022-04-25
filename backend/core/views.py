from django.shortcuts import render
from rest_framework import viewsets, status as http_status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser
from drf_yasg.utils import swagger_auto_schema

from .models import Language, Project, Sentence
from .serializers import LanguageSerializer, ProjectCreateSerializer, ProjectSerializer, SentenceUpdateSerializer
import pysbd
from wikipediaapi import Wikipedia


class ProjectViewSet(viewsets.ViewSet):
    parser_class = (FormParser, JSONParser)

    @swagger_auto_schema(responses={200: ProjectSerializer}, request_body=ProjectCreateSerializer)
    def create_project(self, request):
        """
        Request to create a project and fetching summary
        """
        try:
            project, created = Project.objects.get_or_create(
                wiki_title=request.data["wiki_title"],
                fk_target_lang=Language.objects.get(language_id=request.data["fk_target_lang"]),
            )

            if created:
                summary = Wikipedia().page(project.wiki_title).summary
                seg = pysbd.Segmenter(language='en',clean=False)
                summary = seg.segment(summary)
                for sentence in summary:
                    if sentence != "":
                        Sentence(fk_project=project, original_sentence=sentence).save()
                project = Project.objects.get(project_id=project.project_id)
                project.save()
                serialized = ProjectSerializer(project)
                return Response(serialized.data, status=http_status.HTTP_201_CREATED)

            else:
                return Response({"message": "Project of that title already exists."}, status=http_status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_projects(self, request):
        """
        Request to get projects
        """
        try:
            project = Project.objects.all()
            serialized = ProjectSerializer(project, many=True)
            return Response(serialized.data, status=http_status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=http_status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_project(self, request, project_id):
        """
        Request to get projects
        """
        try:
            project = Project.objects.get(project_id=project_id)
            serialized = ProjectSerializer(project)
            return Response(serialized.data, status=http_status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=http_status.HTTP_404_NOT_FOUND)

    def delete_project(self, request, project_id):
        try:
            project = Project.objects.get(project_id=project_id)
            project.delete()
            return Response(status=http_status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=http_status.HTTP_404_NOT_FOUND)


class SentenceViewSet(viewsets.ViewSet):
    parser_class = (FormParser, JSONParser)

    @swagger_auto_schema(request_body=SentenceUpdateSerializer)
    def update_sentence(self, request):
        serialized = SentenceUpdateSerializer(data=request.data)
        if serialized.is_valid():
            try:
                sentence = Sentence.objects.get(sentence_id=request.data["sentence_id"])
                sentence.translated_sentence = request.data["translated_sentence"]
                sentence.save()
                return Response(status=http_status.HTTP_200_OK)
            except Sentence.DoesNotExist:
                return Response(status=http_status.HTTP_404_NOT_FOUND)
            except Exception as e:
                print(e)
                return Response(status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=http_status.HTTP_400_BAD_REQUEST)

class LanguageViewSet(viewsets.ViewSet):
    parser_class = (FormParser, JSONParser)

    def get_languages(self, request):
        """
        Request to get languages
        """
        try:
            languages = Language.objects.all()
            serialized = LanguageSerializer(languages, many=True)
            return Response(serialized.data, status=http_status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=http_status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)
