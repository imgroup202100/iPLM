from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def chairperson_login(request):
    return render(request, 'chairperson_login.html')

def faculty_login(request):
    return render(request, 'faculty_login.html')

def student_login(request):
    return render(request, 'student_login.html')

def applicant_login(request):
    return render(request, 'applicant_login.html')