from PIL import Image
import numpy as np
import os
import pandas as pd

dir_path='crown_image1'
files=os.listdir(dir_path)
def loop_through_images():
    for filename in files:
        print(dir_path+filename)
        lstFileNames=filename.split('_')
        lstFileNames=lstFileNames[:-1]
        siteName='_'.join(lstFileNames)
        print(siteName)
        print('================')

def calc_perc(img):
    img = img.convert('L')
    img = np.array(img)
    cnt = np.zeros_like(img)
    sm = np.ones_like(img)
    cnt[img > 150] = 1
    cnt[img <= 150] = 0
    img[img > 150] = 255
    img[img <= 150] = 0

    perc = np.sum(cnt) / np.sum(sm)  # areas without crown
    return (1 - perc)

def loop_through_images():
    cvgdic={}
    for filename in files:
        img=Image.open(dir_path+'/'+filename)
        lstFileNames=filename.split('_')
        lstFileNames=lstFileNames[:-1]
        siteName='_'.join(lstFileNames)
        perc=calc_perc(img)
        if siteName not in cvgdic:
            cvgdic[siteName]=[perc]
        else:
            cvgdic[siteName].append(perc)
    cvgdic=avg(cvgdic)
    return cvgdic

def avg(dic):
    avg_dic={}
    for key in dic:
        lst=dic[key]
        avg=sum(lst)/len(lst)
        avg_dic[key]=avg
    return avg_dic


cvgdic=loop_through_images()
print(cvgdic)
sites=cvgdic.keys()
sites=sorted(sites)
cvg=[]
for site in sites:
    cvg.append(cvgdic[site])


frame=pd.DataFrame({'sites':sites,'coverage':cvg})
frame.to_csv('coverage.csv',index=False,sep=',')





if __name__=='__main__':
    '''img=Image.open('crown_image/MHS_BM_420_W3_3.jpg')
    img=img.convert('L')
    img=np.array(img)
    cnt=np.zeros_like(img)
    sm=np.ones_like(img)
    cnt[img>150]=1
    cnt[img<=150]=0
    img[img>150]=255
    img[img<=150]=0

    perc=np.sum(cnt)/np.sum(sm) #areas without crown

    #img=Image.fromarray(cnt)
    #img.show()'''