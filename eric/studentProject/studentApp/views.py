from django.views.generic import ListView
from .models import Student


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student_list'
