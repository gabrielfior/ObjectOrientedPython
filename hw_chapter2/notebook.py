import datetime

last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a string in searches and store tags for each note'''

    def __init__(self, memo=None, tags=''):
        '''Initialize a note with memo and optional space-separated tags. Automatically set the note's
        creation date and a unique ID'''

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.today()
        self.id = self.retrieve_unique_id()

    def __str__(self):
        return "ID: %d, memo: %s, tags: %s" %(self.id, self.memo, self.tags)

    def retrieve_unique_id(self):
        global last_id
        last_id += 1
        return last_id

    def match(self, filter):
        '''Determine if this note matches the filter text.
        Searches for matches in the note's memo and in the note's tags'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Represents a collection of notes that can be tagged, modified and searched'''

    def __init__(self):
        '''Initializes notebook with empty list'''
        self.notes = []

    def new_note(self, memo, tags = ''):
        '''Creates new note and it to notebook's notes list'''
        note = Note(memo, tags)
        print("Inserted note with ID %d and memo %s" %(note.id, note.memo))
        self.notes.append(note)

    def _find_note(self, note_id):
        '''
        Locate the note with given ID
        :param note_id: ID of note to be found
        :return: note with ID corresponding to note_id
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return None

    def modify_memo(self, note_id, memo):
        '''
        Finds the note with the given ID and change its memo to the given value
        :param note_id: ID of note to be modified
        :param memo: Memo to be stored
        :return: Boolean indicating success or failure of update
        '''''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True

        return False

    def modify_tags(self, note_id, tags):
        '''
        Finds note with given ID and change its tags to given value
        :param note_id: Note ID to be found
        :param tags: tags to store in the note
        :return:
        '''

        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''
        Finds all notes that match given filter string
        :param filter: string with which notes will be queried
        :return:
        '''

        return [note for note in self.notes if note.match(filter)]