import random

small = [chr(x) for x in range(65, 91)]
caps = [chr(x) for x in range(97, 123)]
nums = list(map(str, [x for x in range(10)]))
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','+','=','-','?','/','>','.','<']

length = int(input("What should be the length of your password: "))
combination = small + caps + nums + symbols
random.shuffle(combination)
password = random.sample(combination, length)

print("Here's a strong Password for you")
print(''.join(password))
