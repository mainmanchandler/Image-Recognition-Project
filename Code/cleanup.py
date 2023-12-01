# use this script to clear out all of the output folders

import os
counter = 0
for folder in ['Detected_Objects/', 'Keypoints/', 'Matches/', 'Stitched/']:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) and filename != '.keep':
                os.unlink(file_path)
                counter += 1
        except Exception as e:
            print(e)

print(f'Deleted {counter} files')