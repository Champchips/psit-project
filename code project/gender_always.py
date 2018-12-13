import csv
import pygal
with open('database_for_alcohol.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    sample_list = []
    for line in csv_reader:
        sample_list.append(line)
    header = list(map(int, sample_list[0]))
    line_1 = list(map(float, sample_list[1]))
    line_2 = list(map(float, sample_list[2]))
    line_3 = list(map(float, sample_list[3]))
    for i in range(len(line_1)):
        if line_1[i] == 0:
            line_1[i] = None
    for i in range(len(line_2)):
        if line_2[i] == 0:
            line_2[i] = None
    for i in range(len(line_3)):
        if line_3[i] == 0:
            line_3[i] = None
chart = pygal.Bar(margin=50)
chart.x_labels = u'αβγδ'
chart.add('line 1', line_2)
chart.add('line 2', line_3)
chart.render('eiei.svg')