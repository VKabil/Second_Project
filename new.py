jewels = "aAbbb"
stones = "aAAbbbbb"


count=0
for stone in stones:
    if stone in jewels:
        count +=1

print(count)