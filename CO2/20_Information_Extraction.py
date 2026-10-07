import re

text = """
Aditya Mourya joined NIET in Greater Noida.
Email: aditya@example.com
Phone: +91-9876543210
"""

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
phones = re.findall(r'\+?\d[\d -]{9,}\d', text)

print("Extracted Email:")
print(emails)

print("\nExtracted Phone:")
print(phones)

# Simple named-entity style extraction for capitalized words.
names_places = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)

print("\nPossible Names/Places:")
print(names_places)
