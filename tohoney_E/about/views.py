from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about/about.html')
def faq(request):
    return render(request, 'about/faq.html')
