from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from .models import Post, MBAAlumniDetail, MBASchoolList, MBAIndustryList, MBABlogSubcriberList, MSSchoolList, MSMajorList, MSAlumniDetail, MSBlogSubcriberList
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import json


# ----------- 404 ErrorPage View
def error_404_view(request, exception):
    return render(request, 'app/404.html')



# ----------- HomePage View
def index(request):
    school = MBASchoolList.objects.all().order_by('school_name')
    industry = MBAIndustryList.objects.all().order_by('industry_name')

    major_ms = MSMajorList.objects.all().order_by('major_name')


    if request.method == "POST" and 'mail_btn' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        # subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            "Website Contact Us Lead", # subject
            "Name - " + name + "\nEmail - " + email + "\nPhone Number - " + number + "\nMessage - " + message, # message
            email, # from email
            ['help@alumnextdoor.com'], # to email
        )

        args = { 'name': name, 'school':school, 'industry':industry, 'major_ms':major_ms }
        return render(request, 'app/homePage.html', args)

    elif request.method == "POST" and 'blog_subscribe' in request.POST:
        email = request.POST['email']
        degree = request.POST['degree']

        if degree == "1":
            sub_list_obj = MBABlogSubcriberList(email = email)
            sub_list_obj.save()

        if degree == "2":
            sub_list_obj = MSBlogSubcriberList(email = email)
            sub_list_obj.save()
        
        
        args = { 'school':school, 'industry':industry, 'major_ms':major_ms }
        return render(request, 'app/homePage.html', args)

    else:
        args = { 'school':school, 'industry':industry, 'major_ms':major_ms }
        return render(request, 'app/homePage.html', args)



# ----------- BlogPage View
def BlogPageView(request):
    post = Post.objects.all()
    args = {'posts': post }

    if request.method == "POST" and 'blog_subscribe' in request.POST:
        email = request.POST['email']
        degree = request.POST['degree']

        if degree == "1":
            sub_list_obj = MBABlogSubcriberList(email = email)
            sub_list_obj.save()

        if degree == "2":
            sub_list_obj = MSBlogSubcriberList(email = email)
            sub_list_obj.save()
        
        args = { 'posts': post }
        return render(request, 'app/blogPage.html', args)
    
    return render(request, 'app/blogPage.html', args)



# ----------- SingleBlogPage View
def BlogPostDetailView(request, pk):

    post = get_object_or_404(Post, id=pk)
    print(post.form_subject)
    args = {
        'post':post
    }

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        bschool = request.POST['bschool']

        send_mail(
            "Website Blog Page Lead - " + post.form_subject, # subject
            "Name - " + name + "\nEmail - " + email + "\nPhone Number - " + number + "\nMessage - " + bschool, # message
            email, # from email
            ['help@alumnextdoor.com'], # to email
        )
        
        return render(request, 'app/singleBlogDetailPage.html',args)

    return render(request, 'app/singleBlogDetailPage.html',args)



# ----------- AlumniList View
@csrf_exempt
def AlumniListView(request):
    degree = request.POST.get("degree")
    school = request.POST.get("school")
    indus = request.POST.get("industry")
    school_ms = request.POST.get("school_ms")
    major_ms = request.POST.get("major_ms")

    if degree == "1":
        alumni_details = MBAAlumniDetail.objects.filter(FK_school_name = school, FK_industry_name = indus).order_by('name')

    elif degree == "2":
        alumni_details = MSAlumniDetail.objects.filter(FK_school_name = school_ms, FK_major_name = major_ms).order_by('name')


    
    industry = MBAIndustryList.objects.all()

    render_string = render_to_string("app/alumniList.html",{ 'degree':degree, 'alumni_details':alumni_details })

    return HttpResponse(render_string)



# ----------- MajorsList View
# @csrf_exempt
# def GetMajors(request):
#     schoolSelected = request.POST.get("schoolSelected")
#     major_list = list(MSMajorList.objects.filter(FK_school_name=schoolSelected).values_list('id', 'major_name').order_by('major_name'))

#     return HttpResponse(json.dumps(major_list))



# ----------- SchoolList View
@csrf_exempt
def GetSchools(request):
    majorSelected = request.POST.get("majorSelected")
    school_list = list(MSSchoolList.objects.filter(FK_major_name=majorSelected).values_list('id', 'school_name').order_by('school_name'))

    return HttpResponse(json.dumps(school_list))



# ----------- IndustriesList View
@csrf_exempt
def GetIndustries(request):
    schoolSelected = request.POST.get("schoolSelected")
    industry_list = list(MBAIndustryList.objects.filter(FK_school_name=schoolSelected).values_list('id', 'industry_name').order_by('industry_name'))

    return HttpResponse(json.dumps(industry_list))