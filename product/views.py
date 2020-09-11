from django.shortcuts import render
from .models import *

def Home(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    items = productItems.objects.all()
    if request.method == "POST":
        d = request.POST
        Firstname = d["firstname"]
        Lastname = d["lastname"]
        Email = d["email"]
        Meassage = d["message"]
        ContactUs.objects.create(firstName=Firstname,lastName=Lastname,email=Email,message=Meassage)
    data = {
        "links": socialMedialinks, "item": items
    }
    return render(request, "index.html",data)


def About(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    if request.method == "POST":
        d = request.POST
        Firstname = d["firstname"]
        Lastname = d["lastname"]
        Email = d["email"]
        Meassage = d["message"]
        ContactUs.objects.create(firstName=Firstname,lastName=Lastname,email=Email,message=Meassage)
    data = {
        "links": socialMedialinks
    }
    return render(request, "about.html",data)


def Contact(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    if request.method == "POST":
        d = request.POST
        Firstname = d["firstname"]
        Lastname = d["lastname"]
        Email = d["email"]
        Meassage = d["message"]
        ContactUs.objects.create(firstName=Firstname,lastName=Lastname,email=Email,message=Meassage)
    data = {
        "links": socialMedialinks
    }
    return render(request, "contact.html",data)


def Gallery(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    data = {
        "links": socialMedialinks
    }
    return render(request, "gallery.html",data)


def Shop(request):
    item = productItems.objects.all()
    socialMedialinks = SocialMediaLinks.objects.all().first()
    data = {
        "links": socialMedialinks, "item": item
    }
    return render(request, "shop.html",data)


def Blog(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    data = {
        "links": socialMedialinks
    }
    return render(request, "blog.html",data)

def Product_Show_Case(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    data = {
        "links": socialMedialinks
    }
    return render(request, "product_showcase.html",data)


def Product_Description_Page(request):
    socialMedialinks = SocialMediaLinks.objects.all().first()
    data = {
        "links": socialMedialinks
    }
    return render(request, "gallery_with_description.html",data)



def Info(request):
    cinfo = ContactUs.objects.all()
    d = {
        "data": cinfo
    }
    return render(request, "contactUs_data.html",d)


def Product_details_page(request,p_id):
    item = productItems.objects.filter(id = p_id).first()

    data = {
        "item": item
    }
    return render(request, "product_info.html",data)