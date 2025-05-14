class Word:
    def __init__(self, term, definition, example):
        self.term = term
        self.definition = definition
        self.example = example

    def to_line(self):
        return f"{self.term}|{self.definition}|{self.example}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split('|')
        return Word(*parts)
