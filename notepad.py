from tkinter import * 
from tkinter import messagebox as tmg
from tkinter import filedialog
import os

# Define a class for the GUI application
class gui(Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Tk)
        self.geometry('500x400')  # Set the window size
        self.title('Python - Notepad')  # Set the window title
        self.iconbitmap("image/notepad.ico")  # Set the window icon

        # Bind keyboard shortcuts to methods
        self.bind("<Control-n>", lambda event: self.new())
        self.bind("<Control-o>", lambda event: self.open())
        self.bind("<Control-s>", lambda event: self.save())
        self.bind("<Control-Shift-S>", lambda event: self.saveas())
        self.bind("<Control-x>", lambda event: self.cut())
        self.bind("<Control-c>", lambda event: self.copy())
        self.bind("<Control-v>", lambda event: self.paste())
        self.bind("<Control-q>", lambda event: self.exit())

    def new(self):
        """Create a new file."""
        global file 
        self.title("Untitled-Notepad")  # Update the title for a new file
        self.file = None  # Reset the file variable
        self.text.delete(1.0, END)  # Clear the text area

    def open(self):
        """Open an existing file."""
        global file 
        # Open a file dialog to select a file
        self.file = filedialog.askopenfilename(title="Open file", defaultextension=".txt",filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None  # If no file is selected, reset the file variable
        else:
            self.title(os.path.basename(self.file) + '-Notepad')  # Update the title with the file name
            self.text.delete(1.0, END)  # Clear the text area
            with open(self.file, "r") as f:  # Open the file for reading
                self.text.insert(1.0, f.read())  # Insert the file content into the text area

    def save(self):
        """Save the current file."""
        global file
        if self.file is None:  # If no file is currently open
            # Open a save dialog to specify the file name
            self.file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=[("All files", "*.*"), ("Text Document", "*.txt")])
            if self.file == "":
                self.file = None  # If no file name is provided, reset the file variable
            else:
                with open(self.file, "w") as f:  # Open the file for writing
                    f.write(self.text.get(1.0, END))  # Write the text area content to the file
                self.title(os.path.basename(self.file) + '-Notepad')  # Update the title with the file name
        else:
            with open(self.file, "w") as f:  # If a file is already open, overwrite it
                f.write(self.text.get(1.0, END))  # Write the text area content to the file

    def saveas(self):
        """Save the current file with a new name."""
        self.file = filedialog.asksaveasfilename(initialfile=os.path.basename(self.file),defaultextension=".txt",filetypes=[("All files", "*.*"), ("Text Document", "*.txt")])
        if self.file == "":
            self.file = None  # If no file name is provided, reset the file variable
        else:
            with open(self.file, "w") as f:  # Open the file for writing
                f.write(self.text.get(1.0, END))  # Write the text area content to the file
            self.title(os.path.basename(self.file) + '-Notepad')  # Update the title with the file name

    def exit(self):
        """Exit the application."""
        self.destroy()  # Close the application window

    def cut(self):
        """Cut the selected text."""
        self.text.event_generate("<<Cut>>")  # Generate the cut event

    def copy(self):
        """Copy the selected text."""
        self.text.event_generate("<<Copy>>")  # Generate the copy event

    def paste(self):
        """Paste text from the clipboard."""
        self.text.event_generate("<<Paste>>")  # Generate the paste event

    def about(self):
        """Show information about the application."""
        tmg.showinfo("Notepad", "Notepad By Swapneel using python")  # Display an information message box

    def notepadd(self):
        """Create the text area and scrollbar for the notepad."""
        self.scrol = Scrollbar(self)  # Create a scrollbar
        self.scrol.pack(side=RIGHT, fill=Y)  # Pack the scrollbar to the right side

        self.text = Text(self, font=['times new roman', 14, 'normal'])  # Create a text area
        self.text.pack(fill=BOTH, expand=True)  # Pack the text area to fill the window
        self.text.config(yscrollcommand=self.scrol.set)  # Link the scrollbar to the text area
        self.scrol.config(command=self.text.yview)  # Configure the scrollbar to scroll the text area

    def menubar(self):
        """Create the menu bar for the application."""
        self.file = None  # Initialize the file variable
        # File menu
        self.menu = Menu(self)  # Create a menu
        self.file_menu = Menu(self.menu, tearoff=0)  # Create a file menu
        self.file_menu.add_command(label='New', command=self.new)  # Add 'New' command
        self.file_menu.add_command(label='Open', command=self.open)  # Add 'Open' command
        self.file_menu.add_command(label='Save', command=self.save)  # Add 'Save' command
        self.file_menu.add_command(label='Save as', command=self.saveas)  # Add 'Save as' command
        self.file_menu.add_separator()  # Add a separator
        self.file_menu.add_command(label='Exit', command=self.quit)  # Add 'Exit' command
        self.menu.add_cascade(label="File", menu=self.file_menu)  # Add file menu to the main menu

        # Edit menu
        self.edit_menu = Menu(self.menu, tearoff=0)  # Create an edit menu
        self.edit_menu.add_command(label='Cut', command=self.cut)  # Add 'Cut' command
        self.edit_menu.add_command(label='Copy', command=self.copy)  # Add 'Copy' command
        self.edit_menu.add_command(label='Paste', command=self.paste)  # Add 'Paste' command
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)  # Add edit menu to the main menu

        # Help menu
        self.help_menu = Menu(self.menu, tearoff=0)  # Create a help menu
        self.help_menu.add_command(label='About', command=self.about)  # Add 'About' command
        self.menu.add_cascade(label="Help", menu=self.help_menu)  # Add help menu to the main menu

        self.config(menu=self.menu)  # Configure the main window to use the menu

if __name__ == '__main__':
    obj = gui()  # Create an instance of the gui class
    obj.menubar()  # Create the menu bar
    obj.notepadd()  # Create the text area and scrollbar
    obj.mainloop()  # Start the main event loop of the application ```python


# This Python code implements a simple Notepad application using the Tkinter library for the graphical user interface (GUI). The application allows users to create, open, save, and edit text files with keyboard shortcuts and a menu bar. It features basic text editing functionalities such as cut, copy, and paste, along with an "About" section that provides information about the application. The GUI includes a text area with a scrollbar for easy navigation. The application is structured using a class-based approach, encapsulating functionality within methods for better organization and readability. Overall, it serves as a basic text editor.