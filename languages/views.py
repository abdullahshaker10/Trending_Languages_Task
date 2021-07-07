from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import TrandingGithubAPI


class TrandingLanguageAPIView(APIView):
    def get(self, request, languages_number, *args, **kwargs):
        github_api = TrandingGithubAPI(languages_number)
        Tranding_languages = github_api.get_trending_languages_data()
        return Response({"data": Tranding_languages})
