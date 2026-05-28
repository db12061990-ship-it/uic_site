from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def about2(request):
    return render(request, 'main/about2.html')


def employees(request):
    return render(request, 'main/employees.html')


def conferences(request):
    return render(request, 'main/conferences.html')


def contacts(request):
    return render(request, 'main/contacts.html')