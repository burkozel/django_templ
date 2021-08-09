import csv
from django.shortcuts import render


def view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', 'r', encoding='utf-8') as m:
        csvreader = csv.reader(m, delimiter=';')
        info = {}
        # табличка
        for i, row in enumerate(csvreader):
            if i == 0:
                headers = [x for x in row]
            else:
                for j, values in enumerate(row):
                    if j == 0:
                        year = values
                        info.update({year: []})
                        # табличка
                    else:
                        if values:
                            info[year].append(float(values))
                        else:
                            info[year].append(values)
    context = {'headers':headers, 'contents':info}
    return render(request, template_name, context)

#view(request=r)