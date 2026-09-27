import math

print(f"{"="*8} Probabilities via Combinatorics {"="*8}")

total = int(input("Enter total number: "))
select = int(input("Enter number to randomly pick: "))
look = int(input("Enter number of the type you're looking for: "))
want = int(input("Enter number of the type you want: "))

total_final = math.comb(total, select)
special_final = math.comb(look, want)
not_special = math.comb(total - look, select - want)
both = special_final * not_special
prob = both / total_final

print(f"\n{"="*8} RESULT {"="*8}")

print("Total combinations:", total_final)
print(f"Probability: {prob:.5f}")
