class Note:
    def __init__(self, content, tags=None):
        self.content = content
        self.tags = tags if tags else []

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def search_by_tag(self, tag):
        matching_notes = []
        if tag in self.tags:
            matching_notes.append(self)
        return matching_notes