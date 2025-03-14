from typing import List
import string
import re


def decode_unicode(text: str) -> str:
        return re.sub(r'\\u([0-9a-fA-F]{4})', lambda match: chr(int(match.group(1), 16)), text)

def get_longest_diverse_words(file_path: str) -> List[str]:
        words = set()
        with open(file_path, encoding='utf-8') as file:
                for line in file:
                        line = decode_unicode(line)
                        words.update(re.findall(r'\w+', line))
        words = sorted(words, key=lambda word: (-len(set(word)), -len(word)))
        return words[:10]

def get_rarest_char(file_path: str) -> str:
        char_count = {}
        with open(file_path, encoding='utf-8') as file:
                for line in file:
                        line = decode_unicode(line)
                        for char in line:
                                char_count[char] = char_count.get(char, 0) + 1
        most_common_char = min(char_count, key=char_count.get)
        unicode_value = f"\\u{ord(most_common_char):04X}"
        return f"{most_common_char} {unicode_value}" if char_count else None

def count_punctuation_chars(file_path: str) -> int:
        count = 0
        with open(file_path, encoding='utf-8') as file:
                for line in file:
                        line = decode_unicode(line)
                        count += sum(1 for char in line if char in string.punctuation)
        return count

def count_non_ascii_chars(file_path: str) -> int:
        count = 0
        with open(file_path, encoding='utf-8') as file:
                for line in file:
                        line = decode_unicode(line)
                        count += sum(1 for char in line if ord(char) > 127) 
        return count

def get_most_common_non_ascii_char(file_path: str) -> str:
        char_count = {}
        with open(file_path, encoding='utf-8') as file:
                for line in file:
                        line = decode_unicode(line)
                        for char in line:
                                if ord(char) > 127:
                                        char_count[char] = char_count.get(char, 0) + 1
        most_common_char = max(char_count, key=char_count.get)
        unicode_value = f"\\u{ord(most_common_char):04X}"
        return f"{most_common_char} {unicode_value}" if char_count else None

if __name__ == "__main__":
        file_path = 'data.txt'
        print("10 Longest Diverse Words:", get_longest_diverse_words(file_path))
        print("Rarest Character:", get_rarest_char(file_path))
        print("Punctuation Characters Count:", count_punctuation_chars(file_path))
        print("Non-ASCII Characters Count:", count_non_ascii_chars(file_path))
        print("Most Common Non-ASCII Character:", get_most_common_non_ascii_char(file_path))
