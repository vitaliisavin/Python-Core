commands = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code',
            'ordered-list', 'unordered-list', 'new-line')
printed_text = []


def get_level():
    while True:
        level = int(input('Level: '))
        if 0 < level < 6:
            return level
        else:
            print('The level should be within the range of 1 to 6')


def get_text():
    return input('Text: ')


def get_url():
    return input('URL: ')


def get_label():
    return input('Label: ')


def changed_text(text, command):
    if command == 'plain':
        return text
    elif command == 'bold':
        return '**' + text + '**'
    elif command == 'italic':
        return '*' + text + '*'
    elif command == 'inline-code':
        return '`' + text + '`'


def get_rows():
    while True:
        num_rows = int(input('Number of rows: '))
        if num_rows > 0:
            break
        print('The number of rows should be greater than zero')
    rows = []
    for i in range(num_rows):
        rows.append(input(f'Row #{i + 1}: '))
    return rows


def do_command(command):
    if command == 'header':
        printed_text.append('#' * get_level() + ' ' + get_text() + '\n')
        print("".join(printed_text))
    elif command == 'new-line':
        printed_text.append('\n')
        print("".join(printed_text))
    elif command == 'link':
        printed_text.append('[' + get_label() + '](' + get_url() + ')')
        print("".join(printed_text))
    elif command == 'ordered-list':
        rows = get_rows()
        for i in range(len(rows)):
            printed_text.append(str(i + 1) + '. ' + rows[i] + '\n')
        print("".join(printed_text))
    elif command == 'unordered-list':
        rows = get_rows()
        for i in range(len(rows)):
            printed_text.append('* ' + rows[i] + '\n')
        print("".join(printed_text))
    else:
        printed_text.append(changed_text(get_text(), command))
        print("".join(printed_text))


def save_in_file():
    with open('output.md', 'w') as file:
        for row in printed_text:
            file.write(row)


def main():
    while True:
        command = input('Choose a formatter: ')
        if command == '!done':
            save_in_file()
            break
        elif command not in commands:
            print('Unknown formatting type or command')
            continue
        elif command in commands:
            do_command(command)


if __name__ == "__main__":
    main()
