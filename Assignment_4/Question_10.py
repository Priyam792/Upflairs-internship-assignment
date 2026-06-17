# Write a program that reads numbers from a file and calculates:  
# ● Total  
# ● Average  
# ● Handle the case if the file does not exist.

#Solution -->
try : 
    numbers = []
    with open("numbers.txt" , "r") as f:
        for line in f:
            numbers.append(int((line.rstrip())))

        total = sum(numbers)
        average = total/len(numbers)
        print(f"Total : {total}")
        print(f"Average : {average}")

except FileNotFoundError:
    print("File not found !!")
except ValueError:
    print("File contains non-numeric data!")    