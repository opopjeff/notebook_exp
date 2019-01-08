import datetime

last_id = 0

class Note:
    def __init__(self,memo,tags = ''):
        self.memo = memo
        self.tags = tags
        self.caculation_date = datetime.date.today()
        global last_id
        last_id+=1
        self.id = last_id

    def match(self,filter):
        return filter in self.memo or filter in self.tags

class Notebook:
    def __init__(self):
        'Initialize a notebook with an empty list'
        self.notes = []

    def new_note(self,memo,tags = ''):
        'create a new note and add it to the list'
        self.notes.append(Note(memo,tags))

    def modify_memo(self,note_id,memo):
        self.find_id(note_id).memo = memo
        

    def modify_tags(self,note_id,tags):
        self.find_id(note_id).tags = tags

    def find_id(self,note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        

    def search(self,filter):
        return [note for note in self.notes if note.match(filter)]
    
