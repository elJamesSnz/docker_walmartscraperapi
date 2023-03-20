from rest_framework.response import Response
from rest_framework.views import APIView
from scrape_app.models import Categoria
from django.http import JsonResponse
from .scraper import scrape_walmart

class ScrapeView(APIView):
    def post(self, request):
        data = request.data.dict()
        todo = Categoria(name=data['name'], url=data['url'])    
        todo.save()    
        return Response(200)
    def get(self, request):

        categories = scrape_walmart()
        return JsonResponse(categories, safe=False)