from django.shortcuts import render
from .models import student, course
from django.http import JsonResponse

def search_students(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        query = request.GET.get('query','')
        students = student.objects.filter(student_name__icontains = query)
        result = []
        for student1 in students :
            student_data = {
                'id': student1.id,
                'Name': student1.student_name,
                'Semester': student1.student_sem,
                'courses': [course.course_name for course in student1.enrolment.all()]
            }
            result.append(student_data)
        return JsonResponse({'Result': result})
    return render(request, 'search.html')
