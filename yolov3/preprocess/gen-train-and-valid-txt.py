
# Creating files train.txt and valid.txt
# for training in Darknet framework
#
# Algorithm:
# Setting up full paths --> List of paths -->
# --> Extracting 15% of paths to save into valid.txt file -->
# --> Writing paths into train and test txt files
#
# Result:
# Files train.txt and valid.txt with full paths to images
import os
full_path_to_images = \
    '/Users/valera/Documents/venprojs/alpr/imgs/contrasted/augmented'
full_path_to_config_files = \
    '/Users/valera/Documents/venprojs/alpr/yolov3/data'

print(os.getcwd())
os.chdir(full_path_to_images)
print(os.getcwd())

p = []

# Using os.walk for going through all directories
# and files in them from the current directory
# Fullstop in os.walk('.') means the current directory
for current_dir, dirs, files in os.walk('.'):
    # Going through all files
    for f in files:
        if f.endswith('.jpg') or f.endswith('.jpeg'):
            path_to_save_into_txt_files = full_path_to_images + '/' + f
            p.append(path_to_save_into_txt_files + '\n')

# Slicing first 15% of elements from the list
p_valid = p[:int(len(p) * 0.15)]
p = p[int(len(p) * 0.15):]

# Creating file train.txt and writing 85% of lines in it
with open(full_path_to_config_files + '/train.txt', 'w') as train_txt:
    for e in p:
        train_txt.write(e)

with open(full_path_to_config_files + '/valid.txt', 'w') as valid_txt:
    for e in p_valid:
        valid_txt.write(e)

