import os

# ==========================================
# 1. Write & Read File using Functions
# ==========================================
def task_1():
    # 'w+' creates/overwrites and allows reading
    with open("question.txt", "w+") as f:
        print("Enter 10 lines of text:")
        for i in range(1, 11):
            line = input(f"Line {i}: ")
            f.write(line + "\n")
        
        f.seek(0)
        content = f.read()
        print("\n--- File Content ---")
        print(content)
        print("Total number of lines:", len(content.splitlines()))

# ==========================================
# 2. Count Words, Characters, and Lines
# ==========================================
def task_2():
    with open("question.txt", "r") as f:
        data = f.read()
        lines = data.splitlines()
        words = data.split()
        print(f"Lines: {len(lines)}, Words: {len(words)}, Characters: {len(data)}")

# ==========================================
# 3. Append Data to File
# ==========================================
def task_3():
    user_data = input("Enter text to append: ")
    with open("question.txt", "a+") as f:
        f.write(user_data + "\n")
        f.seek(0)
        print("Updated Content:\n", f.read())

# ==========================================
# 4. Update File Content (Replace Word)
# ==========================================
def task_4(old_word, new_word):
    with open("question.txt", "r") as f:
        data = f.read()
    updated_data = data.replace(old_word, new_word)
    with open("question.txt", "w") as f:
        f.write(updated_data)
    print(f"Replaced '{old_word}' with '{new_word}'.")

# ==========================================
# 5. Delete Specific Line
# ==========================================
def task_5(line_number):
    with open("question.txt", "r") as f:
        lines = f.readlines()
    
    if 0 < line_number <= len(lines):
        del lines[line_number - 1]
        with open("question.txt", "w") as f:
            f.writelines(lines)
        print(f"Line {line_number} deleted.")

# ==========================================
# 6. Unique Lines from File
# ==========================================
def task_6():
    with open("question.txt", "r") as f:
        lines = f.readlines()
    unique_lines = list(set(lines))
    with open("unique_lines.txt", "w") as f:
        f.writelines(unique_lines)
    print("Unique lines saved to unique_lines.txt")

# ==========================================
# 7. Count Number of Entries (Student Names)
# ==========================================
def task_7():
    name = input("Enter student name: ")
    with open("students.txt", "a+") as f:
        f.write(name + "\n")
        f.seek(0)
        print("Total Student Entries:", len(f.readlines()))

# ==========================================
# 8. File Copy and Move (Rename)
# ==========================================
def task_8():
    # Copy
    with open("question.txt", "r") as original, open("copy.txt", "w") as duplicate:
        duplicate.write(original.read())
    # Move (Simulated by rename)
    if os.path.exists("moved_file.txt"): os.remove("moved_file.txt")
    os.rename("copy.txt", "moved_file.txt")
    print("File copied and renamed to moved_file.txt")

# ==========================================
# 9. File Rename and Delete (Error Handling)
# ==========================================
def task_9():
    try:
        # Create a temp file to demonstrate
        open("temp.txt", "w").close()
        os.rename("temp.txt", "renamed.txt")
        os.remove("renamed.txt")
        print("File renamed and deleted successfully.")
    except FileNotFoundError:
        print("Error: The file does not exist.")

# ==========================================
# 10. Filter Lines Based on Condition
# ==========================================
def task_10(keyword):
    with open("question.txt", "r") as f, open("filtered.txt", "w") as out:
        for line in f:
            if keyword in line:
                out.write(line)
    print(f"Lines containing '{keyword}' moved to filtered.txt")

# ==========================================
# 11. Count Frequency of Each Word
# ==========================================
def task_11():
    with open("question.txt", "r") as f:
        words = f.read().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("Word Frequency Dictionary:", freq)

# ==========================================
# 12. File Handling with Parameters
# ==========================================
def task_12(filename):
    # Write
    with open(filename, "w") as f: f.write("Sample line 1\nSample line 2")
    # Read
    with open(filename, "r") as f:
        data = f.read()
        lines = len(data.splitlines())
        words = len(data.split())
    return lines, words

# ==========================================
# 13. Merge Two Files
# ==========================================
def task_13():
    # Creating two dummy files first
    with open("file1.txt", "w") as f: f.write("Content from File 1")
    with open("file2.txt", "w") as f: f.write("Content from File 2")
    
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
        f3.write(f1.read() + "\n" + f2.read())
    
    with open("merged.txt", "r") as f:
        print("Merged Result:\n", f.read())

# ==========================================
# 14. Mini CRUD System
# ==========================================
def task_14():
    while True:
        print("\n1. Add Record  2. View Records  3. Exit")
        choice = input("Select option: ")
        if choice == '1':
            with open("records.txt", "a") as f:
                f.write(input("Enter record details: ") + "\n")
        elif choice == '2':
            try:
                with open("records.txt", "r") as f: print("\nRecords:\n" + f.read())
            except FileNotFoundError: print("No records found.")
        elif choice == '3':
            break

# ==========================================
# TESTING THE FUNCTIONS
# ==========================================
# You can uncomment these lines one by one to test:
# task_1()
# task_2()
# task_14()