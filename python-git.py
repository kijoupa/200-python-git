html_begin ="""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <div>
"""

html_end ="""
  </div>
</body>
</html>
"""


string1=""" Geneva Hello World2"""
string2="Lausanne Hello World"

import difflib

def compare_strings(str1, str2):
    # split the strings into lists of words
    str1_words = str1.split()
    str2_words = str2.split()

    # loop through the words in the first string
    for word in str1_words:
        # if the word is not in the second string, it has been deleted
        if word not in str2_words:
            str1 = str1.replace(word, '<span style="color:white; background-color:red;">' + word + '</span>')
    for word in str2_words:
        # if the word is not in the first string, it has been added
        if word not in str1_words:
            str2 = str2.replace(word, '<span style="color:white; background-color:green;">' + word + '</span>')
    return str1,str2


html_diff = compare_strings(string1, string2)
html_diff_list = list(html_diff)
string1=html_diff_list[0]
string2=html_diff_list[1]
print(string1)
print(string2)
print(type(html_diff_list))


file = open("git.html", "w")
file.write(html_begin)
file.write(string1)
file.write(string2)
file.write(html_end)
file.close()
