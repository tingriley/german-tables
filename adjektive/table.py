#!/usr/bin/python3
from prettytable import PrettyTable
wf = open("adjektive.html", "w", encoding='UTF-8')
wf.write("<html><head><link rel=\"stylesheet\" href=\"style.css\"></head><body>")


def create_table(filename, wf, name):
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

	wf.write(tmp)
	wf.write("<br>")
	rf.close()


create_table('indefinite.txt', wf, "Indefinite Article")
create_table('definite.txt', wf, "Definite Article")
create_table('no.txt', wf, "No Article")


wf.write("</body></html>")
wf.close()

