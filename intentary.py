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
else:    print("Grapes are out of stock!")
print("Number of items in inventory:", len(inventry))
print("Current inventory:")
for item in inventry:
    print("- " + item)