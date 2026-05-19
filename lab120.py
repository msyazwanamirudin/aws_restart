# Store the human preproinsulin sequence in a variable called 
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# preproInsulin = ""

# try:
#     with open("lsinsulin-seq-clean.txt" , "r") as f1:
#         preproInsulin = f1.read()
# except Exception as e:
#     print (e)

# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  

aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 
    'M': 149.21,'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 
    'S': 105.09, 'T': 119.12,'V': 117.15, 'W': 204.23, 'Y': 181.19
    }

# Count the number of each amino acids  

keyList = [
        'A', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'K', 'L', 'M', 'N', 'P', 'Q',
        'R', 'S', 'T', 'V', 'W', 'Y'
    ]

for x in keyList:
    print ({x: float(insulin.upper().count(x))})

aaCountInsulin = ({})

# aaCountInsulin = ({x: float(insulin.upper().count(x)) 
#                    for x in [
#                        'A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S','T','V', 'W', 'Y'
#                     ]}) 