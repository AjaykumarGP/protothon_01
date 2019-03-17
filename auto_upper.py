import numpy as np
from PIL import Image
import PIL


def black_white(arr,threshold=150):
#gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
    
    array=arr
    for i in range(len(array)):
        for j in range(len(array[0])):
            red=array[i][j][0]
            green=array[i][j][1]
            blue=array[i][j][2]
            gray=(red*0.299)+(green*0.587)+(blue*0.114)
            array[i][j]=(int(gray),int(gray),int(gray))

            
            '''if (np.all(array[i][j]>threshold)):
                array[i][j]=255
            else:
                array[i][j]=1'''

    return array


data = np.array(Image.open("images/quotes.jpg"))


gray=black_white(data)

result=PIL.Image.fromarray(gray)

result.show()

    