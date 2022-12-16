from PyInquirer import prompt
from pyfiglet import Figlet
from colorama import Fore
from prompt_toolkit.validation import Validator, ValidationError
from tqdm import tqdm

header = Figlet()
print(header.renderText("Wordlist parser"))
print(f"{Fore.LIGHTRED_EX}Just let yourself be guided by the steps :)\n")


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message="Please enter a number.", cursor_position=len(document.text)
            )


class WordlistValidator(Validator):
    def validate(self, document):
        try:
            open(document.text, "r", encoding="utf-8", errors="ignore")

        except:
            raise ValidationError(
                message="Invalid wordlist", cursor_position=len(document.text)
            )


questions = [
    {
        "type": "input",
        "name": "wordlist",
        "message": "Wordlist to parse:",
        "validate": WordlistValidator,
    },
    {
        "type": "input",
        "name": "length",
        "message": "Length of words:",
        "validate": NumberValidator,
    },
    {"type": "confirm", "name": "confirm", "message": "Is it okay for you?"},
]

def main():
    # Asking prompt
    answers = prompt(questions)
    initial_wordlist = answers.get("wordlist")
    word_length = int(answers.get("length"))
    confirm = answers.get("confirm")

    if confirm:
        wordlist = []
        with open(initial_wordlist, "r", encoding="utf-8", errors="ignore") as f:
            print(f"{Fore.LIGHTRED_EX}>  Parsing files with the right length...")
            content = f.read().strip()
            for word in content.rsplit("\n"):
                if len(word) == word_length:
                    wordlist.append(word)

        with open(f"wordlist_length_{word_length}.txt", "w") as f:
            print(f"{Fore.LIGHTRED_EX}>  Creating wordlist...")
            for word in wordlist:
                f.write(f"{word}\n")
        print(f"{Fore.LIGHTRED_EX}>  wordlist_length_{word_length}.txt created.")

    else:
        main()


if __name__ == "__main__":
    main()
