with open('./test.txt', 'w+', encoding='utf-8') as fp:
    fp.write('aaa')
    fp.close()
with open('./home.txt', 'w+', encoding='utf-8') as fp:
    fp.write('aaa')
    fp.close()
print("ok")