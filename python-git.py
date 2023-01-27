
string1="""
Hello World
My name is John
I am 25 years old
"""
string2="""
Hello World
My name is Jack
I am 30 years old
"""

import difflib

def compare_strings(string1, string2):
    return "".join(difflib.unified_diff(string1.splitlines(), string2.splitlines()))

diff = compare_strings(string1, string2)

print(diff)