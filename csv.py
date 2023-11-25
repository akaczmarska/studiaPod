with open('C:\\Users\\akaczmarska\\Desktop\\Moj_folder\\rozliczenie.csv', 'r') as plik1: # read czyta caly plik
  # #  content = plik1.read(5)
  #   print(content)
  #   content = plik1.read(5)
  #   # metoda read wrzuca wszystko do jednego stringa, metoda readlines wyswietla liste stringow, readlines przeczyta wszystko
  #   content = plik1.read(5)  # przeczyta piec znakow; pierwszych badz kolejnych
  #   print(content)
  #   for line in range(10):
  #       content = plik1.readline()
  #       print(content)
    content = plik1.readlines()
print(content)

# przygotowanie danych
for i in range(len(content)):
  content[i] = content[i].split(',')
print(content)

# #obliczanie sredniej wyplaty
# total = 0
# for line in content[1:]:
#   total += int(line[1])
# print(f'srednia {round(total/len(content)-1,2)}')

#obliczanie ilosci kobiet na macierzynskim
kobiety_na_macierzyskim = 0
for line in content[1:]:
  if line[4][0].lower() == 't' and line[3].lower() == 'k':
    kobiety_na_macierzyskim += 1
print(f'Liczba kobiet na macierzynskim wynosi{kobiety_na_macierzyskim}')
#if line[4][0].lower() == 't' and line[3].lower() == 'k' --mozna napisac \n czyli znak nowej lini
    #lib mozemy to obejsc line.[4][0]