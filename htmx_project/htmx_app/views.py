from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from django.views.generic import TemplateView
from django.views import View


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class HomepageView(TemplateView):
    template_name = "index.html"


class HtmxTestView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'htmx_test_paragraph.html')
    
    def patch(self, request, *args, **kwargs):
        return render(request, 'row_1.html')
    
    def get(self, request, *args, **kwargs):
        return render(request, 'htmx_test_paragraph_2.html')
    
    def put(self, request, *args, **kwargs):
        return render(request, 'row_2.html')
