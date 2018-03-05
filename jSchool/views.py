from django.shortcuts import render
from jSchool.models import Course, Student

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, "home.html", context)
