print("""Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.""")
user_input = input()
print(f"""What a great name you have, {user_input}!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")
remainder3, remainder5, remainder7 = [int(input()) for i in range(3)]
user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {user_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
user_counting_input = int(input())

for i in range(user_counting_input + 1):
    print(f"{i} !")

print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

user_answer_choice = int(input())

while user_answer_choice != 2:
    print("Please, try again.")
    user_answer_choice = int(input())

print("""Completed, have a nice day!
Congratulations, have a nice day!""")

