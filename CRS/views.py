from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from CRS.models import User
from CRS.models import facultyApplicant, Student

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
    return render(request,'./applicant/applicant.html')

def faculty_applicant(request):
    return render(request, './applicant/faculty_applicant.html')

def faculty_applicant_form(request):
    if (request.method == 'POST'):
        try:
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            middleName = request.POST['middleName']
            email = request.POST['email']
            phoneNumber = request.POST['phoneNumber']
            CV = request.FILES['CV']
            certificates = request.FILES.get('certificates')
            credentials = request.FILES.get('credentials')
            TOR = request.FILES['TOR']
            facultyApplicantInfo = facultyApplicant(firstName=firstName,lastName=lastName,middleName=middleName,email=email,phoneNumber=phoneNumber,CV=CV, certificates=certificates, credentials=credentials, TOR=TOR)
            facultyApplicantInfo.save()
            return redirect('faculty_applicant_form_submitted')
        except:
            messages.error(request,'Fill everything on the form!')
            return render(request,'./applicant/faculty_applicant_form.html')


    return render(request, './applicant/faculty_applicant_form.html')
    
def faculty_applicant_form_submitted(request):
    return render(request,'./applicant/faculty_applicant_form_submitted.html')
def student_applicant(request):
    return render(request,'./applicant/student_applicant.html')

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
            sNum = request.POST.get('studentNumber')

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
                '''
                testing lang hehehhee
                asdstudent = Student.objects.create(user=user)
                asdstudent.studentNumber(sNum)
                asdstudent.save()
                '''

        return render(request,'./admin/admin.html')
    else:
        return redirect('admin_login')