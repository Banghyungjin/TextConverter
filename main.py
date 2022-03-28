# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def convert_text(input_text):
    binary_converted = ' '.join(format(c, 'x') for c in bytearray(input_text, "utf-8"))
    print(binary_converted)


if __name__ == '__main__':
    print('Please enter sentence you want to conver into hex code')
    convert_text(input())
