import base64
def encode_integer_to_string(number):
    number_bytes = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')
    encoded_string = base64.urlsafe_b64encode(number_bytes).decode('utf-8')
    return encoded_string

def decode_string_to_integer(encoded_string):
    number_bytes = base64.urlsafe_b64decode(encoded_string.encode('utf-8'))
    return int.from_bytes(number_bytes, byteorder='big')


def encode_string_to_string(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode('utf-8')
    # Encode bytes to a URL-safe Base64 string
    encoded_string = base64.urlsafe_b64encode(input_bytes).decode('utf-8')
    return encoded_string

def decode_string_to_string(encoded_string):
    # Decode URL-safe Base64 string to bytes
    decoded_bytes = base64.urlsafe_b64decode(encoded_string.encode('utf-8'))
    # Decode bytes back to string
    return decoded_bytes.decode('utf-8')

