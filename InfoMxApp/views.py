from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'information/index.html',{'title':'La Viruela Del Mono'})

def about(request):
    return render(request,'information/about.html',{'abt':'Acerca De Nosotros'})
def contact(request):
    return render(request,'information/contact.html',{'abt':'Acerca De Nosotros'})
