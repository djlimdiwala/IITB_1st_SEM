import numpy as np
import pickle
import csv
import matplotlib.pyplot as plt
import pandas as pd

def get_feature_matrix(file_path):
    


  tr = open("matrix_maker.csv")
  train = csv.reader(tr, delimiter=';')
  maker = list(train)
  maker = np.array(maker)[1:,1:]
  maker = np.array(maker, dtype= float)
  # maker = np.array(maker , dtype = 'int32')
  # print (maker.shape)


  # print (maker)
  tr = open(file_path)
  train = csv.reader(tr)
  data = list(train)
  data = np.array(data)[1:,1:]
  rows, cols = data.shape
  t = np.zeros((rows, 1)) 
  tt1 = np.zeros((rows, 1))
  tt2 = np.zeros((rows, 1)) 
  tt3 = np.zeros((rows, 1)) 
  for i in range(rows):
    temp = str(data[i,0]).split(" ") 
    temp2 = str(temp[1]).split(":") 
    t[i] = temp2[0]
    if int(temp2[0])<= 5:
       tt1[i] = 1
    if int(temp2[0]) > 5 and int(temp2[0]) <=11:
       tt1[i] = 2
    if int(temp2[0]) >11 and int(temp2[0]) <= 17:
       tt1[i] = 3
    if int(temp2[0]) >17 and int(temp2[0]) <= 23:
       tt1[i] = 4
    # tt1[i] = int(int(temp2[0])) / 6 + 1
    temp2 = str(temp[0]).split("-")
    tt2[i] = temp2[1]
    tt3[i] = temp2[2]
  


  t = np.concatenate((t, tt1), axis=1)
  t = np.concatenate((t, tt2), axis=1)  
  t = np.concatenate((t, tt3), axis=1)
  data = np.concatenate((t, data[:,1:]), axis=1)
  data = np.array(data, dtype = float)
  # print (data.shape)


  print (data[:,2])

  r,c = maker.shape
  rows, cols = data.shape
  matrix = np.zeros((rows,r) ,dtype = float)

  for i in range(r):
    t = np.ones((rows,1) ,dtype = float)

    for j in range(c):
      if int(maker[i][j]) != -1:

        p = np.ones((rows,1) ,dtype = float)

        for g in range(rows):
          p[g] = data[g,int(maker[i][j])]
        t = t * p
      else:
        break
    # print (t.shape)
    for g in range(rows):
      matrix[g,i] = t[g]
      

  return matrix


feature_matrix =  get_feature_matrix("test_features.csv")




tr = open("test_features.csv")
train = csv.reader(tr)
data = list(train)
data = np.array(data)[1:,1:]
rows, cols = data.shape
t = np.zeros((rows, 1)) 
tt1 = np.zeros((rows, 1)) 
tt2 = np.zeros((rows, 1)) 
tt3 = np.zeros((rows, 1)) 
for i in range(rows):
  temp = str(data[i,0]).split(" ") 
  temp2 = str(temp[1]).split(":") 
  t[i] = temp2[0]
  if int(temp2[0])<= 5:
      tt1[i] = 1
  if int(temp2[0]) > 5 and int(temp2[0]) <=11:
      tt1[i] = 2
  if int(temp2[0]) >11 and int(temp2[0]) <= 17:
      tt1[i] = 3
  if int(temp2[0]) >17 and int(temp2[0]) <= 23:
      tt1[i] = 4
  # tt1[i] = int(temp2[0]) / 6 + 1
  temp2 = str(temp[0]).split("-")
  tt2[i] = temp2[1]
  tt3[i] = temp2[2]
  


t = np.concatenate((t, tt1), axis=1)
t = np.concatenate((t, tt2), axis=1)  
t = np.concatenate((t, tt3), axis=1)



data = np.concatenate((t, data[:,1:]), axis=1)
data = np.array(data, dtype = float)
# rows, cols = data.shape
# for i in range(cols):
#   max = np.amax(data[:,i])
#   min = np.amin(data[:,i])

#   for j in range(rows):

#     data[j,i] = (data[j,i] - min) / (max - min)



print (feature_matrix.shape)
print (data.shape)


rows, cols = data.shape
tt = np.ones((rows, 1))
feature_matrix = np.concatenate((data, feature_matrix), axis=1)


rows , cols = feature_matrix.shape
for i in range(cols):
  max = np.max(feature_matrix[:,i])
  min = np.min(feature_matrix[:,i])
  print (str(i) + "  " +str(max) + "   " + str(min))
  # print (min)
  for j in range(rows):

    feature_matrix[j,i] = (feature_matrix[j,i] - min) / (max - min)

feature_matrix = np.concatenate((tt, feature_matrix) , axis = 1)
tr = open("www.csv")
train = csv.reader(tr , delimiter=';')
ww = list(train)
# print (ww)
ww = np.array(ww)[1:,1:]
ww = np.array(ww , dtype = float)


# print (ww)
yy = np.dot(feature_matrix,ww)
print (yy)
dataframe = pd.DataFrame(data=yy.astype(float))
dataframe.to_csv('yy.csv', sep=';')