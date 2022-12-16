from PyInquirer import prompt
from pyfiglet import Figlet
from colorama import Fore
from prompt_toolkit.validation import Validator, ValidationError

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


questions = [
    {
        "type": "input",
        "name": "wordlist",
        "message": "Wordlist to parse:"
    },
    {
        "type": "input",
        "name": "length",
        "message": "Length of words:",
        "validate": NumberValidator,
    },
    {
        "type": "confirm",
        "name": "confirm",
        "message": "Is it okay for you?"
    },
]


def number_validator(value):
    try:
        int(value)
    except:
        print("")


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
        f.close

        with open(f"wordlist_length_{word_length}.txt", "w") as f:
            print(f"{Fore.LIGHTRED_EX}>  Creating wordlist...")
            for word in wordlist:
                f.write(f"{word}\n")
        f.close
        print(f"{Fore.LIGHTRED_EX}>  wordlist_length_{word_length}.txt created.")

    else:
        main()


if __name__ == "__main__":
    main()
