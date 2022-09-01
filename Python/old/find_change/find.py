import re   # regex module
 
# opening and reading the file
with open('text.txt') as f:
  string = f.readlines()
   
def change(string, pattern, replacementText):
  
    # initializing the list objects
    changedText = []
    originalText = []
    totalCount=0

    # extracting the IP addresses
    for line in string:
        line = line.rstrip()

        # replace patterns in text
        modText, count = re.subn(pattern, replacementText, line, flags=re.MULTILINE) 

        # count replaced text
        if count:
            originalText.append(line)
            changedText.append(modText)
            totalCount += count
    
    return originalText, changedText, totalCount
    # print(f'변경 수 : {totalCount}')
    # index = 0
    # for i in changedText:
    #     index += 1
    #     print(f'{index} : {originalText[index-1]} -> {i}')

print(change(string, pattern = "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", replacementText="*.*.*.*"))
print(change(string, pattern="hunseop", replacementText="gogo"))