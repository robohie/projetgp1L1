from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .models import Student

PROMO = (("PREPO", "prépo"), ("L1", "l1"), ("L2", "l2"), ("L3", "l3"))


class Welcome(forms.Form):
    nom = forms.CharField(max_length=25)
    postnom = forms.CharField(max_length=25)
    matricule = forms.CharField(max_length=15)
    promo = forms.ChoiceField(choices=PROMO)


# Create your views here.
def welcome(request):
    if request.method == "POST":
        form = Welcome(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                Student.objects.get(nom=data["nom"], matricule=data["matricule"],
                                    promo=data["promo"])
            except Student.DoesNotExist:
                return HttpResponse("ERROR")

            return redirect("assess", data["nom"], data["matricule"])
    else:
        form = Welcome()

    return render(request, "access/access.html", {"form": form})
