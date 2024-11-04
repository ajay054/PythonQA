# Check if a String Is a Valid IPv4 Address
def is_valid_ipv4(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True
# This checks if the string has four numeric parts in the range of 0–255.

print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("256.100.50.25"))
print(is_valid_ipv4("192.168.1"))
print(is_valid_ipv4("192.168.1.abc"))