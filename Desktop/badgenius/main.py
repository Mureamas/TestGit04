# Import functions and variables from app.py
from app import reduce_to_20_chars, convert_to_40_chars

def main():
    original_string = "aaddabdcacbdaddabacdbbccbccbbdcaaadd"
    encoded_string = reduce_to_20_chars(original_string)
    decoded_string = convert_to_40_chars(encoded_string)

    print("Original String:",original_string)
    print("Encoded String:",encoded_string)
    print("Decoded String:",decoded_string)

if __name__ == "__main__":
    main()
