# Name:
# Period:

# ============================================================
# Python Skills Check — LISTS & LOOPS
# CHALLENGE VERSION — 40 TASKS
# ============================================================
# DIRECTIONS:
# - Create a repository, clone it, and add this file.
# - Complete each task UNDER its directions.
# - Do not delete the directions.
# - Use ONLY concepts learned in class, except for 'in' and 'not in'.
#   You must research these two new operators independently in Section 5.
# - Use the EXACT variable and function names provided.
# - The entire file must run without errors.
# - Do not hard-code results Python should calculate.
# - Unless a task says otherwise, do NOT use sum(), min(), max(),
#   sorted(), sort(), list comprehensions, sets, or dictionaries.
# - For functions, RETURN values when instructed; do not just print.
# - Test edge cases and change the starting values to check your logic.
# - Tasks that ask for input() may be tested individually.

# ============================================================
# SECTION 1 — LIST FUNDAMENTALS (TASKS 1–6)
# ============================================================

# TASK 1:
# Create a list named scores containing 85, 92, 78, 96, 88.
# Print the entire list and its length using len().
scores = [85, 92, 78, 96, 88]
lengthScores = len(scores)
print(scores, "length:", lengthScores)

# TASK 2:
# Using scores from Task 1, print the FIRST, THIRD, and LAST
# elements on separate lines. Use indexes, not hard-coded values.
First = scores[0]
Third = scores[2]
Last = scores[len(scores) - 1]
print(First)
print(Third)
print(Last)

# TASK 3:
# Change the third element of scores to 100.
# Print the updated list. Do not create a replacement list.
scores[2] = 100
print(scores)

# TASK 4:
# Create games = ["Minecraft", "Roblox", "Fortnite"].
# Append "Valorant" and insert "Rocket League" at index 1.
# Print games. Check the order carefully.
games = ["Minecraft", "Roblox", "Fortnite"]
games.append("Valorant")
games.insert(1, "Rocket League")
print(games)

# TASK 5:
# Using games from Task 4, remove "Roblox" with remove().
# Then pop the FIRST item into a variable named removed_game.
# Print removed_game and the remaining games list.
games.remove("Roblox")
removedGame = games.pop(0)
print("Removed:", removedGame)
print(games)

# TASK 6:
# Create colors = ["red", "blue", "green", "yellow", "purple"].
# Store the index of "green" in green_index using index().
# Print green_index. Then replace "yellow" with "orange".
# Print the new list.
colors = ["red", "blue", "green", "yellow", "purple"]
greenIndex = colors.index("green")
print(greenIndex)
yellowIdx = colors.index("yellow")
colors[yellowIdx] = "orange"
print(colors)

# ============================================================
# SECTION 2 — FOR LOOPS & RANGE (TASKS 7–12)
# ============================================================

# TASK 7:
# Use a for loop with range() to print numbers 1 through 20,
# INCLUDING 20. Do not manually print the numbers.
print()
for i in range(1, 21):
    print(i)


# TASK 8:
# Use a for loop with range() to print 30, 27, 24, ... 0.
# IMPORTANT: The zero must be included.
print()
for i in range(30, -1, -1):
    print(i)

# TASK 9:
# Use a for loop to print all EVEN numbers from 1 to 50.
# You MUST use an if statement and the % operator inside the loop.
print()
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# TASK 10:
# Create number = 7.
# Print its multiplication table from 1 through 12 using a for loop.
# Example line: 7 x 3 = 21
# Your code must also work if number changes.
print()
number = 7
for i in range(1, 13):
    print(i * number)

# TASK 11:
# Create students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"].
# Use a for loop to print "Student: " followed by each name.
# Do NOT write five separate print statements.
students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
for name in students:
    print("Student:", name)

# TASK 12:
# Using students, print a NUMBERED roster:
# 1. Alex
# 2. Jordan
# ...
# 5. Casey
# Use range(len(students)) OR enumerate().
for i in range(len(students)):
    print(str(i + 1) + ".", students[i])

# ============================================================
# SECTION 3 — WHILE LOOPS & VALIDATION (TASKS 13–18)
# ============================================================

# TASK 13:
# Create countdown = 10.
# Use a while loop to print from countdown down to 0.
# Then print "Blast off!". Avoid an infinite loop.
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    if countdown == 0:
        print(countdown)
        print("Blast off!")
        break

#test
# TASK 14:
# Create password = "Python123".
# Keep asking the user for a password until it matches.
# Print "Access granted" exactly once after a correct entry.
password = "Python123"
inputPwd = ""
while inputPwd != "Python123":
    inputPwd = input("Please Enter Password: ")
    if inputPwd == "Python123":
        print("Access granted")

