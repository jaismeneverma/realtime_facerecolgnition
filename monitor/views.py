from django.shortcuts import render
from monitor import data_reader

# Create your views here.


def search(request):
    name = request.GET.get('search')
    if not name:
        return render(request, 'search_bar.html')
    else:
        rows = data_reader.get_row(name)
        if rows:
            date = "12-5-1908"
            return render(request, 'search_bar.html', context={'rows': rows, 'date': date})
        else:
            return render(request, 'search_bar.html')
