'''
Unable to get the font name and size of paragraphs. Returns NONE
'''

import docx
path = 'C:\Python Files\Automating The Boring Stuff With Python\Chapter 13 - Working with PDF and word Documents\Practice Projects - Working with PDF and Word Documents\Invitation_Template.docx'
doc = docx.Document(path)
for p in doc.paragraphs:
    name = p.style.font.name
    size = p.style.font.size
    print(name, size)
