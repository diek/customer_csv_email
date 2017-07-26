# exporter/views.py

import csv
import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Customers

from .forms import ReportForm

# From Big Nige, @djangobook.com, some experimentation
def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def report(request):
    shifts = []
    form = ReportForm(request.GET or None)
    customers = Customers.objects.order_by('last_name')
    if form.is_valid():
        if form.cleaned_data['download_as_csv']:
            # generate CSV - use current datetime for filename
            current_date = datetime.datetime.now()
            timestamp = current_date.strftime('%Y-%m-%d %H%M')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=Report {}.csv'.format(timestamp)

            # Create the CSV writer using the HttpResponse as the "file."
            writer = csv.writer(response)
            writer.writerow(['Date', 'Name', 'Job', 'Duration'])
            for shift in shifts:
                writer.writerow([shift.date, shift.employee, shift.job, shift.duration])

            return response

    return render(request, 'exporter/report.html', {
        'form': form,
        'customers': customers,
        'container_class': 'container-fluid',
    })
