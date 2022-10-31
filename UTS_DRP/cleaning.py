from string import punctuation
import csv
import re
import string

def case_folding(reader):
    res = []
    next(reader)
    for x in reader:
        res.append(x[1].lower())
    return res

def cleaning(file):
    res = []
    for x in file:
        # menghilangkan newline dan diganti dengan space
        pattern1 = re.compile(r'\s+')
        str_no_space = pattern1.sub(' ', x)
        str_no_space += " "

        # menghilangkan URL, string berawalan @ dan #
        pattern2 = re.compile(r'https:(.*?\s+)|(#.*?\s+)|(@.*?\s+)')
        str_clean = pattern2.sub('', str_no_space)

        # menghilangkan angka
        pattern3 = re.compile(r'\s*\d+\s*')
        str_no_num = pattern3.sub(' ', str_clean)

        # menghilangkan tanda baca, mengambil data tanda baca dari string.punctuation
        punctuation = str_no_num.maketrans('', '', string.punctuation)
        str_no_punc = str_no_num.translate(punctuation)

        res.append(str_no_punc.strip())

    return res

with open("snscrape.csv", "r", encoding="utf-8") as readfile:
    reader = csv.reader(readfile)
    res = None

    # CASE FOLDING
    res = case_folding(reader)

    # MENGHILANGKAN URL, TAGAR, DAN TAG
    res = cleaning(res)

with open("snscrape.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)

    output = open("hasil_pre.csv", "w", encoding="utf-8", newline="")
    w = csv.writer(output)

    header = ["No.","Tweets","Tendensi"]
    w.writerow(header)
    
    y = 0
    for x in r:
        content = [x[0], res[y], x[2]]
        w.writerow(content)
        y+=1

    output.close()