V = int(input())
result = list(input())
if result.count("A") > result.count("B"):
    print("A")
elif result.count("A") == result.count("B"):
    print("Tie")
else:
    print("B")
