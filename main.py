from PIL import Image 
from numpy import asarray
import json 
f=open('input.json',)
data=json.load(f)
row_count=data['die']['width']
col_count=data['die']['height']
rows=data['die']['rows']
col=data['die']['columns']
print(row_count,col_count)
not_impure=[]
not_impure.append(255)
not_impure.append(128)
points_of_impurity=[]
img_data=Image.open('wafer_image_1.png')
numpydata=asarray(img_data)
for j in range(col_count):
    for i in range(row_count):
        list1=numpydata[j][i]
        flag=True
        for pixels in list1:
            if pixels not in not_impure:
                flag=False
                break
        if flag==False:
            impure_points=[]
            impure_points.append(i)
            impure_points.append(j)
            points_of_impurity.append(impure_points)
print(points_of_impurity)

