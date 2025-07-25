def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

def main():
    text = input()
    converted_text = convert(text)
    print(converted_text)

main()
