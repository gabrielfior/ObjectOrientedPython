import sys

from hw_chapter2.notebook import Notebook


class Menu:
    '''Displays a menu and respond to choices when run'''

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu 
        
        1. Show all notes
        2. Search notes
        3. Add note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        '''
        Displays the menu and respond to choices.
        :return: 
        '''''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} if not a valid choice".format(choice))

    def show_notes(self, notes = None):
        '''
        Shows notes present in notebook. If notes is provided, it gets printed instead
        :param notes: Notes to be printed
        :return: 
        '''''
        if not notes:
            notes = self.notebook.notes

        if notes == []:
            print("No notes to be displayed.")

        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo
            ))

    def search_notes(self):
        '''
        Asks user for input and search notes for any matches (either in memo or in tags)
        :return: 
        '''''
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        '''
        Adds note to notebook.
        :return: 
        '''''
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)

    def modify_note(self):
        '''
        Asks user for note's ID, memo and tags. Adds note with those properties to notebook.
        :return: 
        '''''
        id = input("Enter a note ID: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        '''
        Exists menu CLI tool.
        :return: 
        '''''
        print("Thanks for using Notebook Inc. services today!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()