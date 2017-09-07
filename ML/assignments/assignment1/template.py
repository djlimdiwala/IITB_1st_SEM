#!/bin/python3

import numpy as np
import pickle
import csv
import pandas as pd

m_size = 29 + 38

nr = 13000
nc = 0







def get_output(file_path):

  feature_matrix = get_feature_matrix(file_path)
  tr = open(file_path)
  train = csv.reader(tr)
  data = list(train)
  # print (output)
  data = np.array(data)[1:,1:26]
  rows, cols = data.shape
  t = np.zeros((rows, 1)) 
  tt1 = np.zeros((rows, 1)) 
  tt2 = np.zeros((rows, 1)) 
  tt3 = np.zeros((rows, 1)) 
  for i in range(rows):
    temp = str(data[i,0]).split(" ") 
    temp2 = str(temp[1]).split(":") 
    t[i] = temp2[0]
    if int(temp2[0]) <= 5:
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
  feature_matrix = np.concatenate((data, feature_matrix) , axis = 1)
  rows , cols = feature_matrix.shape
  for i in range(cols):
    max = np.max(feature_matrix[:,i])
    min = np.min(feature_matrix[:,i])
    for j in range(rows):

      feature_matrix[j,i] = (feature_matrix[j,i] - min) / (max - min)



  qq = np.ones((rows,1))
  feature_matrix = np.concatenate((qq,feature_matrix) , axis = 1)
  wwww = pickle.load( open( "weight.pickle", "rb" ) )
  w = wwww["weight"]
  yyy = np.dot( feature_matrix, w)

  return yyy



def get_feature_matrix(file_path):
    




  tr = open("matrix_maker.csv")
  train = csv.reader(tr, delimiter=';')
  maker = list(train)
  maker = np.array(maker)[1:,1:]
  maker = np.array(maker, dtype= float)
  tr = open(file_path)
  train = csv.reader(tr)
  data = list(train)
  # output = np.array((13000,1))
  # output = np.array(data)[1:,26]
  # output = np.array(output, dtype = float)
  # output = output.reshape(13000,1)
  # data = np.array(data)[1:,1:]
  # rows, cols = data.shape
  # print (output)
  data = np.array(data)[1:,1:]
  rows, cols = data.shape
  # print (rows,cols)
  data = np.array(data)[0:,0:26]
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
    temp2 = str(temp[0]).split("-")
    tt2[i] = temp2[1]
    tt3[i] = temp2[2]

  t = np.concatenate((t, tt1), axis=1)
  t = np.concatenate((t, tt2), axis=1)  
  t = np.concatenate((t, tt3), axis=1)
  data = np.concatenate((t, data[:,1:]), axis=1)
  data = np.array(data, dtype = float)


  rows, cols = data.shape


 
  # counter = 0
  # rows, cols = data.shape
  # med = np.median(output)
  # for i in range(rows):
  #   if output[counter] > med + 150:
  #     output = np.delete(output, (counter), axis=0)
  #     data = np.delete(data, (counter), axis=0)

  #   else:
  #     counter = counter + 1

  rows, cols = data.shape



  r,c = maker.shape
  rows, cols = data.shape
  matrix = np.zeros((rows,r) ,dtype = float)
  counter = 0
  c = 5
  for i in range(r):
    t = np.ones((rows,1) ,dtype = float)

    for j in range(c-3):
      counter = counter + 1
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
  
  # qq = np.ones((rows,1))
  # matrix = np.concatenate((qq, matrix), axis=1)

  return matrix



def grad(w, phi, y, lam, p):
  
  # reg = np.dot((p*lam) , w)
  # reg = np.array(reg, dtype = float)
  reg = (p * lam) * np.linalg.norm(w)
  a = np.dot(phi, w)
  b = a - y
  # print (b.shape)
  b.reshape(1,1)
  c = b * phi
  d = 2 * c
 
  temp = d + reg
  return temp.transpose()




# def get_output(file_path):





