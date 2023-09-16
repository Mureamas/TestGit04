# Define a dictionary for encoding and decoding
encoding_dict = {
    'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
    'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
    'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
    'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
}

# Function to reduce a 40-character string to a 20-character string
def reduce_to_20_chars(input_string):
    result = ""
    for i in range(0, len(input_string), 2):
        pair = input_string[i:i+2]
        result += encoding_dict[pair]
    return result

# Function to convert a 20-character string back to the original 40-character string
def convert_to_40_chars(input_string):
    result = ""
    for char in input_string:
        for key, value in encoding_dict.items():
            if char == value:
                result += key
                break
    return result