# TASK 15:
# Ask the user for an integer between 1 and 10 INCLUSIVE.
# Keep asking while the value is invalid.
# After a valid entry, print "Valid number".
# Test 0, 1, 10, and 11.
inputNum = "12"
while not 10 >= int(inputNum) >= 1:
    inputNum = input("Enter integer between 1 and 10: ")
    if 10 >= int(inputNum) >= 1:
        print("Valid Number")

# TASK 16:
# Create total = 0.
# Repeatedly ask for an integer. Add each nonzero entry to total.
# Stop when the user enters 0, then print total.
# Example inputs: 5, 8, -2, 0 -> Total: 11.
total = 0
inputInt = "20"
while int(inputInt) != 0:
    inputInt = input("Enter integer: ")
    total += int(inputInt)
    if int(inputInt) == 0:
        print(total)

# TASK 17:
# Create secret = "robot" and attempts = 3.
# Ask the user to guess secret, allowing AT MOST 3 guesses.
# Print "Correct" if guessed in time; otherwise "Out of attempts".
# Make sure a correct guess does NOT print both messages.
secret = "robot"
attempts = 3
while attempts > 0:
    print("Attempts:", attempts)
    guess = input("Guess the secret: ")
    if guess == "robot":
        print("Correct!")
        break
    else:
        attempts -= 1
    if attempts == 0:
        print("Out of attempts:(")


# TASK 18:
# Make a while-loop menu:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit
# Repeat until the user enters 3. Handle invalid choices.
# Print "Goodbye" only when option 2 is selected.
start = True
while start:
    print("1. Say Hello\n2. Say Goodbye\n3. Exit")
    choice0 = input("Enter # of choice: ")
    while "2" != choice0 != "1" and choice0 != "3":
        choice0 = input("Please Enter Valid #: ")
    if choice0 == "1":
        print("Hello")
        print("\n\n\n\n\n")
    elif choice0 == "2":
        print("Goodbye")
        print("\n\n\n\n\n")
    elif choice0 == "3":
        print("\n\n\n\n\n\n\n\n\n")
        break

# ============================================================
# SECTION 4 — PROCESSING LISTS WITH LOOPS (TASKS 19–24)
# ============================================================

# TASK 19:
# Create numbers = [4, 8, 15, 16, 23, 42].
# Use a for loop to calculate and print their total.
# Do NOT use sum().
numbers = [4, 8, 15, 16, 23, 42]
numbersTot = 0
for num in numbers:
    numbersTot += num
print(numbersTot)

# TASK 20:
# Create grades = [90, 85, 78, 92, 88].
# Use a loop and len() to calculate the average.
# Print the average. Do NOT use sum().
grades = [90, 85, 78, 92, 88]
totGrades = 0
for i in grades:
    totGrades += i
avgGrades = totGrades / len(grades)
print(avgGrades)

# TASK 21:
# Create numbers = [3, 8, 12, 7, 15, 20, 24, 9].
# Use ONE loop to count even and odd values separately.
# Print "Even: [count]" and "Odd: [count]".
numbers = [3, 8, 12, 7, 15, 20, 24, 9]
evenCnt = 0
oddCnt = 0
for num in numbers:
    if num % 2 == 0:
        evenCnt += 1
    else:
        oddCnt += 1
print("Even:", evenCnt)
print("Odd:", oddCnt)

# TASK 22:
# Create numbers = [-14, -67, -23, -89, -45].
# Use a loop to find and print the HIGHEST number.
# Do NOT use max() or sorting.
# IMPORTANT: Starting your answer at 0 gives a wrong result.
numbers = [-14, -67, -23, -89, -45]
highestNum = -100
for num in numbers:
    if num >= highestNum:
        highestNum = num
print(highestNum)

# TASK 23:
# Create numbers = [14, 67, 23, 89, 45, 12].
# Use a loop to find and print the LOWEST number.
# Do NOT use min() or sorting.
# Your logic must also work with all-negative numbers.
numbers = [14, 67, 23, 89, 45, 12]
lowestNum = 100
for num in numbers:
    if num <= lowestNum:
        lowestNum = num
print(lowestNum)

# TASK 24:
# Create numbers = [5, 2, 5, 8, 5, 3, 2, 5].
# Create target = 5.
# Use a loop to count how often target appears; print the count.
# Do NOT use count(). It must work if target changes.
numbers = [5, 2, 5, 8, 5, 3, 2, 5]
target = 5
targetCnt = 0
for num in numbers:
    if num == target:
        targetCnt += 1
print("Count:", targetCnt)

