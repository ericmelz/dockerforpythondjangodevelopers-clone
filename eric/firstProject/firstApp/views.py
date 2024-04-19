from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('Django is cool and Docker volumes are awesome!')