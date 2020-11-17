import tkinter as tk
import PySimpleGUI as sg
import requests
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, legal, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, KeepTogether, Spacer, PageBreak, Table, TableStyle 
from reportlab.lib.styles import getSampleStyleSheet

import csv
import os


#view deo
sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Izeberi csv fajl: "), sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Text("Naziv pdf fajla: "), sg.Input(key='-IN2-')], [sg.Button("Submit")]]

###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))

path = ""
name = ""

while True:
    event, values = window.read()
    path = values["-IN-"]
    name = values["-IN2-"]

    #biznis logika

    # Get de work directory 
    cwd = os.getcwd() 

    # Introduction text
    line1 = 'Ovde treba da ide neki tekst'
    line2 = 'koji će klijent da precizira'
    line3 = 'prva verzija koda 16.11.2020. godine'
    line4 = 'jos teksta'
    line5 = 'jos teksta'
    line6 = 'jos teksta'

    # File that must be written to report
    with open (path, 'r', encoding = 'utf-8') as csvfile:
        data = list(csv.reader(csvfile))

    print(data)
    elements = []

    # PDF Text
    # PDF Text - Styles
    styles = getSampleStyleSheet()
    styleNormal = styles['Normal']

    elements.append(Paragraph(line1, styleNormal))
    elements.append(Paragraph(line2, styleNormal))
    elements.append(Paragraph(line3, styleNormal))
    elements.append(Spacer(inch, .25 * inch))
    elements.append(Paragraph(line4, styleNormal))
    elements.append(Paragraph(line5, styleNormal))
    elements.append(Paragraph(line6, styleNormal))
    elements.append(Spacer(inch, .25 * inch))

    # PDF Table
    # PDF Table - Styles
    # [(start_column, start_row), (end_column, end_row)]
    all_cells = [(0, 0), (-1, -1)]
    header = [(0, 0), (-1, 0)]
    column0 = [(0, 0), (0, -1)]
    column1 = [(1, 0), (1, -1)]
    column2 = [(2, 0), (2, -1)]
    column3 = [(3, 0), (3, -1)]
    column4 = [(4, 0), (4, -1)]
    column5 = [(5, 0), (5, -1)]
    column6 = [(6, 0), (6, -1)]
    column7 = [(7, 0), (7, -1)]
    column8 = [(8, 0), (8, -1)]
    column9 = [(9, 0), (9, -1)]
    column10 = [(10, 0), (10, -1)]
    column11 = [(11, 0), (11, -1)]
    column12 = [(12, 0), (12, -1)]
    column13 = [(13, 0), (13, -1)]
    column14 = [(14, 0), (14, -1)]
    column15 = [(15, 0), (15, -1)]
    column16 = [(16, 0), (16, -1)]
    column17 = [(17, 0), (17, -1)]
    column18 = [(18, 0), (18, -1)]
    column19 = [(19, 0), (19, -1)]
    column20 = [(20, 0), (20, -1)]
    column21 = [(21, 0), (21, -1)]
    column22 = [(22, 0), (22, -1)]
    #column23 = [(23, 0), (23, -1)]

    table_style = TableStyle([
        ('VALIGN', all_cells[0], all_cells[1], 'TOP'),
        ('LINEBELOW', header[0], header[1], 1, colors.black),
        ('ALIGN', column0[0], column0[1], 'LEFT'),
        ('ALIGN', column1[0], column1[1], 'LEFT'),
        ('ALIGN', column2[0], column2[1], 'LEFT'),
        ('ALIGN', column3[0], column3[1], 'RIGHT'),
        ('ALIGN', column4[0], column4[1], 'RIGHT'),
        ('ALIGN', column5[0], column5[1], 'LEFT'),
        ('ALIGN', column6[0], column6[1], 'RIGHT'),
        ('ALIGN', column7[0], column7[1], 'RIGHT'),
        ('ALIGN', column8[0], column8[1], 'RIGHT'),
        ('ALIGN', column9[0], column9[1], 'RIGHT'),
        ('ALIGN', column10[0], column10[1], 'RIGHT'),
        ('ALIGN', column11[0], column11[1], 'RIGHT'),
        ('ALIGN', column12[0], column12[1], 'RIGHT'),
        ('ALIGN', column13[0], column13[1], 'RIGHT'),
        ('ALIGN', column14[0], column14[1], 'RIGHT'),
        ('ALIGN', column15[0], column15[1], 'RIGHT'),
        ('ALIGN', column16[0], column16[1], 'RIGHT'),
        ('ALIGN', column17[0], column17[1], 'RIGHT'),
        ('ALIGN', column18[0], column18[1], 'RIGHT'),
        ('ALIGN', column19[0], column19[1], 'RIGHT'),
        ('ALIGN', column20[0], column20[1], 'RIGHT'),
        ('ALIGN', column21[0], column21[1], 'RIGHT'),
        ('ALIGN', column22[0], column22[1], 'RIGHT'),
        #('ALIGN', column23[0], column23[1], 'RIGHT'),
    ])

    # PDF Table - Column Widths
    colWidths = [
        0.7 * inch,  # Column 0
        3.1 * inch,  # Column 1
        3.7 * inch,  # Column 2
        1.2 * inch,  # Column 3
        4.5 * inch,  # Column 4
        3 * inch,  # Column 5
        2 * inch,  # Column 6
        2 * inch,  # Column 7
        2 * inch,  # Column 8
        2 * inch,  # Column 9
        2 * inch,  # Column 10
        2 * inch,  # Column 11
        2 * inch,  # Column 12
        2 * inch,  # Column 13
        2 * inch,  # Column 14
        2 * inch,  # Column 15
        2 * inch,  # Column 16
        2 * inch,  # Column 17
        2 * inch,  # Column 18
        2 * inch,  # Column 19
        2 * inch,  # Column 20
        2 * inch,  # Column 21
        2 * inch,  # Column 22
        #2 * inch,  # Column 23
    ]

    # PDF Table - Strip '[]() and add word wrap to column 5
    for index, row in enumerate(data):
        for col, val in enumerate(row):
            """ if col != 5 or index == 0:
                data[index][col] = val.strip("'[]()")
            else: """
            print("col ", col)
            print("val ", val)
            data[index][col] = Paragraph(val, styles['Normal'])

    # Add table to elements
    t = Table(data, colWidths=colWidths)
    t.setStyle(table_style)
    elements.append(t)

    # Generate PDF
    archivo_pdf = SimpleDocTemplate(
        name,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=28)

    if event == sg.WIN_CLOSED:
            break
    elif event == "Submit":
        archivo_pdf.build(elements)
        #print(values["-IN-"])