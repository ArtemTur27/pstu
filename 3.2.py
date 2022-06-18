def compare(S1, S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count = count + S2.count(ngram)
        
    return count/max(len(S1), len (S2))

Strings = '''Москва
Санкт-Петербург
Новосибирск
Екатеринбург
Нижний Новгород
Волгоград
Пермь
Красноярск
Воронеж'''.split('\n')

y = 'Пенза'

if __name__ == '__main__':
    for x in Strings:
        print(x, y, compare(x, y), compare (y, x))