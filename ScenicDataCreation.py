import xml.etree.ElementTree as ET
import os

caption_path = './Data/captions_Dataset2/'
captions_filename = './Data/captions_Dataset2.txt'
files = os.listdir(caption_path)

print("**** Starting extraction of captions ****")
print("Creating captions file")
if os.path.exists(captions_filename):
    os.remove(captions_filename)
    with open(captions_filename, 'w') as file:
        file.write('image,caption\n')

print("Extracting captions from XML files")
with open(captions_filename, 'a') as file:
    for fname in files:
        tree = ET.parse(caption_path + fname,parser=ET.XMLParser(encoding='iso-8859-5'))
        description = tree.find('DESCRIPTION')
        captions = description.text.split(';')
        for caption in captions:
            if len(caption) > 1:
                line = fname[:-4] + '.jpg' + ';' + caption.strip() + '\n'
                file.write(line)
print("**** Completed the captions generation ****") 
    
