import re

text = """REPORT: Sales Summary
Revenue increased by 12 percent.
The next quarter may remain stable.

INVOICE: 1042
Bill To: Example Customer
Amount Due: $250

MEMO: Office Update
The office will be closed on Friday."""

def boundary_score(line):
    if not line:
        return 0.0
    score = 0.05
    if re.match(r"^(REPORT|INVOICE|MEMO|LETTER|FORM)\\b", line, re.I):
        score += 0.75
    if len(line) < 45 and line.isupper():
        score += 0.15
    return min(score, 0.99)

state = "OUTSIDE"
documents, current = [], []
for line in (x.strip() for x in text.splitlines()):
    if boundary_score(line) >= 0.70:
        if current:
            documents.append("\\n".join(current).strip())
        current = [line]
        state = "INSIDE"
    elif line:
        current.append(line)
        state = "INSIDE"
if current:
    documents.append("\\n".join(current).strip())

print("Detected documents:", len(documents))
for i, doc in enumerate(documents, 1):
    print(f"\\n--- Document {i} ---\\n{doc}")
