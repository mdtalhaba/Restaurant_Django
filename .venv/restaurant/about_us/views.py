from django.shortcuts import render

def about(req) :
    return render(req, 'about_us/about.html')
