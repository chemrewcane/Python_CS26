import math

print(f"{"="*8} Probability Using Combinations {"="*8}")

total = int(input("Enter total number (e.g., 52): "))
select = int(input("Enter number to be selected (e.g., 5): "))
sp = int(input("Enter number of special/favorable items (e.g., 4 aces): "))
want = int(input("Enter wanted number (e.g., 2 aces): "))

total_final = math.comb(total, select)
special_final = math.comb(sp, want)
not_special = math.comb(total - sp, select - want)
fav = special_final * not_special
prob = fav / total_final

print(f"\n{"="*8} RESULT {"="*8}")

print("Total combinations:", total_final)
print("Probability:", round(prob, 6))