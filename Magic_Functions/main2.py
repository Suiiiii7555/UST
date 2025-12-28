import os
from PIL import Image
class ImageDataset:
    def __init__(self, root):
        self.root = root
        self.filenames = os.listdir(self.root)

    def __len__(self):
        return len(self.filenames)
    
    def __getitem__(self,index):
        img = Image.open(self.root + "/" + self.filenames[index])
        return img

ds = ImageDataset("images")
print(f"The files in the folder are : {ds.filenames}")
print(f"The length / number of files in the images folder are : {len(ds)}")
img = ds[0]
print(f"The file with index 0 in the folder is {img.show}")