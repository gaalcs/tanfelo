from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tanfelo_Tantargy, Tanfelo_Tanar, Tanfelo_Tanulocsoport, Tanfelo_Kmk
from inputok import 

# Create your views here.



# KMK feltoltese
def kmk_feltoltese(request):
    context = {
        "kmk": 
    }
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Tanfelo_Kmk.objects.create(
            tanar = sortomb[0],
            tantargy = sortomb[1],
            tanulocsoport = sortomb[2],
            oraszam = sortomb[3],
        )

    return render(request, context)



# Tanulocsoport feltoltese
def kmk_feltoltese(request):
    context = {
        "kmk": 
    }
    kmk = kmk.txt
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Tanfelo_Tanulocsoport.objects.create(
            tanar = sortomb[0],
            tantargy = sortomb[1],
            tanulocsoport = sortomb[2],
            oraszam = sortomb[3],
        )

    return render(request, context)
