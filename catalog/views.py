from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ReestrActive
from django.db.models import Q
# from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
   
    return render(
        request,
        'index.html',
    )

def indexTwo(request):

    return render(
        request,
        'twoIndex.html',
    )

def legislation(request):

    return render(
        request,
        'legislation.html',
    )

def documentsSro(request):

    return render(
        request,
        'documentsSro.html',
    )

def compensationFund(request):

    return render(
        request,
        "compensationFund.html"
    )

def protocols(request):

    return render(
        request,
        'protocols.html'
    )

class ReestrView(ListView):
    model = ReestrActive
    template_name = "registrySro.html"
    context_object_name = 'reestrActive'

def registrySro(request):
    if request.method=="POST":
        srch = request.POST["srh"]

        if srch:
            match = ReestrActive.objects.filter(inn = srch)

            if match:
                return render(request, "registrySro.html", {'sr':match})
            else:
                messages.error(request, "ничего не найдено")
        # else:
        #     return HttpResponseRedirect("indexTwo/")


    return render(
        request,
        "registrySro.html"
    )

def ManagementBodies(request):

    return render(
        request,
        "ManagementBodies.html"
    )

def intoSro(request):

    return render(
        request,
        "intoSro.html"
    )

def termsStrah(request):

    return render(
        request,
        "termsStrah.html"
    ) 

def vajnInfo(request):

    return render(
        request,
        "vajnInfo.html"
    )