from PIL import Image 
from numpy import asarray
import csv
import json 
f=open('input.json',)
data=json.load(f)
row_count=data['die']['width']
col_count=data['die']['height']
rows=data['die']['rows']
col=data['die']['columns']
print(row_count,col_count)
print(row_count,col_count)
name="wafer_image_"
not_impure=[]
fields=['Dice','X','Y']
not_impure.append(255)
not_impure.append(128)
points_of_impurity=[]
count_of_image=2
filename="impure_data_record.csv"
img_data_temp=Image.open('wafer_image_1.png')
numpydatatemp=asarray(img_data_temp)
for k in range(count_of_image):
    k=k+1
    st=str(k)
    str1=name+st+".png"
    img_data=Image.open(str1)
    numpydata=asarray(img_data)
    for i in range(col_count):
        for j in range(row_count):
            r=numpydata[i][j][0]
            b=numpydata[i][j][1]
            g=numpydata[i][j][2]
            #print(r,b,g,"image",k)
            r1=numpydatatemp[i][j][0]
            b1=numpydatatemp[i][j][1]
            g1=numpydatatemp[i][j][2]           
            flag=False
            if r==r1 and b==b1 and g==g1:
                flag=True
            if flag==False:
                impure_points=[]
               # print(r,b,g)
                print(r,b,g,"image",k)
                print(r1,b1,g1,"oldimage")
                impure_points.append(k)
                impure_points.append(i)
                impure_points.append(j)
                points_of_impurity.append(impure_points)
with open(filename,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows(points_of_impurity)

