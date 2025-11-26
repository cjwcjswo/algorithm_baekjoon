word = input()

# KMP 알고리즘에 대해 숙지할 것.
word = word.replace("c=", 'a')
word = word.replace("c-", 'a')
word = word.replace("dz=", 'a')
word = word.replace("d-", 'a')
word = word.replace("lj", 'a')
word = word.replace("nj", 'a')
word = word.replace("s=", 'a')
word = word.replace("z=", 'a')

print(len(word))