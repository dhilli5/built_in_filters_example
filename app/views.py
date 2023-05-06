from django.shortcuts import render

# Create your views here.

def filters(request): 
    import datetime 
    dt=datetime.datetime.now()
    d={'data':'hI HeLLo how you ','dt':dt}
    
    return render(request,'filters.html',d)
