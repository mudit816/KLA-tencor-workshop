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
count_of_image=5
filename="impure_data_record.csv"
img_data_temp=Image.open('wafer_image_2.png')
numpydatatemp=asarray(img_data_temp)
img_data=Image.open('wafer_image_1.png')
numpydata=asarray(img_data)


for i in range(col_count):
    for j in range(row_count):
        r=numpydata[i][j][0]
        b=numpydata[i][j][1]
        g=numpydata[i][j][2]
        r1=numpydatatemp[i][j][0]
        b1=numpydatatemp[i][j][1]
        g1=numpydatatemp[i][j][2]           
        flag=False
        if r==r1 and b==b1 and g==g1:
            flag=True
        if flag==False:
            impure_points=[]
            impure_points.append(1)
            impure_points.append(i)
            impure_points.append(j)
            points_of_impurity.append(impure_points)


for k in range(1,count_of_image-1):
    img=k+1
    prev_img=k
    next_img=img+1
    str1=name+str(img)+".png"
    str2=name+str(prev_img)+".png"
    str3=name+str(next_img)+".png"
    print(str1)
    print(str2)
    print(str3)
    img_data1=Image.open(str1)
    img_data2=Image.open(str2)
    img_data3=Image.open(str3)
    numpydata1=asarray(img_data1)
    numpydata2=asarray(img_data2)
    numpydata3=asarray(img_data3)
    for i in range(col_count):
        for j in range(row_count):
            curr_r=numpydata1[i][j][0]
            curr_b=numpydata1[i][j][1]
            curr_g=numpydata1[i][j][2]
            prev_r=numpydata2[i][j][0]
            prev_b=numpydata2[i][j][1]
            prev_g=numpydata3[i][j][2]
            next_r=numpydata3[i][j][0]
            next_b=numpydata3[i][j][1]
            next_g=numpydata3[i][j][2]
            flag=False
            if (curr_r==next_r and curr_g==next_g and curr_b==next_b) or (curr_r==prev_r and curr_g==prev_g and curr_b==prev_b):
                flag=True
            if flag==False:
                impure_points=[]
               # print(r,b,g)
                print(curr_r,curr_b,curr_g,"image",k)
                print(next_r,next_b,curr_g,"oldimage")
                impure_points.append(img)
                impure_points.append(i)
                impure_points.append(j)
                points_of_impurity.append(impure_points)

img_data_temp=Image.open('wafer_image_4.png')
numpydatatemp=asarray(img_data_temp)
img_data=Image.open('wafer_image_5.png')
numpydata=asarray(img_data)
for i in range(col_count):
    for j in range(row_count):
        r=numpydata[i][j][0]
        b=numpydata[i][j][1]
        g=numpydata[i][j][2]
        r1=numpydatatemp[i][j][0]
        b1=numpydatatemp[i][j][1]
        g1=numpydatatemp[i][j][2]           
        flag=False
        if r==r1 and b==b1 and g==g1:
            flag=True
        if flag==False:
            impure_points=[]
            impure_points.append(count_of_image)
            impure_points.append(i)
            impure_points.append(j)
            points_of_impurity.append(impure_points)

with open(filename,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows(points_of_impurity)

