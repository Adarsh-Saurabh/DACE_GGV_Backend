from django.shortcuts import render, HttpResponse
from .models import Login
from datetime import datetime as d
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')

def syllabus(request):
    return render(request, 'syllabus.html')

def register(request):
    if request.method == 'POST':
        emailId = request.POST['emailId']

        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        # category = request.POST.get['category',False]
        ######################################################################################################
        # when theres's multiple options to select like in this case(go to register.html for more information)
        # the django will give multivaledictkey error and if you try to solve this useing
        # get functin you will get anothet error so for that we need to use the 
        # below method to solve this issue
        if 'category' in request.POST:
            category = request.POST['category']
        else:
            category = False
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        address = request.POST['address']
        permanent_address = request.POST["permanent_address"]

        if 'state' in request.POST:
            state = request.POST['state']
        else:
            state = False
        pincode = request.POST['pincode']
        phone_no = request.POST['phone_no']

        if 'profile' in request.FILES:

            profile = request.FILES['profile']
        else:
            profile = False

        if 'signature' in request.FILES:

            signature = request.FILES['signature']

        else:

            signature = False

        if 'caste_certificate' in request.FILES:

            caste_certificate = request.FILES['caste_certificate']
        else:
            caste_certificate = False

        if 'qualification' in request.FILES:

            qualification = request.FILES['qualification']
        else:
            qualification = False


        date = d.now()
        registration_no ="GGV_DACE_" +  str(date.strftime("%Y%m%d%H%M%S"))
        final = Login.objects.create(emailId=emailId, name=name, dob=dob, gender=gender,
        category=category, father_name=father_name, mother_name=mother_name, address=address,
        state=state, pincode=pincode,phone_no=phone_no, profile=profile, signature=signature,
        caste_certificate=caste_certificate, qualification=qualification, permanent_address=permanent_address,
        registration_no=registration_no)
        final.save()
        return render(request, 'success.html')
    return render(request, 'register.html')

    
    


def success(request):
    return render(request, 'success.html')

def aboutdace(request):
    return render(request, 'aboutdace.html')

def aboutggv(request):
    return render(request, 'aboutggv.html')

def signin(request):
    return render(request, 'signIn.html')