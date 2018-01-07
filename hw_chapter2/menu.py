from hw_chapter2.notebook import Notebook


class Menu:
    '''Displays a menu and respond to choices when run'''

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1" : self.show_notes,
            "1": self.search_notes,
            "1": self.add_note,
            "1": self.modify_note,
            "1": self.quit
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
        '''Displays the menu and respond to choices'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} if not a valid choice".format(choice))

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo
            ))

    # Missing implementation of other methods (pg. 55)