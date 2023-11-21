# import random
#
# ile_rzutow = int(input('Ile rzutow?' ))
#
# count = 0
# ileok = 0
#
# for i in range(1,ile_rzutow):
#     for j in range (1,3):
#         if random.randint(1,6) == 6:
#             count += 1
#     if count !=0:
#         #ileok += 1
#         prawdopodobienstwo = 100 * count / ile_rzutow
# print(f'prawdopodobienstwo wynosi: {prawdopodobienstwo}')
import random

# print(list(range(1, 11)))

# rzuć kostką 3 razy i sprawdź czy jest conajmniej 1 szóstka!
#total_rolls = 100000

# # flexowe rozwiązanie any + list comprehension
# success_count = 0
# for i in range(total_rolls):
#     success_count += any([random.randint(1, 6) == 6
#                           for _ in range(3)])
# count = 0
# ileok = 0

# for i in range(1000):
#     for j in range(3):
#         if random.randint(1, 6) == 6:
#             count += 1
#     if count != 0:
#        ileok += 1
#     count = 0
# prawdop = 100 * ileok / 1000
# print(f'Prawdopodobienstwo wynosi {prawdop}%.')

# znajdz pare w liscie ktorej suma wynosi 42
# a = [253, 12, -2, 53, 9, 234, 123, -94, 29, 7]
#
# for i in a:
#     for j in a:
#         if i + j == 21:
#             print(f'W liscie jest para ktorej suma wynosi 42 {i} oraz {j}')
#             break

# def collatz_step(n):
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = n * 3 + 1
#     return n
#
#
# def collatz_convergence(n):
#     collatz_path = [n]
#     while n != 1:
#         n = collatz_step(n)
#         collatz_path.append(n)
#     return collatz_path
#
#
# longest_path = 0
# winning_numbers = [1]
# for number in range(2, 101):
#     collatz_path = collatz_convergence(number)
#     collatz_steps_count = len(collatz_path) - 1
#     if collatz_steps_count > longest_path:
#         longest_path = collatz_steps_count
#         winning_numbers = [collatz_path[0]]
#     elif collatz_steps_count == longest_path:
#         winning_numbers.append(collatz_path[0])
#
#
# print(f"The highest amount of steps was: {longest_path} for numbers {winning_numbers}")

#a = 5
#b = 7.4
#c = 'mama'
#d_lista = [1, 2, 3, 5.5, 'mama', '54']

#print(a * d_lista[5])
#print(c[2])


#for i in range(3, 25, 4):
    #print(i)

#for i in range(100, -20, -10):
#    print(i)

# moj_string = 'to jest moj string'
#
# #print(moj_string[3:13:2])
# #print(moj_string[::-1])
# moj_string = moj_string.replace(' ', '')

#Sprawdz czy string jest palindromem
list_of_sentences = []
sentence = input('Podaj ciag znakow')
list_of_sentences.append(sentence)
max_len = len(sentence)
while True:
    print(f'Podano zdanie bedace palindromem')
    tmp_sentence = sentence.replace(' ', '').replace('.','').replace(',','')
    if tmp_sentence.lower == tmp_sentence[::-1].lower:
        print(f'zdanie jest palindromem')
    else:
        print(f'zdanie nei jest palindormem')
    break


# list_of_sentences = []
# sentence = input('Podaj wyrazenie: ')
# list_of_sentences.append(sentence)
# max_length = len(sentence)
# while True:
#     print(f'wprowadzono: {sentence}')
#     # sentence = sentence.replace(' ','')
#     # sentence = sentence.replace('.','')
#     # sentence = sentence.replace(',','')
#     # sentence = sentence.lower()
#     tmp_sentence = sentence.replace(' ','').replace('.','').replace(',','')
#     if tmp_sentence.lower() == tmp_sentence[::-1].lower():
#         print(f'tak, wyrazenie {sentence} jest palindromem')
#     else:
#         print(f'nie, to nie jest palindrom')
#     decision = input('Czy chcesz sprawdzic kolejne slowo? T/N')
#     if decision.lower() == 't':
#         sentence = input('Podaj kolejne wyrazenie: ')
#         list_of_sentences.append(sentence)
#         if len(sentence) > max_length:
#             max_length = len(sentence)
#     else:
#         break
#
# print(f'statystyki:')
# print(f'liczba sprawdzonych slow: {len(list_of_sentences)},\nnajdlusze ma: {max_length} znakow')
