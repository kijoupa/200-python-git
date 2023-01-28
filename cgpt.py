from difflib import HtmlDiff

# original strings
string1="Hello World2"
string2="Hello Hello World"

# create a diff object
diff = HtmlDiff()

# compare the strings
diff_result = diff.make_file(string1.splitlines(), string2.splitlines())

# print the differences
print(diff_result)

file = open("cgpt.html", "w")
file.write(diff_result)
file.close()