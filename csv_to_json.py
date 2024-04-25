import csv
import json


COLOUR_PALETTE = [
    '#292f36',
    '#ffb000',
    '#2bb6a8',
    '#648de5',
    '#dbcbd8',
    '#c9035f',
]

with open('precios_urbanizaciones_v.csv') as f:
    labels = list()
    dicty = dict()

    reader = csv.DictReader(f)
    for row in reader:
        labels.append(row.pop('Factura'))
        for index, k_v in enumerate(row.items()):
            key, value = k_v
            if key not in dicty:
                dicty[key] = {
                    'label': key,
                    'fill': False,
                    'borderColor': COLOUR_PALETTE[index],
                    'tension': 0.1,
                    'data': list()
                }
            dicty[key]['data'].append(row[key])

    datasets = [value for value in dicty.values()]
    data = {
        'labels': labels,
        'datasets': [value for value in dicty.values()]
    }

    with open('result.json', 'w') as jf:
        json.dump(data, jf, indent=4)
