import re

pan_regex = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

pan = input("Enter PAN number: ").strip()

if re.match(pan_regex, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")