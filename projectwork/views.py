# Views.py controls what is being seen in the browser
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import urlForm
import requests
from bs4 import BeautifulSoup

def home_page(request):
    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        print (search_id)
        def printurl():  
            read = requests.get(search_id)
            soup = BeautifulSoup(read.content)
            #print(soup.find_all("a"))
            for link in soup.find_all("a"):
                printout = link.get("href")
                print (printout)
                
            pass
            
        form = urlForm(request.POST or None)
        context ={
            "form": form,
        }

        if form.is_valid():

            print("The form is valid")
            response = requests.get(search_id ).text
            if 'You have an error in your SQL syntax;' in response:
                print ('its vulnerable')
                printurl()
               
                return render(request, "vulnerable.html", context)
                
            else:
                print ('its not vulnerable')
                printurl()

                return render(request, "notvulnerable.html", context)
   
    
    return render(request, "index.html", context)