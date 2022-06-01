import numpy as np
import cv2
import os


def img_BGR2GRAY(DATADIR, data_k, img_size):
    w=img_size[0]
    h=img_size[1]
    path=os.path.join(DATADIR, data_k)
    img_list=os.listdir(path)
    
    for i in img_list:
        if i.endswith('.PNG'):
            img_array=cv2.imread((path + '/' + i),cv2.IMREAD_COLOR) #先讀取 指定路徑內 的檔案
            new_array=cv2.resize(img_array,(w,h),interpolation=cv2.INTER_CUBIC) #更改 指定路徑內 的圖片尺寸為(0,1)
            gray = cv2.cvtColor(new_array, cv2.COLOR_BGR2GRAY) #更改 指定路徑內 的圖片顏色(彩階 > 灰階)
            img_name=str(i) 
            
            save_path=path + '_BGR2GRAY/' #指定更改完成的圖片要存放的 新路徑位置
            
            #創造 新路徑位置 並將 修正完的新圖片 放置進去
            if os.path.exists(save_path):
                print(i)
                save_img=save_path + img_name
                cv2.imwrite(save_img, gray)
            else:
                os.mkdir(save_path)
                save_img=save_path + img_name
                cv2.imwrite(save_img, gray)
                
    #更改 新路徑位置內 的 新圖片名稱            
    print(f"Before Renaming: {img_list}")
    for i in range(len(img_list)):
        os.rename(save_path+img_list[i], f"{save_path}{i+1}.PNG")
    print(f"After Renaming: {os.listdir(save_path)}")

#主程式
if __name__ == '__main__':
    DATADIR= "C:/Users/user/"
    data_k= "D403"
    img_size=[512,512]
    img_BGR2GRAY(DATADIR, data_k, img_size)
