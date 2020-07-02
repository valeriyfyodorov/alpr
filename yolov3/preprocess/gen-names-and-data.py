
# Creating files obj.data and obj.names
# for training in Darknet framework
#
# Algorithm:
# Setting up full paths --> Reading file classes.txt -->
# Result:
# Files obj.names and obj.data needed to train



# Full or absolute path to the folder with images
# Find it with Py file getting-full-path.py
# Pay attention! If you're using Windows, yours path might looks like:
# r'C:\Users\my_name\OIDv4_ToolKit\OID\Dataset\train\Car_Bicycle_wheel_Bus'
# or:
# 'C:\\Users\\my_name\\OIDv4_ToolKit\\OID\\Dataset\\train\\Car_Bicycle_wheel_Bus'
full_path_to_images = \
    '/Users/valera/Documents/venprojs/alpr/imgs/contrasted/augmented'
full_path_to_config_files = \
    '/Users/valera/Documents/venprojs/alpr/yolov3/data'

# Defining counter for classes
c = 0
with open(full_path_to_config_files + '/' + 'obj.names', 'w') as names, \
    open(full_path_to_config_files + '/' + 'classes.txt', 'r') as txt:
    for line in txt:
        names.write(line)  # Copying all info from file txt to names
        c += 1


with open(full_path_to_config_files + '/' + 'obj.data', 'w') as data:
    data.write('classes = ' + str(c) + '\n')
    data.write('train = ' + full_path_to_config_files + '/' + 'train.txt' + '\n')
    data.write('valid = ' + full_path_to_config_files + '/' + 'valid.txt' + '\n')
    data.write('names = ' + full_path_to_config_files + '/' + 'classes.names' + '\n')
    data.write('backup = backup')
