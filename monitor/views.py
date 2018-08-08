from django.shortcuts import render

# Create your views here.


def search(request):
    roll_no = request.GET.get('search')
    if not roll_no:
        return render(request, 'search_bar.html')
    else:
        status = "in"
        date = "12-5-1908"
        return render(request, 'search_bar.html', context={'status': status, 'roll_no': roll_no, 'date': date})
