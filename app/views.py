from django.shortcuts import render, HttpResponse
from .models import Login
import requests
from datetime import datetime as d
import os


# Create your views here.
def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

def syllabus(request):
    return render(request, 'syllabus.html', {'navbar': 'syllabus'})

def register(request):
    if request.method == 'POST':
        emailId = request.POST['emailId']
        # password = request.POST['password']
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
        # state = request.POST['state']
        if 'state' in request.POST:
            state = request.POST['state']
        else:
            state = False
        pincode = request.POST['pincode']
        phone_no = request.POST['phone_no']
        # profile = request.FILES['profile']
        if 'profile' in request.FILES:
            # if os.path.getsize(request.FILES['profile']) < 200000:
                # profile = request.FILES['profile']
            profile = request.FILES['profile']
        else:
            profile = False
            # return HttpResponse("File Size in more than 200kb")
        # signature = request.FILES['signature']
        if 'signature' in request.FILES:
            # if os.path.getsize(request.FILES['signature']) < 200000:
                # signature = request.FILES['signature']
            signature = request.FILES['signature']
            # print("t")
        else:
            # print("F")
            signature = False
            # return HttpResponse("File Size in more than 200kb")

        # caste_certificate = request.FILES['caste_certificate']
        if 'caste_certificate' in request.FILES:
            # if os.path.getsize(request.FILES['caste_certificate']) < 200000:
                # caste_certificate = request.FILES['caste_certificate']
            caste_certificate = request.FILES['caste_certificate']
        else:
            caste_certificate = False
            # return HttpResponse("File Size in more than 200kb")

        # qualification = request.FILES['qualification']
        if 'qualification' in request.FILES:
            # if os.path.getsize(request.FILES['qualification']) < 200000:
                # qualification = request.FILES['qualification']
            qualification = request.FILES['qualification']
        else:
            qualification = False
            # return HttpResponse("File Size in more than 200kb")

        date = d.now()
        registration_no ="GGV_DACE_" +  str(date.strftime("%Y%m%d%H%M%S"))
        final = Login.objects.create(emailId=emailId, name=name, dob=dob, gender=gender,
        category=category, father_name=father_name, mother_name=mother_name, address=address,
        state=state, pincode=pincode,phone_no=phone_no, profile=profile, signature=signature,
        caste_certificate=caste_certificate, qualification=qualification, permanent_address=permanent_address,
        registration_no=registration_no)
        final.save()
        return HttpResponse("Sucess!")
    return render(request, 'register.html', {'navbar': 'register'})

    
    


def success(request):
    return render(request, 'success.html', {'navbar': 'success'})

def aboutdace(request):
    return render(request, 'aboutdace.html', {'navbar': 'aboutdace'})

def aboutggv(request):
    return render(request, 'aboutggv.html', {'navbar': 'aboutggv'})

