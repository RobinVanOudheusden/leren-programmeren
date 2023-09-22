import base64

# Your Python code as a string
python_code = """
CmRlZiBncmVldChuYW1lKToKICAgIHByaW50KGYiSGVsbG8sIHtuYW1lfSEiKQoKZ3JlZXQoIkFsaWNlIikK
"""

# Encode the Python code as bytes
encoded_code = base64.b64encode(python_code.encode('utf-8'))

# Decode the encoded code (if needed)
decoded_code = base64.b64decode(encoded_code).decode('utf-8')

# Print the encoded and decoded code
print("Encoded Code:")
print(encoded_code.decode('utf-8'))

print("\nDecoded Code:")
print(decoded_code)
