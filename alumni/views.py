from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from alumni.forms import AlumniForm
from alumni.models import Alumni


# Create your views here.
def index(request):
    return render(
        request,
        "alumni/index.html",
        {"list_alumni": Alumni.objects.all()},
    )


def view_alumni(request, id):
    Alumni.objects.get(pk=id)
    return HttpResponseRedirect(reverse("index"))


def add_alumni(request):
    if request.method == "POST":
        form = AlumniForm(request.POST)
        if form.is_valid():
            new_alumni_number = form.cleaned_data["alumni_number"]
            new_first_name = form.cleaned_data["first_name"]
            new_last_name = form.cleaned_data["last_name"]
            new_email = form.cleaned_data["email"]
            new_field_of_study = form.cleaned_data["field_of_study"]
            new_gpa = form.cleaned_data["gpa"]

            new_alumni = Alumni(
                alumni_number=new_alumni_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa,
            )
            new_alumni.save()
            return render(
                request,
                "alumni/add.html",
                {"form": AlumniForm(), "success": True},
            )
    else:
        form = AlumniForm()
    return render(
        request,
        "alumni/add.html",
        {"form": AlumniForm()},
    )


def edit_alumni(request, id):
    if request.method == "POST":
        alumni = Alumni.objects.get(pk=id)
        form = AlumniForm(request.POST, instance=alumni)
        if form.is_valid():
            form.save()
            return render(
                request,
                "alumni/edit.html",
                {"form": form, "success": True},
            )
    else:
        alumni = Alumni.objects.get(pk=id)
        form = AlumniForm(instance=alumni)
    return render(
        request,
        "alumni/edit.html",
        {"form": form},
    )


def delete_alumni(request, id):
    if request.method == "POST":
        alumni = Alumni.objects.get(pk=id)
        alumni.delete()
    return HttpResponseRedirect(reverse("index"))