# ============================================================
# SECTION 5 — IN / NOT IN (TASKS 25–30)
# ============================================================
# INDEPENDENT RESEARCH REQUIRED:
# We have NOT covered 'in' and 'not in' in class. Before starting
# Tasks 25–30, research both operators on your own using reliable
# Python learning resources or the official Python documentation.
# Learn what each operator does, how it works with lists, and how
# to use it inside if statements and while loops.
# Write a short comment in your code explaining the difference
# between 'in' and 'not in' in your own words.
# The examples below are starting hints, NOT a substitute for research.
#
# NEW CONCEPT:
# 'in' checks whether a value is in a list.
# Example: "apple" in ["apple", "banana"] evaluates to True.
# 'not in' checks whether a value is missing.
# Example: "grape" not in ["apple", "banana"] evaluates to True.
# These expressions are useful in if statements and while loops.

# TASK 25:
# Create foods = ["pizza", "burger", "tacos", "sushi", "pasta"].
# Ask the user to enter a food.
# Use 'in' to print "Available" or "Not available".
# Do NOT use index() to search.
foods = ["pizza", "burger", "tacos", "sushi", "pasta"]
inpFood = input("Enter a food name in lowercase: ")
if inpFood in foods:
    print("Available")
else:
    print("Not available")

# TASK 26:
# Create supplies = ["pencil", "notebook", "eraser", "backpack"].
# Ask the user for an item.
# Use 'not in' to print "Need to buy" if it is missing,
# otherwise print "Already have it".
supplies = ["pencil", "notebook", "eraser", "backpack"]
inpSupply = input("Enter item in lowercase: ")
if inpSupply not in supplies:
    print("Need to buy")
else:
    print("Already have it")

# TASK 27:
# Create usernames = ["alex123", "gamer99", "pythonpro"].
# Ask the user to enter a new username.
# If it is already in the list, print "Username taken".
# Otherwise append it and print the updated list.
# Do not allow duplicates.
usernames = ["alex123", "gamer99", "pythonpro"]
inpUsername = input("Enter new username: ")
if inpUsername in usernames:
    print("Username taken")
else:
    usernames.append(inpUsername)
    print(usernames)

# TASK 28:
# Modify the idea from Task 27 using a NEW list named accounts.
# Start with accounts = ["admin", "guest"].
# Use a while loop to keep asking until the entered name
# is NOT in accounts. Append the accepted name and print accounts.
# REQUIREMENT: Use 'not in' in your solution.
accounts = ["admin", "guest"]
inpAccount = "guest"
while inpAccount in accounts:
    inpAccount = input("Enter account name: ")
    if inpAccount not in accounts:
        accounts.append(inpAccount)
        print(accounts)
        break

# TASK 29:
# Create secret_words = ["dragon", "robot", "python", "galaxy"].
# Keep asking the user for a word UNTIL it is in secret_words.
# Count and print the number of guesses made.
# A correct first guess should count as 1.
secret_words = ["dragon", "robot", "python", "galaxy"]
guesses = 1
inpWord = "filler"
while inpWord not in secret_words:
    inpWord = input("Enter secret word: ")
    if inpWord in secret_words:
        print("Correct on", guesses, "try!")
        break
    else:
        guesses += 1
        
# TASK 30:
# Create guests = [].
# Ask the user to enter EXACTLY FIVE UNIQUE guest names.
# If a name is already in guests, reject it and ask again.
# Use a while loop, 'in' or 'not in', and append().
# Print the finished list and its length.
guests = []
names = 0
while names < 5:
    inpName = input("Enter 5 unique names: ")
    if inpName in guests:
        print("Name already added")
    else:
        guests.append(inpName)
        names += 1
print(guests, "count:", names)

# ============================================================
# SECTION 6 — LISTS + FUNCTIONS (TASKS 31–35)
# ============================================================

# TASK 31:
# Create a function named count_positive(numbers).
# RETURN how many elements are greater than 0.
# Do NOT use count().
# Test: count_positive([-2, 0, 4, 9, -1]) -> 2
def count_positive(numbers):
    posCnt = 0
    for num in numbers:
        if num > 0:
            posCnt += 1
    return posCnt

numOfPos = count_positive([-2, 0, 4, 9, -1])
print("Positive numbers:", numOfPos)

# TASK 32:
# Create a function named find_item(items, target).
# RETURN the index of the FIRST matching item, or -1 if missing.
# Do NOT use index().
# Test: find_item(["cat", "dog", "cat"], "cat") -> 0
# Test: find_item(["cat", "dog"], "fish") -> -1
def find_item(items, target):
    itemIdx = -1
    if target in items:
        itemIdx = items.index(target)
    return itemIdx

