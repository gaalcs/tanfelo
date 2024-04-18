from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tanfelo_Tantargy, Tanfelo_Tanar

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
            slug = sortomb[1],
            # tantargygondozoi = sortomb[2],
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
        Tanfelo_Tanar.objects.create(
            nev = sortomb[0],
            # tantargyai = sortomb[1],
        )

    return render(request, template, context)

# Tantárgy-Tanár kapcsolat feltoltese
@login_required
def kapcsolat_feltoltese_view(request):
    template = 'feltoltes_kapcsolat.html'
    context = {}
    return render(request, template, context)

@login_required
def kapcsolat_feltoltese_kuld_view(request):
    template = 'feltoltes_kapcsolat_kuld.html'
    context = {}
    nyers = request.POST['tsv_szoveg'].strip()
    sorok = nyers.split('\r\n')
    for sor in sorok[1:]:
        sortomb = sor.split('\t')
        a_tanar = Tanfelo_Tanar.objects.get(nev = sortomb[0]) #get-first!!!
        for tantargy in sortomb[:1]:
            a_tantargya = Tanfelo_Tantargy.objects.get(nev = tantargy)
            a_tanar.tantargyai.add(a_tantargya)
            a_tantargya.tantargygondozoi.add(a_tanar)

    return render(request, template, context)