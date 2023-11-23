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