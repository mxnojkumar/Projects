import os
import sys

FILENAME = "todos.txt"

def get_todos():
    """ This is a function
    This reads the file line by line
    And returns as a list """
    
    # This detects if we're running as an executable created by PyInstaller
    if getattr(sys, 'frozen', False):
        # Path to the folder where the executable is located
        base_path = sys._MEIPASS
    else:
        # Use the current directory during development
        base_path = os.path.dirname(__file__)

    # Create the full path to the text file
    file_path = os.path.join(base_path, 'test_files', 'todos.txt')
    
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg):
    """This is another function
    This is to overwrite the content of the file
    It needs to be called with a list argument """
    
    # This detects if we're running as an executable created by PyInstaller
    if getattr(sys, 'frozen', False):
        # Path to the folder where the executable is located
        base_path = sys._MEIPASS
    else:
        # Use the current directory during development
        base_path = os.path.dirname(__file__)

    # Create the full path to the text file
    file_path = os.path.join(base_path, 'test_files', 'todos.txt')
    
    with open(file_path, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)
        

if __name__ == "__main__":
    print("Hello")
    print("This is functions.py!")