# Write a program that generates a multiplication table (1–10) in matrix format using nested loops.

#Solution -->

for i in range(1,11):
    for j in range(1,11):
        print(i*j ,end="\t")
    print()