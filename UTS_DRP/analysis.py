import csv

def isIdentical(list):
    if list.count(list[0]) == len(list):
        return True
    else:
        return False

def findMax(list):
    index = 0
    max = list[index]
    for x in range(1, len(list)):
        if list[x] > max:
            max = list[x]
            index = x

    return index+1

list_setuju = [
    "krisis ekonomi", "resesi", "krisis ekonomi 2023"
]
list_berani = [
    "optimis", "berani", "solusi", "antisipasi", "keberanian", "siap", "mantap"
]
list_takut = [
    "ngeri", "takut", "seram", "serem", "resah", "khawatir", "cemas", "bimbang", "ragu", "ketakutan",
    "ditakuttakuti", "gelisah", "panik"
]
list_tidak_setuju = [
    "tidak", "nggak", "tak", "bukan"
]

list_kata = [list_setuju, list_tidak_setuju, list_berani, list_takut]

result = open("hasil_analisis.csv", "w", encoding="utf-8", newline="")
source = open("hasil_pre.csv", "r", encoding="utf-8", newline="")

resW = csv.writer(result)
srcR = csv.reader(source)
header = next(srcR) # untuk memajukan satu baris (tidak menghitung header)
resW.writerow(header)

for x in srcR:
    tweet = x[1]
    tendensi = x[2]
    score = [0,0,0,0]

    for y in range(len(list_kata)):
        for z in range(len(list_kata[y])):
            if list_kata[y][z] in tweet:
                score[y] += tweet.count(list_kata[y][z])

    flag = isIdentical(score)

    writing = [x[0], tweet]
    if flag:
        writing.append(5)
    else:
        writing.append(findMax(score))

    resW.writerow(writing)

result.close()
source.close()

with open("final.csv","w",encoding="utf-8") as final:
    source =  open("hasil_analisis.csv", "r", encoding="utf-8", newline="")
    sR = csv.reader(source)
    next(sR)
    fW = csv.writer(final)

    header = ["No.", "Kategori", "Jumlah"]
    fW.writerow(header)

    final = [0,0,0,0,0]

    for x in sR:
        tendensi = x[2]
        if tendensi == '1':
            final[0] += 1
        elif tendensi == '2':
            final[1] += 1
        elif tendensi == '3':
            final[2] += 1
        elif tendensi == '4':
            final[3] += 1
        elif tendensi == '5':
            final[4] += 1
    
    print(final)

    for x in range(1,6):
        if x == 1:
            content = [1,"Setuju",final[0]]
            fW.writerow(content)
        if x == 2:
            content = [2,"Tidak Setuju", final[1]]
            fW.writerow(content)
        if x == 3:
            content = [3,"Berani", final[2]]
            fW.writerow(content)
        if x == 4:
            content = [4,"Takut", final[3]]
            fW.writerow(content)
        if x == 5:
            content = [5,"Netral", final[4]]
            fW.writerow(content)