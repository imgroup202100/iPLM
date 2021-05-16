from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from CRS.models import User

def index(request):
    return render(request, 'index.html')

def chairperson_login(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            type_obj = request.user
            if user.is_authenticated and type_obj.is_chairperson:
                return redirect('chairperson')
        else:
            return redirect('chairperson_login')
    return render(request, 'chairperson_login.html')

def chairperson(request):
    if request.user.is_authenticated and request.user.is_chairperson:
        username = request.user.username
        return render(request,'./chairperson/chairperson.html',{'username':username})
    else:
        return redirect('chairperson_login')

def faculty_login(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            type_obj = request.user
            if user.is_authenticated and type_obj.is_faculty:
                return redirect('faculty')
        else:
            return redirect('faculty_login')
    return render(request, 'faculty_login.html')

def faculty(request):
    if request.user.is_authenticated and request.user.is_faculty:
        username = request.user.username
        return render(request,'./faculty/faculty.html',{'username':username})
    else:
        return redirect('faculty_login')

def applicant(request):
    if request.user.is_authenticated and request.user.is_applicant:
        username = request.user.username
        return render(request,'./applicant/applicant.html',{'username':username})
    else:
        return redirect('faculty_login')

def student_login(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            type_obj = request.user
            if user.is_authenticated and type_obj.is_student:
                return redirect('students')
        else:
            return redirect('student_login')
    return render (request,'student_login.html')

def students(request):
    username = request.user.username
    if request.user.is_authenticated and request.user.is_student:
        return render(request,'./student/student.html',{'username':username})
    else:
        return redirect('student_login')
def applicant_login(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            type_obj = request.user
            if user.is_authenticated and type_obj.is_applicant:
                return redirect('applicant')
        else:
            return redirect('applicant_login')
    return render(request, 'applicant_login.html')

def admin_login(request):
    if(request.method == 'POST'):
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            type_obj = request.user
            if user.is_authenticated and type_obj.is_superuser:
                return redirect('admin')
        else:
            return redirect('admin_login')
    return render (request,'admin_login.html')

def admin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if (request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_type = request.POST.get('user_type')

            user = User.objects.create_user(
                username=username
            )
            user.set_password(password)
            user.save()
            ut = None
            if user_type == 'admin':
                user.is_superuser = True
                user.save()
            elif user_type == 'applicant':
                user.is_applicant = True
                user.save()
            elif user_type == 'chairperson':
                user.is_chairperson = True
                user.save()
            elif user_type == 'faculty':
                user.is_faculty = True
                user.save()
            elif user_type == 'student':
                user.is_student = True
                user.save()

        return render(request,'./admin/admin.html')
    else:
        return redirect('admin_login')