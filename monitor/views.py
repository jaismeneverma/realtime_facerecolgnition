from django.shortcuts import render
from monitor import data_reader
import datetime
# Create your views here.


def search(request):
    name = request.GET.get('search')
    if not name:
        return render(request, 'search.html')
    else:
        rows = data_reader.search_by_name(name)
        if rows:
            return render(request, 'search.html', context={'rows': rows})
        else:
            return render(request, 'search.html')


def search_by_status(request):
    rows = data_reader.search_by_status()
    print(rows)
    if rows:
        date = "12-5-1908"
        return render(request, 'search.html', context={'rows': rows})
    else:
        return render(request, 'search.html')


def search_by_date(request):
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')
    m_id = request.GET.get('id')
    if not m_id:
        return render(request, "view_by_date.html")
    if not to_date:
        to_date = str(datetime.date.today())
    dates, hours, in_out_details, total_hours = data_reader.get_in_time_between_dates(m_id, from_date, to_date)
    return render(request, "view_by_date.html", context={'rows': list(zip(dates, hours, in_out_details)),
                                                         'total_hours': total_hours})
