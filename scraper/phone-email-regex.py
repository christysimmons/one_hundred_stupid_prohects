#! python3

import re, pyperclip

# Create a regex object for phone numbers
phoneReg = re.compile(r'''
# 916-999-9999, 555-5555, (916) 212-6364, 555-5555 (ext | ext. | x) 12345
( # supergroup to solve for findall's love of tuples
((\d\d\d)|(\(\d\d\d\)))?    # area code (opt)
(\s|-)    # first separator
\d\d\d    # 3 dig
-    # separator
\d\d\d\d    # last 4 dig
(((ext(\.)?\s)|x) (\d{1,5}))?   # extension (opt)
)
''',re.VERBOSE)
# Create a regex object for email addresses
emailReg = re.compile(r'''
[a-zA-Z0-9_.+]*    # username
@    # @
[a-zA-Z0-9_.+]*    # domain name
\. # dot
[a-zA-Z]* # Top Level Domain - ends with an alpha character 
''', re.VERBOSE)
# Get the text off the clipboard
text = pyperclip.paste()
# Extract email addresses/ phone numbers
extractPhoneList = phoneReg.findall(text)
extractEmailList = emailReg.findall(text)

justPhonesList = []

# findall returns each phone num as a nested list w/ each group,
# extractPhoneList[0][0] (for example) will return the full phone number only

for phoneNum in extractPhoneList: 
    justPhonesList.append(phoneNum[0])

# Copy extracted emails & phone numbers to clipboard
results = ' '.join(justPhonesList) + ' ' + ' '.join(extractEmailList)
pyperclip.copy(results)
