import os 
import getcolor
import recon
from os.path import join as pjoin 
from scipy import misc 
 
def load_color(color_dir,list):
    
    #filename='D:\OneDrive\COMPYear3Sem1\COMP3122\project\images.jpg'
    recon.photo_process(color_dir)
    color_dir='D:\OneDrive\COMPYear3Sem1\COMP3122\project'
    count = 0 
    for dir in os.listdir(color_dir):   
        img_dir =pjoin(color_dir, dir)   
        #image = getcolor.Image.open('D:\OneDrive\COMPYear3Sem1\COMP3122\project\Mouth2.jpg')
        image = getcolor.Image.open('D:\OneDrive\COMPYear3Sem1\COMP3122\project\Mouth2.jpg')
        image = image.convert('RGB') 
        get=getcolor.get_dominant_color(image) 
        list.append(get) 
        count = count+1 
        #print(person_dir) 
    #print(count) 
    return count 
 
def Mean_color(count,list): 
     Mean_R=Mean_G=Mean_B=0 
     for i in range(count): 
        tuple=list[i] 
        Mean_R+=tuple[0] 
        Mean_G+=tuple[1] 
        Mean_B+=tuple[2] 
     MeanC=((int)(Mean_R/count),(int)(Mean_G/count),(int)(Mean_B/count)) 
     return MeanC
