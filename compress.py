def compress (text: list[str]) -> int:
    #Проверка на пустоту листа
    if not text:
        return 0

    char_counter=1
    new_len=0

    for x in range(1,len(text)):
        if text[x] == text [x-1]:
            char_counter += 1
        #нахдим равные последовательные элетенты
        else:
            text[new_len] = text[x-1]
            new_len += 1
            #Пишем сколько раз повторилась буква и обнуляем счетчик 
            if char_counter > 1:
                for digit in str(char_counter):
                    text[new_len] = digit
                    new_len += 1
            char_counter = 1

    #бубубубубубубу
    text[new_len] = text[len(text)-1]
    new_len += 1
    if char_counter > 1:
        for digit in str(char_counter):
            text[new_len] = digit
            new_len += 1
    return new_len

text = list('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
new_len = compress(text)

print(text[:new_len])

assert new_len == 20
assert text[:new_len] == list('A4B3C2XYZD4E3F3A6B28')

text = list('AAAA')
new_len = compress(text)

assert new_len == 2
assert text[:new_len] == list('A4')


text = list('')
new_len = compress(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list('A')
new_len = compress(text)

assert new_len == 1
assert text[:new_len] == list('A')

text = list('A4B3C2XYZD4E3F3A6B28')
new_len = compress(text)