# Q1: Write a Python script that accepts input from the user until the user types "end".

print("Welcome to Notes CLI!")
print("Type 'end' to exit and save notes\n\n")

try:
    inp = ""
    notes = []

    # get info
    while inp != "end":
        inp = input("> ")
        if inp == "end":
            break
        else:
            notes.append("\n" + inp)

    # write info to file and close
    with open("notes.txt", "a") as f:
        f.writelines(notes)

    # reopen file and write to stdout
    with open("notes.txt", "r") as f:
        print("\n\n", "=== SAVED NOTES ===")
        for line in f:
            print(line, end="")

except FileNotFoundError:
    print("Could not open notes! Please ensure notes.txt exists")
except PermissionError:
    print("Could not open notes! Please you have sufficient permissions")
except EOFError:
    print("EOF encountered! Quiting...")


# Q2: Write a script that copies one file to another
print("Welcome to File Cloner 1.0.0")
print("**NOTE: relative or absolute paths may be used**\n")

# take src and dest files
src_file_path = input("Specify the path of the source file: ")
dest_file_path = input("Specify the path of the destination file: ")

try:
    # open src for read
    with open(src_file_path) as src_file:
        # open dest for writing
        with open(dest_file_path, "w") as dest_file:
            # implement copy
            dest_file.write(src_file.read())

except PermissionError as e:
    print("Error: Insufficient user permisions", e.with_traceback())
except FileNotFoundError as e:
    print("Error: File not found", e.with_traceback())
except IOError as e:
    print("Error: IO error", e.with_traceback())
except Exception as e:
    print("Error: An exception occured", e.with_traceback())