test = find_item(["cat", "dog", "cat"], "cat")
print(test)
test = find_item(["cat", "dog"], "fish")
print(test)

# TASK 33:
# Create a function named unique_items(items).
# RETURN a NEW list without duplicate values, preserving first
# appearance order. REQUIREMENT: Use 'not in'.
# Test: unique_items([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
def unique_items(items):
    uniItems = []
    for item in items:
        if item not in uniItems:
            uniItems.append(item)
    return uniItems

test = unique_items([1, 2, 2, 3, 1, 4])
print(test)

# TASK 34:
# Create a function named common_items(list1, list2).
# RETURN a NEW list of values found in BOTH lists.
# Include each matching value only once, in list1's order.
# REQUIREMENT: Use both 'in' and 'not in'.
# Test: common_items([1, 2, 3, 3], [3, 4, 1]) -> [1, 3]
def common_items(list1, list2):
    commons = []
    for item in list1:
        if item in list2:
            if item not in commons:
                commons.append(item)
    return commons

test = common_items([1, 2, 3, 3], [3, 4, 1])
print(test)

# TASK 35:
# Create a function named reverse_list(items).
# RETURN a NEW list in reverse order, without changing items.
# Do NOT use reverse(), reversed(), or [::-1].
# Test: reverse_list([10, 20, 30]) -> [30, 20, 10]
def reverse_list(items):
    reversedList = []
    for item in items:
        reversedList.insert(0, item)
    return reversedList

test = reverse_list([10, 20, 30])
print(test)

# ============================================================
# SECTION 7 — DEBUGGING (TASKS 36–37)
# ============================================================

# TASK 36:
# Fix this code so it prints 1, 2, 3, 4, 5 exactly once each.
# Explain in a comment what was wrong.
#
# number = 1
# while number <= 5:
#     print(number)
#
# Do NOT replace the while loop with a for loop.
number = 1
while number <= 5:  #what was wrong here was we didnt increase our number, so while was
    print(number)   #always true, and it always printed 1
    number += 1     

# TASK 37:
# Fix this code so it removes ALL 4s without skipping any.
# Explain in a comment why the original approach can fail.
#
# values = [4, 4, 7, 4, 9]
# for value in values:
#     if value == 4:
#         values.remove(value)
# print(values)
#
# Expected: [7, 9]
# HINT: A while loop and 'in' can help.
values = [4, 4, 7, 4, 9]
while 4 in values:          #we need a while loop because the og goes throught first 3
    values.remove(value)    #values, then stops because the first 4s are removed and theres
print(values)               #only 3 indexes to go through and has counted 3 indexes gone through

#while loops makes it remove the first matching value as long as it recognizes a 4 in the list

# ============================================================
# FINAL BOSS CHALLENGES (TASKS 38–40)
# ============================================================

# TASK 38 — SHOPPING LIST MANAGER:
# Build a menu-driven program with:
# 1. Add item
# 2. Remove item
# 3. View numbered items
# 4. Search for item
# 5. Exit
# Start with shopping_list = [].
# REQUIREMENTS:
# - Use a while loop for the menu and a for loop to display items.
# - Use 'in' to prevent duplicates and 'not in' to reject missing items.
# - Handle an empty list and invalid menu selections.
# - Keep running until the user chooses Exit.


# TASK 39 — GRADE ANALYZER:
# Create a function named analyze_grades(grades).
# RETURN a list containing, IN THIS ORDER:
# [highest_grade, lowest_grade, average_grade, passing_count, failing_count]
# Passing means 70 or higher.
# Do NOT use sum(), min(), max(), or sorting.
# For an empty list, RETURN [].
# Test: analyze_grades([95, 82, 67, 74, 58])
# Expected: [95, 58, 75.2, 3, 2]
# Test with a single grade and all-negative values too.


# TASK 40 — STUDENT ATTENDANCE SYSTEM:
# Start with:
# students = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
# present = []
# absent = []
# For EACH student, ask whether they are Present (P) or Absent (A).
# REQUIREMENTS:
# - Use a for loop to process the student list.
# - Use a while loop to reject anything other than P or A.
# - Prevent duplicate attendance records using 'in' / 'not in'.
# - Print numbered present and absent lists.
# - Print the number present, number absent, and attendance percentage.
# - Print "Perfect Attendance!" if everyone is present.
# - Create attendance_percentage(present, students) that RETURNS
#   the percentage; if students is empty, RETURN 0.
# - Test with all present, all absent, and a mixture.


# ============================================================
# END OF CHECKPOINT — REVIEW YOUR WORK BEFORE PUSHING
# ============================================================
