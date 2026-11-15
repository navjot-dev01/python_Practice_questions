# WAP to print the contents of directories using the os module 
import os
import sys

def print_directory_contents(path="/"):
    """
    Prints the names of all files and subdirectories within the given path.

    Args:
        path (str): The path to the directory. Defaults to the current directory (.). (/)= c drive directories,
    """
    try:
        # Get the list of all entries in the directory
        entries = os.listdir(path)

        print(f"Contents of directory '{path}':")
        # Iterate over the list and print each entry
        for entry in entries:
            full_path = os.path.join(path, entry)
            # Check if it's a file or a directory for better formatting
            if os.path.isdir(full_path):
                print(f"[DIR] {entry}")
            else:
                print(f"[FILE] {entry}")
                
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Example Usage ---

# 1. Print contents of the current working directory
print_directory_contents()

print("-" * 30)