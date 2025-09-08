from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'index.html')


def custom_error_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "errors/404.html", status=404)


def custom_error_500(request: HttpRequest) -> HttpResponse:
    return render(request, "errors/500.html", status=500)
