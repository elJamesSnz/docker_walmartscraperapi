from django.urls import path
from scrape_app.views import ScrapeView


urlpatterns = [
    path('api/scraper/despensa/', ScrapeView.as_view(), )
]