def get_weight_vector(feature_matrix, output, lambda_reg, p):
  
    epochs = 20
    w = np.zeros((m_size,1) , dtype = float)
    eta = 0.001



    if p == 2:
      # print (feature_matrix)
      # for i in range(epochs * nr):
      #   # print (np.mod(i,12999))
      #   p = feature_matrix[np.mod(i,nr),:].reshape(1,m_size)
      #   # p = feature_matrix
      #   dw = grad(w, p, output[np.mod(i,nr)], lambda_reg, 2)
      #   # print (dw)
      #   # tttt = input()
      #   w = w - eta * (dw / nr)


      rows, cols = feature_matrix.shape
      for k in range(epochs):
        for i in range(rows):
          for j in range(cols):
            w[j] = w[j] - 0.001 * (2*(np.dot(feature_matrix[i],w)-output[i])*feature_matrix[i][j]+p*lambda_reg*(w[j]))
    elif p == 1:
      rows, cols = feature_matrix.shape
      for k in range(epochs):
        for i in range(rows):
          for j in range(cols):
            w[j] = w[j] - eta * ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j])

            if w[j] > (lambda_reg * eta / 2):
              w[j] = w[j] - (lambda_reg * eta / 2)

            elif w[j] < (-1 *(lambda_reg * eta / 2)):
              w[j] = w[j] + (lambda_reg * eta / 2)  
              
            else:
              w[j] = 0 


    else:
      rows, cols = feature_matrix.shape
      for k in range(epochs):
        for i in range(rows):
          for j in range(cols):
            if w[j] == 0:
              pp = ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j])
              # pp = np.dot(feature_matrix[j].transpose(),np.dot(feature_matrix,w)-output)
              if pp > 0:
                w[j] = w[j] - eta * ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j] + 1)
              elif pp < 0:
                w[j] = w[j] - eta * ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j] - 1)

              else:
                w[j] = w[j] - eta * ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j])

            else:
              w[j] = w[j] - eta * ((2 * np.dot(feature_matrix[i],w) - output[i]) * feature_matrix[i,j]) + ((p-1) * lambda_reg*  np.power(np.absolute(w[j]),p-2))


    weight  = {"weight":w}
    pickle.dump( weight, open( "weight.pickle", "wb" ))           
    return w

    





    # print (feature_matrix.shape)
    # a = np.dot(feature_matrix.transpose(), feature_matrix)
    # print (a.shape)
    # b = np.dot(lambda_reg, np.identity(m_size))
    # c = np.linalg.inv(a + b)
    # d = np.dot(c , feature_matrix.transpose())
    # ww = np.dot(d , output)

    # return ww







def get_my_best_weight_vector():
  wwww = pickle.load( open( "weight.pickle", "rb" ) )
  return wwww["weight"]
  # print (wwww["weight"])







def build_model():

  feature_matrix =  get_feature_matrix("train.csv")




  tr = open("train.csv")
  train = csv.reader(tr)
  data = list(train)
  output = np.array((13000,1))
  output = np.array(data)[1:,26]
  output = np.array(output, dtype = float)
  output = output.reshape(13000,1)
  # print (output)
  data = np.array(data)[1:,1:26]
  rows, cols = data.shape
  t = np.zeros((rows, 1)) 
  tt1 = np.zeros((rows, 1)) 
  tt2 = np.zeros((rows, 1)) 
  tt3 = np.zeros((rows, 1)) 
  for i in range(rows):
    temp = str(data[i,0]).split(" ") 
    temp2 = str(temp[1]).split(":") 
    t[i] = temp2[0]
    if int(temp2[0]) <= 5:
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
  counter = 0

  rows, cols = data.shape
  # med = np.median(output)
  # print(med)
  # for i in range(rows):
  #   if output[counter] > med + 150 :
  #     output = np.delete(output, (counter), axis=0)
  #     data = np.delete(data, (counter), axis=0)

  #   else:
  #     counter = counter + 1

  rows, cols = data.shape

  feature_matrix = np.concatenate((data, feature_matrix) , axis = 1)
  # feature_matrix = data
  rows , cols = feature_matrix.shape
  for i in range(cols):
    max = np.max(feature_matrix[:,i])
    min = np.min(feature_matrix[:,i])
    # print (str(i) + "  " +str(max) + "   " + str(min))
    # print (min)
    # feature_matrix[:,i] = (feature_matrix[:,i] - np.mean(feature_matrix[:,i]))

    for j in range(rows):

      feature_matrix[j,i] = (feature_matrix[j,i] - min) / (max - min)



  qq = np.ones((rows,1))
  feature_matrix = np.concatenate((qq,feature_matrix) , axis = 1)
  # feature_matrix = data
  dataframe = pd.DataFrame(data=feature_matrix.astype(float))
  dataframe.to_csv('fff.csv', sep=';')

  www = get_weight_vector(feature_matrix, output, 0.001, 2)

  # print (www.shape)


  yyy = np.dot( feature_matrix, www)
  print ("value of w--")
  print (www)
  dataframe = pd.DataFrame(data=www.astype(float))
  dataframe.to_csv('www.csv', sep=';')
  s,r = yyy.shape
  p = 0
  for i in range(s):
     p = p + ((yyy[i] - output[i])**2)

  p = p / nr
  p = p ** 0.5
  print (p)



# build_model()
# print (get_my_best_weight_vector())
# yyy = get_output("test_features.csv")
# print (yyy)

print (np.dot(get_feature_matrix("test_features.csv"), get_my_best_weight_vector()))


