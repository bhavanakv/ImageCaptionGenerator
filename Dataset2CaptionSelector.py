import shutil
import os

print("**** Starting selection of captions ****")
image_path = './Data/Images_Dataset2/'
src_captions_path = './Data/annotations_complete_eng/'
trg_captions_path = './Data/captions_Dataset2'
images = os.listdir(image_path)
image_names = [image[:-4] for image in images]
print("Number of images for which captions are to be picked: " + str(len(image_names)))
caption_folders = os.listdir()

caption_folder_name = 0
count = 0
while caption_folder_name <= 40:
    if caption_folder_name < 10:
        src = '0' + str(caption_folder_name)
    else:
        src = str(caption_folder_name)
    src_path = src_captions_path + src
    print("Starting with folder: " + src)
    caption_folder_name += 1
    files=os.listdir(src_path)
    for fname in files:
        if fname[:-4] in image_names:
            shutil.copy2(os.path.join(src_path,fname), trg_captions_path)
            count += 1
print("Number of captions picked: " + str(count))

print("**** Completed caption selection ****")
    
    

