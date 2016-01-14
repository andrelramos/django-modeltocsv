from django.http import HttpResponse
import time
import csv

def modeltocsv(model=None, filename='', queryset=None, time_in_filename=True, exclude_fields=[]):
    '''
    Do csv file from a model and return HttpResponse with the same
    :param model: (django.db.models.base.ModelBase) The model
    :param filename: (str) Name of end file
    :param queryset: (django.db.models.query.QuerySet) Custom queryset
    :param time_in_filename: (bool) False to don't show timestamp in file name
    :param exclude_fields: (list) Fields that don't shown in end file
    :return: django.http.HttpResponse
    '''

    if not model:
        raise Exception("The model argument should not be blank")

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    if time_in_filename:
        contentDisposition = 'attachment; filename="%s-%s.csv"' % (filename, str(time.time()).replace('.', ''))
    else:
        contentDisposition = 'attachment; filename="%s.csv"' % (filename)
    response['Content-Disposition'] = contentDisposition

    # If queryset was passed
    if queryset:
        registers = queryset
    else:
        registers = model.objects.all()

    writer = csv.writer(response) # Write in http response

    # Write table titles
    headerRow = []
    for field in model._meta.fields:
            if field.name not in exclude_fields:
                headerRow.append(field.name.upper())
    writer.writerow(headerRow)

    # Write data
    for obj in registers:
        row = []
        for field in model._meta.fields: # Get model fields to get attrs
            if field.name not in exclude_fields:
                row.append(getattr(obj, field.name))
        writer.writerow(row)

    return response