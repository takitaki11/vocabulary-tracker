from word import Word
import os
import json
import csv
from datetime import datetime

class WordManager:
    def __init__(self, filepath='words.txt'):
        self.filepath = filepath
        self.words = []
        self.load_words()

    def load_words(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.words = [Word.from_line(line) for line in f.readlines()]
        else:
            self.words = []

    def save_words(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            for word in self.words:
                f.write(word.to_line())

    def log_operation(self, action):
        with open("log.txt", "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now()}] {action}\n")

    def add_word(self, term, definition, example):
        self.words.append(Word(term, definition, example))
        self.save_words()
        self.log_operation(f"Added: {term}")

    def show_words(self):
        for i, word in enumerate(self.words, 1):
            print(f"{i}. {word.term} - {word.definition} (e.g. {word.example})")

    def update_word(self, index, term, definition, example):
        if 0 <= index < len(self.words):
            self.words[index] = Word(term, definition, example)
            self.save_words()
            self.log_operation(f"Updated: {term}")

    def delete_word(self, index):
        if 0 <= index < len(self.words):
            self.log_operation(f"Deleted: {self.words[index].term}")
            del self.words[index]
            self.save_words()

    def generate_report(self):
        print(f"\n📊 Всего слов: {len(self.words)}")
        if self.words:
            longest = max(self.words, key=lambda w: len(w.term))
            print(f"📌 Самое длинное слово: {longest.term}")
        self.log_operation("Generated report")

    def export_to_csv(self, filename='words.csv'):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("term,definition,example\n")
            for w in self.words:
                f.write(f'"{w.term}","{w.definition}","{w.example}"\n')
        self.log_operation("Exported to CSV")

    def import_from_csv(self, filename='words.csv'):
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.words.append(Word(row['term'], row['definition'], row['example']))
        self.save_words()
        self.log_operation("Imported from CSV")

    def export_to_json(self, filename='words.json'):
        data = [w.__dict__ for w in self.words]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        self.log_operation("Exported to JSON")

    def import_from_json(self, filename='words.json'):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                self.words.append(Word(**item))
        self.save_words()
        self.log_operation("Imported from JSON")
