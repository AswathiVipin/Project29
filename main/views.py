from django.shortcuts import render
from .forms import StudentForm

def home(request):
    return render(request, "index.html")


def home1(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, "index1.html", {"form": form})
