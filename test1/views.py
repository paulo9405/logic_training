from django.shortcuts import render, redirect
from test1.models import Double
from .forms import DoubleForm


def double(request):
    double = Double.objects.all()
    return render(request, 'double.html', {'double': double})


def new_double(request):
    form = DoubleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('double')

    return render(request, 'double.html', {'form': form})


def double2(request):
    if request.method == 'POST':
        data = request.POST.get('valueuser')
        double = int(data) * 2

    return render(request, 'double2.html', {'double': double})
