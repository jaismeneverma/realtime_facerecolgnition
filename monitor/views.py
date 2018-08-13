from django.shortcuts import render
from monitor import data_reader

# Create your views here.


def search(request):
    name = request.GET.get('search')
    if not name:
        return render(request, 'search_bar.html')
    else:
        rows = data_reader.search_by_name(name)
        if rows:
            return render(request, 'search_bar.html', context={'rows': rows})
        else:
            return render(request, 'search_bar.html')
			
def search_by_status(request):
    rows = data_reader.search_by_status()
    print(rows)
    if rows:
        date = "12-5-1908"
        return render(request, 'search_bar.html', context={'rows': rows})
    else:
        return render(request, 'search_bar.html')
