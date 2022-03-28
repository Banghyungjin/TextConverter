def convert_text(input_text):  # method that converts string into hex code
    binary_converted = ' '.join(format(c, 'x') for c in bytearray(input_text, "utf-8"))
    print(binary_converted)


if __name__ == '__main__':
    print('Please enter sentence you want to convert into hex code')
    convert_text(input())
