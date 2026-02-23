inventry=["kiwi","apple","banana","grapes"]
print(inventry)
inventry.append("orange")
print(inventry)
inventry.remove("banana")
print(inventry)
inventry[1]="pear"
print(inventry)
if "grapes" in inventry:
    print("Grapes are in stock!")