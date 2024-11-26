def modify_byte(file_path, byte_index, new_byte_value):
    with open(file_path, "r+b") as f:
        f.seek(byte_index)
        f.write(bytes([new_byte_value]))  # Modify the byte

modify_byte(r"C:\Users\datho\encrypted_cfb.txt", 7, 0xFF)  # Change the 8th byte to 0xFF
modify_byte(r"C:\Users\datho\encrypted_ofb.txt", 7, 0xFF)  # Change the 8th byte to 0xFF
