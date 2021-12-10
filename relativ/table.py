#!/usr/bin/python3
import pdfkit
from prettytable import PrettyTable


outstring = "<html><head><meta charset=\"utf-8\"><link rel=\"stylesheet\" href=\"style.css\"></head><body>"



def create_table(filename, name):
	x = PrettyTable(["", "Masculine", "Feminine", "Neuter", "Plural"])
	lines = []
	with open(filename) as rf:
	    lines = rf.readlines()
	for line in lines:
		line = line.replace("\t", " ")
		line = line.replace("\n", "")
		line = line.split(",")
		x.add_row(line)


	html = x.get_html_string()
	tmp = html.replace("<table>", '')
	tmp = "<table><caption>"+ name + "</caption>" + tmp

	global outstring 
	outstring+= tmp 
	outstring += "<br>"


	rf.close()



create_table('relativ.txt', "relative pronoun")

css = 'style.css'
outstring += "</body></html>"
pdfkit.from_string(outstring, 'relativ.pdf', css = css)
try:
	pdfkit.from_string(outstring, 'relativ.pdf', css = css)
except:
	pass