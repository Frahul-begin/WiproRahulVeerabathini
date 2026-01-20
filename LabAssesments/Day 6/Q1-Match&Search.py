import re
# 1.
emp_id = "EMP123 is logged in"
pattern_emp = r"^EMP\d{3}"

if re.match(pattern_emp, emp_id):
    print("Valid Employe ID found at start")
else:
    print("Invalid Employe ID found")

# 2.

text = "Please contact us at support@gmail.com for help"
pattern_email = r"\b[\w\.-]+@[\w\-]+\.\w+\b"

email_match = re.search(pattern_email, text)
if email_match:
    print("Email found:", email_match.group())
else:
    print("Email not found")

# 3.
sample_text = "User123 logged in at 10am"
patter_meta = r"\w+\d"

matches = re.finditer(patter_meta, sample_text)
result = []
for m in matches:
    result.append(m.group())

print("Matches using meta data:", matches)

# 4.
date_text = "Date: 20-01-2026"

pattern_date = r"(\d{2})-(\d{2}-(\d{4}))"
date_match = re.search(pattern_date, date_text)

if date_match:
    print("Date found:", date_match.group(0))
    print("Day:", date_match.group(1))
    print("Month:", date_match.group(2))
    print("Year:", date_match.group(3))
else:
    print("Date not found")