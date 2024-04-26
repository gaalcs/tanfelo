from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tanfelo_Tantargy, Tanfelo_Tanar, Tanfelo_Tanulocsoport

# Create your views here.

@login_required
def feltoltes_view(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

# Tantárgyak feltoltese
@login_required
def tantargyak_feltoltese_view(request):
    template = 'feltoltes_tantargyak.html'
    context = {}
    return render(request, template, context)

@login_required
def tantargyak_feltoltese_kuld_view(request):
    template = 'feltoltes_tantargyak_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Tanfelo_Tantargy.objects.create(
            nev = sortomb[0],
            slug = "-",
        )

    return render(request, template, context)

# Tanárok feltoltese
@login_required
def tanarok_feltoltese_view(request):
    template = 'feltoltes_tanarok.html'
    context = {}
    return render(request, template, context)

@login_required
def tanarok_feltoltese_kuld_view(request):
    template = 'feltoltes_tanarok_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        neve = Tanfelo_Tanar.objects.create(
            nev = sortomb[0],
        )
        # nem kell egyelore a tanarok tantargyai, majd a kmk-bol fog kidelulni
        # for tantargy in sortomb[1:]:
        #     a_tantargya = Tanfelo_Tantargy.objects.get(nev = tantargy)
        #     neve.tantargyai.add(a_tantargya)

    return render(request, template, context)

# Tanulócsoportok feltoltese
@login_required
def tanulocsoportok_feltoltese_view(request):
    template = 'feltoltes_tanulocsoportok.html'
    context = {}
    return render(request, template, context)

@login_required
def tanulocsoportok_feltoltese_kuld_view(request):
    template = 'feltoltes_tanulocsoportok_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Tanfelo_Tanulocsoport.objects.create(
            nev = sortomb[0],
            kreta = sortomb[0],
        )

    return render(request, template, context)

# # Tantárgy-Tanár kapcsolat feltoltese
# @login_required
# def kapcsolat_feltoltese_view(request):
#     template = 'feltoltes_kapcsolat.html'
#     context = {}
#     return render(request, template, context)

# @login_required
# def kapcsolat_feltoltese_kuld_view(request):
#     template = 'feltoltes_kapcsolat_kuld.html'
#     context = {}
#     nyers = request.POST['tsv_szoveg'].strip()
#     sorok = nyers.split('\r\n')
#     for sor in sorok[1:]:
#         sortomb = sor.split('\t')
#         a_tanar = Tanfelo_Tanar.objects.get(nev = sortomb[0]) #get-first!!!
#         for tantargy in sortomb[:1]:
#             a_tantargya = Tanfelo_Tantargy.objects.get(nev = tantargy)
#             a_tanar.tantargyai.add(a_tantargya)
#             # a_tantargya.tantargygondozoi.add(a_tanar.user)

#     return render(request, template, context)



# KMK feltoltese
@login_required
def tantargyak_feltoltese_view(request):
    template = 'feltoltes_tantargyak.html'
    context = {}
    return render(request, template, context)

@login_required
def tantargyak_feltoltese_kuld_view(request):
    template = 'feltoltes_tantargyak_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        Tanfelo_Tantargy.objects.create(
            nev = sortomb[0],
            slug = sortomb[0],
            # tantargygondozoi = sortomb[2],
        )

    return render(request, template, context)


























# Tanulocsoportok
@login_required
def tancsoportok_view(request):
    template = 'tancsoportok.html'
    context = {
        "tancsoportok": Tanfelo_Tanulocsoport.objects.all(),
    }
    return render(request, template, context)

# Tanulocsoportok
@login_required
def tancsoportok_id_view(request, id):
    template = 'tancsoportok.html'

    for tancsoport in Tanfelo_Tanulocsoport.objects.all():
        if tancsoport.id == id:
            context = {
                "tancsoportok": Tanfelo_Tanulocsoport.objects.all(),
                "id": id,
            }
            

    return render(request, template, context)
