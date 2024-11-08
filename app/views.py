from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    dt=datetime.datetime.now()
    data='WelCome to my wEbsite'
    d={'data':data,'dt':dt,'c':1}
    return render(request,'filters.html',d)