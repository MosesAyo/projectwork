from django.utils.html import format_html
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import urlForm
import requests

def home_page(request):
    form = urlForm(request.POST or None)
    context ={
        "form": form
    }
    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        print (search_id)
        if form.is_valid():
            print("The form is valid")
            response = requests.get(search_id + "%27").text

            if 'You have an error in your SQL syntax;' in response: 
                print ('its vulnerable')

                return render(request, "vulnerable.html", context)
                
            else:
                print ('its not vulnerable')
                
                return render(request,"notvulnerable.html", context)
   

        
    return render(request, "index.html", context)