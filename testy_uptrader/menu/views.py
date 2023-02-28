from django.http import HttpRequest
from django.shortcuts import render


def root(req: HttpRequest):
    return render(req, 'menu/root.html')
