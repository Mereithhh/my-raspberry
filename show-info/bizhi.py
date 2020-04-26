import urllib.request
import requests         
import os.path


def save_img(img_url,dirname):
    
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            #print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, '1.jpg')
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError :
        pass
        #print ('文件操作失败',e)
    except Exception :
        pass
        #print ('错误 ：',e)
    #print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    #print('img_url:', img_url)
    return img_url

# 设置图片绝对路径 filepath 所指向的图片为壁纸


def door():
    dirname = r"/root/my-raspberry/show-info/icon/background"       # 图片要被保存在的位置
    img_url = get_img_url()
    save_img(img_url, dirname)   # 图片文件的的路径
    os.system("sudo cp -rf /root/my-raspberry/show-info/icon/background/1.jpg /root/my-raspberry/show-info/icon/background/0.jpg")
    #os.system('open "'+filepath+'"')


