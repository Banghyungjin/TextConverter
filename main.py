# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def convert_text(input_text):
    binary_converted = ' '.join(format(c, 'b') for c in bytearray(input_text, "utf-8"))
    print(binary_converted)


def convert_text2(input_text):
    binary_converted = ' '.join(map(hex, bytearray(input_text, "utf-8")))
    print(binary_converted)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_text('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
