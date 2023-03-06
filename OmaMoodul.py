def fix_словарь(word, est_words, rus_words):
    if word in est_words:
        index = est_words.index(word)
        new_rus_word = input('Введите новый перевод слова на русский: ')
        rus_words[index] = new_rus_word
        Kirjuta_failisse('rus.txt', rus_words)
    elif word in rus_words:
        index = rus_words.index(word)
        new_est_word = input('Введите новый перевод слова на эстонский: ')
        est_words[index] = new_est_word
        Kirjuta_failisse('est.txt', est_words)
    else:
        print("Слово не найдено")



# функция для добавления нового слова в словарь
def add_word(word, est_words, rus_words):
    if word not in est_words:
        est_words.append(word)
        rus_word = input('Введите перевод слова на русский: ')
        rus_words.append(rus_word)
        Kirjuta_failisse('est.txt', est_words)
        Kirjuta_failisse('rus.txt', rus_words)





# функция для перевода слов с русского на эстонский
def rus_na_est(word, est_words, rus_words):
    if word in rus_words:
        index = rus_words.index(word)
        return est_words[index]
    else:
        return None
# функция для перевода слов с эстонского на русский
def est_na_rus(word, est_words, rus_words):
    if word in est_words:
        index = est_words.index(word)
        return rus_words[index]
    else:
        return None











# функция для записи слов в файл
def Kirjuta_failisse(fail:str,jarjend:list):
    f = open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

# функция для чтения слов из файла
def Loe_failist(fail:str) -> list:
    f = open(fail,'r',encoding="utf-8-sig")
    jarjend = []
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
