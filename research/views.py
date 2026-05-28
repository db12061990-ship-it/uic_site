from django.shortcuts import render
from .models import ResearchWork


def research_list(request):
    query = request.GET.get('q')
    status = request.GET.get('status')

    works = ResearchWork.objects.all()

    if query:
        works = works.filter(employee__icontains=query)

    if status:
        works = works.filter(status=status)

    return render(request, 'research/research.html', {
        'works': works
    })

# Create your views here.
