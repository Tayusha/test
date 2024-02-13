"""
fin = open("students.csv", "r", encoding = "utf-8")
title = fin.readline()
print(title)
students = [x.strip().split(",") for x in fin]
fin.close
bal_sum = {} #bal_sum{key - класс, value - сумма оценок}
bal_cnt = {} #bal_cnt{key - класс, value - кол-во оценок}

#x[0] - порядковый номер
#x[1] - ФИО
#x[2] - № проекта
#x[3] - класс
#x[4] - оценка


for x in students:
    if x[4] != "None":
        if x[3] in bal_sum:
            bal_sum[x[3]] += int(x[4])
            bal_cnt[x[3]] += 1
        else:
            bal_sum[x[3]] = int(x[4])
            bal_cnt[x[3]] = 1
    fio = x[1].split()
    if fio[0] == "Хадаров" and fio[1] == "Владимир":
        print(f'Ты получил: {x[4]}, за проект - {x[2]}')

for x in students:
    if x[4] == "None":
        x[4] = f'{bal_sum[x[3]]/bal_cnt[x[3]]:.3f}'
for x in students:
    print(x)

fout = open("students_new.csv", "w", encoding = "utf-8")
fout.write(title)
for x in students:
    s = ",".join(x) + "\n"
    fout.write(s)
fout.close



fin = open("students.csv", "r", encoding = "utf-8")
title = fin.readline()
print(title)
students = [x.strip().split(",") for x in fin]
fin.close()
for i in range(1, len(students)):
    for j in range(i, 0, -1):
        if students[j][4] < students[j-1][4]:
            students[j], students[j-1] = students[j-1], students[j]
        else:
            break
cnt = 0
for x in students:
    if "10" in x[3] and x[4] == "5":
        cnt+=1
        fio = x[1].split()
        print(f"{cnt} место: {fio[1][0]}. {fio[0]}")
        if cnt == 3:
            break


fin = open("students.csv", "r", encoding = "utf-8")
title = fin.readline()
students = [x.strip().split(",") for x in fin]
fin.close()
while True:
    N = input("Введите № проекта:")
    if N == "СТОП":
        break
    for x in students:
        fio = x[1].split()
        if x[2] == N:
            print(f'Проект № {x[2]} делал {fio[1][0]}. {fio[0]} он(а) получил(а) оценку {x[4]}.')
            break
    else:
            print("Ничего не найдено")

from random import choice
fin = open("students.csv", "r", encoding = "utf-8")
title = fin.readline().strip()
students = [x.strip() for x in fin]
fin.close()
simbol = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
for i in range(len(students)):
    x = students[i].split(",")
    fio = x[1].split()
    log = fio[0] + "_" + fio[1][0] + fio[2][0]
    pasw = ""
    for _ in range(8):
        pasw += choice(simbol)
    students[i] = students[i] + "," + log + "," + pasw
fout = open("students_password.csv", "w", encoding = "utf-8")
fout.write(title+ ", log, password\n")
for x in students:
    s = x +  "\n"
    fout.write(s)
fout.close

#5
def hash_(s):
    #hash_(s) - создаёт хэш по строке
    #входные параметры: str - строка данных
    #выходные параметры: hash_name - hash - строка
    p = 67
    m = 10**9 + 9
    alfabeth = "йцукенгшщзхъфывапролджэячсмитьбюё ЙЦУКЕНГШЩЗХФВАПРОЛДЖЭЯЧСМИТБЮЁ"
    d = {}
    for ind, simbol in enumerate(alfabeth, 1): #создали словарь символов
        d[simbol] = ind
    hashname = 0
    for i in range(len(s)):
        hashname = d[s[i]]*p**i
    return hashname % m

fin = open("students.csv", "r", encoding = "utf - 8")
title = fin.readline()
students = [x.strip().split(",") for x in fin]
fin.close()
fout = open("students_with_hash.csv", 'w', encoding = "utf-8")
fout.write(title)
for x in students:
    s = str(hash_(x[1])) + ", " + x[1] + ", " + x[2]   + ", " + x[3]   + ", " + x[4]  + "\n"
    fout.write(s)
    print(s)
fout.close()
"""
    
#6
    
    

