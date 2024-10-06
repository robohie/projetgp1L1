from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Teachers
from Access.models import Student


class Bulletin(forms.Form):
    la_liste = [(x, x.nom) for x in Teachers.objects.order_by("promo")]
    choix1 = forms.ChoiceField(choices=la_liste, label="N°1")
    choix2 = forms.ChoiceField(choices=la_liste, label="N°2")
    choix3 = forms.ChoiceField(choices=la_liste, label="N°3")
    choix4 = forms.ChoiceField(choices=la_liste, label="N°4")
    choix5 = forms.ChoiceField(choices=la_liste, label="N°5")


# Create your views here.
def show(request, nom, matr):
    student = Student.objects.get(nom=nom, matricule=matr)
    if request.method == "POST":
        form = Bulletin(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            if student.state:
                return HttpResponse(f"<h1>{student.nom}, vous avez déjà voté!!!</h1>")

            choix1 = data["choix1"]
            choix2 = data["choix2"]
            choix3 = data["choix3"]
            choix4 = data["choix4"]
            choix5 = data["choix5"]

            longueur1 = len((choix5, choix4, choix3, choix2, choix1))
            longueur2 = len(list({choix1, choix2, choix3, choix4, choix5}))
            if not longueur1 == longueur2:
                return HttpResponse("<h1>Aucune répétition n'est permise!</h1>")

            choix1 = Teachers.objects.get(nom=choix1.split(' ')[0])
            choix2 = Teachers.objects.get(nom=choix2.split(' ')[0])
            choix3 = Teachers.objects.get(nom=choix3.split(' ')[0])
            choix4 = Teachers.objects.get(nom=choix4.split(' ')[0])
            choix5 = Teachers.objects.get(nom=choix5.split(' ')[0])

            for choix in (choix5, choix4, choix3, choix2, choix1):
                if not choix.promo == student.promo:
                    return HttpResponse(f"<h1>{choix.nom} n'enseigne pas en {choix.promo}</h1>")

            choix1.point += 5
            choix2.point += 4
            choix3.point += 3
            choix4.point += 2
            choix5.point += 1

            choix1.save()
            choix2.save()
            choix3.save()
            choix4.save()
            choix5.save()

            student.state = 1
            student.save()

            return HttpResponse("Success")
    else:
        form = Bulletin()
    return render(request, "assess/assess.html",
                  {"form": form, "promo": student.promo})


def ranking(request, promo):
    places = [0,]
    noms = []
    postnoms = []
    points = []
    get_teachers = Teachers.objects.filter(promo=promo)
    for prof in get_teachers.order_by("-point"):
        if len(noms) != 5:
            places.append(places[-1] + 1)
            noms.append(prof.nom)
            postnoms.append(prof.postnom)
            points.append(prof.point)
    places.pop(0)
    return render(request, "assess/classement.html",
                  {"info": zip(places, noms, postnoms, points)})
