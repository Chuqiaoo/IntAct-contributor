__author__ = 'chuqiao'


txt_file = r"full-intact.txt"
csv_file = r"full.csv"


in_txt = csv.reader(open(txt_file, "r"), delimiter='\t')
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)