from django.db import models

class SocialMediaLinks(models.Model):
    instagram = models.CharField(max_length=500, null=True,blank=True)
    twitter = models.CharField(max_length=500, null=True,blank=True)
    facebook = models.CharField(max_length=500, null=True,blank=True)
    rss = models.CharField(max_length=500, null=True,blank=True)
    tumblr = models.CharField(max_length=500, null=True,blank=True)


class productItems(models.Model):
    name = models.CharField(max_length=200, null=True,blank=True)
    description = models.CharField(max_length=1000, null=True,blank=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)
    img4 = models.FileField(null=True, blank=True)
    img5 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name



class ContactUs(models.Model):
    firstName = models.CharField(max_length=150,null=True,blank=True)
    lastName = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    message  =models.TextField(max_length=5000,null=True,blank=True)

    def __str__(self):
        return self.email

