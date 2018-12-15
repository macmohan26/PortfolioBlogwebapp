from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Work

app_name = 'job'
def home(request):
    object_list = Work.objects.all()

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        works = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        works = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        works = paginator.page(paginator.num_pages)

    return render(request,
                  'job/home.html',
                  {'page': page,
                   'works': works})









# def home(request):
#      works = Work.objects.all()
#      return render(request, 'job/home.html', {'works':works})
