import os
from PIL import Image
import glob

class Get_Files:
    files = ""
    def __init__(self):
        self.working_path=os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.working_path)
    
    def get_files(self, format):
        self.format = format
        if self.format== "J":
            Get_Files.files = glob.glob("*.jpg")
        elif self.format == "P":
            Get_Files.files = glob.glob("*.png")
        else:
            print("error")
        print(Get_Files.files)
    
class Merge:
    def __init__(self):
        self.files = Get_Files.files
                  
    def model_chose(self):
        while True:
            print(f"初始化完成......\n请选择你的拼接模式：\n defult or middle")
            self.model = input()
            try:
                if self.model == "defult":
                    self.model_bur = True
                    break
                elif self.model == "middle":
                    self.model_bur = False
                    break
            except:
                continue

    def get_maxsize(self):
        pic_sizes=[]
        pic_y=[]
        for file in self.files:
            with Image.open(file,mode = "r") as pic:
                pic_sizes.append(pic.size)
                pic_y.append(pic.size[1])
                self.x_size = max(pic_sizes, key = lambda x: x[0])[0]
                self.y_size = sum(pic_y)
    
    def merge(self):
        self.new_pic = Image.new("RGB", (self.x_size, self.y_size), color="white")
        y_count = 0
        for file in self.files:
            try:
                with Image.open(file,mode = "r") as im:
                    if self.model_bur:
                        self.x_position = 0
                    elif not self.model_bur:
                        self.x_position = (self.x_size - im.size[0]) / 2
                    self.new_pic.paste(im, (int(self.x_position), y_count))
                    y_count += im.size[1]
            except:
                print("图片 {} 加载失败，已跳过".format(file))
                continue
    
    def save(self, saving_dir):
        self.new_pic.save("{}/new1.jpg".format(saving_dir))
        
if __name__ == "__main__":
    get_files_obj = Get_Files()
    print("请输入需要拼接的图片格式：jpg->J|png->P")
    format = input()
    get_files_obj.get_files(format)
    merge_obj = Merge()
    merge_obj.model_chose()
    merge_obj.get_maxsize()
    merge_obj.merge()
    merge_obj.save(get_files_obj.working_path)