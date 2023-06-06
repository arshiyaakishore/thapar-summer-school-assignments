#ques1
L= [11, 12, 13, 14]
print(L)
# (i) WAP to add 50 and 60 to L.
L.append(50)
L.append(60)
print(L)
# (ii) WAP to remove 11 and 13 from L.
L.remove(11)
print(L)
L.remove(13)
# (iii) WAP to sort L in ascending order.
L.sort
print(L)
# (iv) WAP to sort L in descending order.
L.reverse()
print(L)
# (v) WAP to search for 13 in L.
if 13 in L:
    print("Exists")
else:
    print("Not there")
# (vi) WAP to count the number of elements present in L.
print(len(L))
# (vii) WAP to sum all the elements in L.
print(sum(L))
# (viii) WAP to sum all ODD numbers in L.
odd_sum = sum(num for num in L if num % 2 != 0)
print(odd_sum)
# (ix) WAP to sum all EVEN numbers in L.
even_sum = sum(num for num in L if num % 2 == 0)
print(even_sum)
# (x) WAP to sum all PRIME numbers in L.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0

for n in L:
    if is_prime(n):
        prime_sum += n

print(prime_sum)


# (xi) WAP to clear all the elements in L.
L.clear
print(L)
# (xii) WAP to delete L.
del L


#ques2
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i) WAP to add new entry in D; key=8 and value is 8.8
D[8]=8.8
print(D)
# (ii) WAP to remove key=2.
del D[2]
print(D)
# (iii) WAP to check weather 6 key is present in D.
if 6 in D:
    print("Present")
else:
    print("Not")
# (iv) WAP to count the number of elements present in D.
print(len(D))
# (v) WAP to add all the values present D.
print(sum(D.values()))
# (vi) WAP to update the value of 3 to 7.1.
D[3]=7.1
print(D)
# (vii) WAP to clear the dictionary.
D.clear()


#ques3
S1= {10, 20, 30, 40, 50, 60}
S2= {40, 50, 60, 70, 80, 90}
# (i) WAP to add 55 and 66 in Set S1.
S1.add(55)
S1.add(66)
print(S1)
print(S2)
# (ii) WAP to remove 10 and 30 from Set S1.
S1.remove(10)
S1.remove(30)
print(S1)
print(S2)
# (iii) WAP to check whether 40 is present in S1.
if 40 in S1:
    print("Present")
else:
    print("Not present")
# (iv) WAP to find the union between S1 and S2.
print(S1.union(S2))
# (v) WAP to find the intersection between S1 and S2.
print(S1.intersection(S2))
# (vi) WAP to find the S1 - S2.
print((S1-S2))

#Ques 4
import random
# (i) WAP to print 100 random strings whose length between 6 and 8.
import string
for n in range(6,9):
    res = ''.join(random.choices(string.ascii_letters, k=n))
    print(str(res))

# (ii) WAP to print all prime numbers between 600 and 800.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

for num in range(600, 801):
    if is_prime(num):
        print(num)
    
# (iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9.
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num)


#ques5
# (i) Common numbers in the two lists
import random
list1 = random.sample(range(10, 31), 10)
list2 = random.sample(range(10, 31), 10)
print(list1)
print(list2)
common = list(set(list1) & set(list2))
print(common)
# (ii) Unique numbers in both the list
unique = list(set(list1) ^ set(list2))
print(unique)
# (iii) Minimum in both the list
min_no=min(min(list1), min(list2))
print(min_no)
# (iv) Maximum in both the list
maximum = max(max(list1), max(list2))
print(maximum)
# (v) Sum of both the lists
list_sum = sum(list1) + sum(list2)
print(list_sum)

#ques6 WAP to create a list of 100 random numbers between 100 and 900. Count and print the: 
import random

list1 = random.sample(range(100,901), 100)
list2 = random.sample(range(100,901), 100)
empty=[]
for num in range(100):
    empty.append(random.randint(100, 900))
# (i) All odd numbers
odd_numbers = [num for num in empty if num % 2 != 0]
print("Odd numbers:", odd_numbers)
print("Count:", len(odd_numbers))
# (ii) All even numbers
even_numbers=[num for num in empty if num%2==0]
print("Even numbers:", even_numbers)
print("Count:", len(even_numbers))
# (iii) All prime numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in empty if is_prime(num)]
print(prime_numbers)
print("count:", len(prime_numbers))

#ques7 
D={1:"One",2:"Two",3:"Three",4:"Four", 5:"Five"}
#open a file
with open("dictionary_data.txt", "w") as file:
    
    for key, value in D.items():
        file.write(f"{key}, {value}\n")

#ques8
L = ["One", "Two", "Three", "Four", "Five"]


with open("list_lengths.txt", "w") as file:
    
    for element in L:
        length = len(element)
        file.write(f"{element}, {length}\n")
        
#ques12
student_marks = {
    "Manan": [80, 85, 90, 95, 92],
    "Aditya": [75, 80, 85, 90, 88],
    "Aman": [90, 92, 88, 85, 95],
    "Alisha": [82, 86, 90, 88, 92],
    "Ravi": [88, 90, 92, 87, 84]
}

average_marks = {student: sum(marks) / len(marks) for student, marks in student_marks.items()}

max_student = max(average_marks, key=average_marks.get)
max_average = average_marks[max_student]

min_student = min(average_marks, key=average_marks.get)
min_average = average_marks[min_student]


print("Student with maximum average marks:")
print("Name:", max_student)
print("Average Marks:", max_average)
print("Student with minimum average marks:")
print("Name:", min_student)
print("Average Marks:", min_average)

