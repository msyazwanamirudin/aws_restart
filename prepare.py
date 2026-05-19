seq = ""

try:
    with open("preproinsulin-seq-clean.txt") as file:
        seq = file.read()
except Exception as e:
    print(e)

try:
    with open("lsinsulin-seq-clean.txt") as file1:
        file1.write(seq[:24])
except Exception as e:
    print(e)

try:
    with open("binsulin-seq-clean.txt") as file1:
        file1.write(seq[24:54])
except Exception as e:
    print(e)

try:
    with open("ainsulin-seq-clean.txt") as file1:
        file1.write(seq[54:84])
except Exception as e:
    print(e)

try:
    with open("cinsulin-seq-clean.txt", "w") as file1:
        file1.write(seq[84:110])
except Exception as e:
    print(e)

print(seq[1:24])
