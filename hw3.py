text = input("Please type anything:\n")

counter=dict()

for ch in text:
    if ch in counter:
        counter[ch]+=1
    else:
        counter[ch] = 1

for ch, count in counter.items():
    print('"',ch,'"', count )
    

