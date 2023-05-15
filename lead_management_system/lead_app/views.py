from django.shortcuts import render

# Create your views here.
import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead, Mapping

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file')
        else:
            data = csv.reader(csv_file.read().decode('utf-8').splitlines())
            headers = next(data) # Get the headers row
            mapping_choices = [(field.db_field, field.db_field) for field in Lead._meta.fields]
            context = {'headers': headers, 'mapping_choices': mapping_choices}
            request.session['csv_data'] = [row for row in data] # Store the CSV data in session
            return render(request, 'lead_app/mapping.html', context)
    return render(request, 'lead_app/upload_csv.html')

def map_csv(request):
    if request.method == 'POST':
        chosen_fields = request.POST.getlist('mapping[]')
        csv_data = request.session.pop('csv_data') # Retrieve CSV data from session
        mapped_data = []
        for row in csv_data:
            mapped_row = {}
            for index, field in enumerate(chosen_fields):
                mapping = Mapping.objects.get(db_field=field)
                csv_index = headers.index(mapping.csv_header)
                mapped_row[field] = row[csv_index]
            mapped_data.append(mapped_row)
            lead = Lead(**mapped_row)
            lead.save()
        messages.success(request, 'CSV data imported successfully')
        return redirect('lead_app:lead_list')
    return redirect('lead_app:upload_csv')

def lead_list(request):
    leads = Lead.objects.all()
    context = {'leads': leads}
    return render(request, 'lead_app/lead_list.html', context)

from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer

class LeadList(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer