def all_varianfs(text):
     for i in range(len(text)):
        for j in range(i, len(text)):
            yield text[i:j + 1]

a = all_varianfs("abc")
for k in a:
    print(k)