# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = 'Напишите программу, удаляющую изабв текабвста все ненужные слова абв'


def del_words(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return ' '.join(txt)


txt = del_words(txt)
print(txt)
