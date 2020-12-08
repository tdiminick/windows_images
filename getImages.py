import shutil
import glob
import os

dir = r"C:\Users\tdimi\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\\"
dest = r"E:\python\windows_images\images\\"

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

for file in glob.glob(dir + "*"):
    if os.path.getsize(file) > 150000:
        fileName = file[len(dir):]
        newFile = dest[:-1] + fileName + ".jpg"
        if not os.path.isfile(newFile):
            print(file + "\n")
            print(newFile + "\n\n")
            copyFile(file, newFile)
