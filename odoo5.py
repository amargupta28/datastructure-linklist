'''
Write a regular expression to find any word between 4 and 9 letters long and containing either “odoo”, “code” or “work”?
'''


import re

txt = "ramcodeis"
x = re.match(r"\b(?=\w{4,9}\b)\w{0,9}(code|work|odoo)\w*",txt)

if x:
    print("Match")
else:
    print("No Match")