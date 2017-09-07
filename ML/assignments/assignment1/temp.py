#!/bin/python3

import numpy as np
import pickle
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
import pdb

"""
NOTE: All functions mentioned below MUST be implemented
      All functions must be reproducible, i.e., repeated function calls with the
      same parameters must result in the same output. Look into numpy RandomState
      to achieve this.
"""
m_size = 27




def feature_maker(file_path):
  
  tr = open(file_path)
  train = csv.reader(tr)
  data = list(train)
  output = np.array(data)[1:,26]
  output = np.array(output, dtype = float)
  labels = np.array(data)[0,:]
  labels = np.array(labels)[1:26]
  
  data = np.array(data)[1:,1:26]
  
  rows , cols = data.shape
  t = np.zeros((rows, 1)) 
  tt = np.zeros((rows, 1)) 
  for i in range(rows):
    temp = str(data[i,0]).split(" ")
    temp2 = str(temp[1]).split(":") 
    temp3 = str(temp[0]).split("-")
    t[i] = temp2[0]
    tt[i] = temp3[1]

  t = np.concatenate((tt, t), axis=1)
  data = np.concatenate((t, data[:,1:25]), axis=1)
  data = np.array(data, dtype = float)

  matrix_maker =  np.dot ( -1 , np.ones((1000,10)))
  mm_flag = 0
  # for i in range(cols):
  #   data[:,i] = data[:,i] - np.mean(data[:,i])
  #   data[:,i] = data[:,i] / data[:,i].std()


  #   output = output - np.mean(output)
  #   output = output / output.std()
  # for i in range(cols):
  #   data[:,i] = data[:,i] - np.mean(data[:,i])


  
  # pca = PCA(n_components=17)
  # pca.fit(data)

  # data = pca.transform(data)

  rows , cols = data.shape

  # print (data.shape)
  p = np.zeros((rows,1))
  print (data.shape)
  counter = 0
  threshold = 0.195
  fl = 0
  for i in range(cols):
    
    # p = np.corrcoef(data[:,i], output)[0,1]
    # if abs(p) > threshold:
    #   print ("1--  " + str(labels[i]) + "   " + str(p))
    #   counter = counter + 1
    #   matrix_maker[mm_flag,0] = i
    #   mm_flag = mm_flag + 1

    for j in range(i,cols):
      temp1 = np.multiply(data[:,i],data[:,j])
      p = np.corrcoef(temp1, output)[0,1]
      if abs(p) > threshold:
        print ("2--  " + str(i) + "   " + str(j) + "   " + str(p))
        counter = counter + 1
        fl = fl + 1
        matrix_maker[mm_flag,0] = i
        matrix_maker[mm_flag,1] = j
        mm_flag = mm_flag + 1

      for k in range(j, cols):
        temp2 = np.multiply(temp1,data[:,k])
        p = np.corrcoef(temp2, output)[0,1]
        if abs(p) > threshold:
          print ("3--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(p))
          counter = counter + 1
          fl = fl + 1
          matrix_maker[mm_flag,0] = i
          matrix_maker[mm_flag,1] = j
          matrix_maker[mm_flag,2] = k
          mm_flag = mm_flag + 1

        for m in range(k, cols):
          temp3 = np.multiply(temp2,data[:,m])
          p = np.corrcoef(temp3, output)[0,1]
          if abs(p) > threshold:
            print ("4--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(p))
            counter = counter + 1
            fl = fl + 1
            matrix_maker[mm_flag,0] = i
            matrix_maker[mm_flag,1] = j
            matrix_maker[mm_flag,2] = k
            matrix_maker[mm_flag,3] = m
            mm_flag = mm_flag + 1
          for n in range(m, cols):
            temp4 = np.multiply(temp3,data[:,n])
            p = np.corrcoef(temp4, output)[0,1]
            if abs(p) > threshold:
              print ("5--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " + str(p))
              counter = counter + 1  
              fl = fl + 1
              matrix_maker[mm_flag,0] = i
              matrix_maker[mm_flag,1] = j
              matrix_maker[mm_flag,2] = k
              matrix_maker[mm_flag,3] = m
              matrix_maker[mm_flag,4] = n
              mm_flag = mm_flag + 1

            # for O in range(n, cols):
            #   temp5 = np.multiply(temp4,data[:,O])
            #   p = np.corrcoef(temp5, output)[0,1]
            #   if abs(p) > threshold:
            #     print ("6--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " +  str(O) + "   " + str(p))
            #     counter = counter + 1  
            #     fl = fl + 1
            #     matrix_maker[mm_flag,0] = i
            #     matrix_maker[mm_flag,1] = j
            #     matrix_maker[mm_flag,2] = k
            #     matrix_maker[mm_flag,3] = m
            #     matrix_maker[mm_flag,4] = n
            #     matrix_maker[mm_flag,5] = O
            #     mm_flag = mm_flag + 1

            #   for z in range(O, cols):
            #     temp6 = np.multiply(temp5,data[:,z])
            #     p = np.corrcoef(temp6, output)[0,1]
            #     if abs(p) > threshold:
            #       print ("7--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " +  str(O) + "   " +  str(q) + "   " + str(p))
            #       counter = counter + 1  
            #       fl = fl + 1
            #       matrix_maker[mm_flag,0] = i
            #       matrix_maker[mm_flag,1] = j
            #       matrix_maker[mm_flag,2] = k
            #       matrix_maker[mm_flag,3] = m
            #       matrix_maker[mm_flag,4] = n
            #       matrix_maker[mm_flag,5] = O
            #       matrix_maker[mm_flag,6] = z
            #       mm_flag = mm_flag + 1

            #     for q in range(z, cols):
            #       temp7 = np.multiply(temp6,data[:,q])
            #       p = np.corrcoef(temp7, output)[0,1]
            #       if abs(p) > threshold:
            #         print ("8--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " +  str(O) + "   " +  str(q) + "   " + str(p))
            #         counter = counter + 1  
            #         fl = fl + 1
            #         matrix_maker[mm_flag,0] = i
            #         matrix_maker[mm_flag,1] = j
            #         matrix_maker[mm_flag,2] = k
            #         matrix_maker[mm_flag,3] = m
            #         matrix_maker[mm_flag,4] = n
            #         matrix_maker[mm_flag,5] = O
            #         matrix_maker[mm_flag,6] = z
            #         matrix_maker[mm_flag,7] = q
            #         mm_flag = mm_flag + 1

            #       for qq in range(q, cols):
            #         temp8 = np.multiply(temp7,data[:,q])
            #         p = np.corrcoef(temp8, output)[0,1]
            #         if abs(p) > threshold:
            #           print ("9--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " +  str(O) + "   " +  str(q) + "   " + str(p))
            #           counter = counter + 1  
            #           fl = fl + 1
            #           matrix_maker[mm_flag,0] = i
            #           matrix_maker[mm_flag,1] = j
            #           matrix_maker[mm_flag,2] = k
            #           matrix_maker[mm_flag,3] = m
            #           matrix_maker[mm_flag,4] = n
            #           matrix_maker[mm_flag,5] = O
            #           matrix_maker[mm_flag,6] = z
            #           matrix_maker[mm_flag,7] = q
            #           matrix_maker[mm_flag,8] = qq
            #           mm_flag = mm_flag + 1


            #         for qqq in range(qq, cols):
            #           temp9 = np.multiply(temp8,data[:,q])
            #           p = np.corrcoef(temp9, output)[0,1]
            #           if abs(p) > threshold:
            #             print ("10--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " +  str(O) + "   " +  str(q) + "   " + str(p))
            #             counter = counter + 1  
            #             fl = fl + 1
            #             matrix_maker[mm_flag,0] = i
            #             matrix_maker[mm_flag,1] = j
            #             matrix_maker[mm_flag,2] = k
            #             matrix_maker[mm_flag,3] = m
            #             matrix_maker[mm_flag,4] = n
            #             matrix_maker[mm_flag,5] = O
            #             matrix_maker[mm_flag,6] = z
            #             matrix_maker[mm_flag,7] = q
            #             matrix_maker[mm_flag,8] = qq
            #             matrix_maker[mm_flag,9] = qqq
            #             mm_flag = mm_flag + 1


  total = 25 + 300 + 2300 +12650 + 53130
  print (str(counter) + "   out of   " + str(total))
  m_size = counter
  

  # np.savetxt("matrix_maker.csv", matrix_maker, delimiter=",")
  dataframe = pd.DataFrame(data=matrix_maker[0:m_size,:].astype(float))
  dataframe.to_csv('matrix_maker.csv', sep=';')




feature_cr = np.zeros((100,5))



def get_feature_matrix(file_path):
    




  tr = open("matrix_maker.csv")
  train = csv.reader(tr, delimiter=',')
  maker = list(train)
  maker = np.array(maker)[1:,1:]
  # maker = np.array(maker , dtype = 'int32')
  # print (maker.shape)


  # print (maker)
  tr = open(file_path)
  train = csv.reader(tr)
  data = list(train)
  data = np.array(data)[1:,1:]
  rows, cols = data.shape
  output = np.array(data)[1:,26]
  output = np.array(output, dtype = float)
  max = np.amax(output)
  min = np.amin(output)
  t = np.zeros((rows, 1))
  tt = np.zeros((rows, 1))
  for i in range(rows):
    temp = str(data[i,0]).split(" ") 
    temp2 = str(temp[1]).split(":") 
    t[i] = temp2[0]
    temp3 = str(temp[0]).split("-")
    t[i] = temp2[0]
    tt[i] = temp3[1]

  t = np.concatenate((tt, t), axis=1)
  data = np.concatenate((t, data[:,1:]), axis=1)
  data = np.array(data, dtype = float)
  # print (data.shape)
  rows, cols = data.shape
  for i in range(cols):
    data[:,i] = data[:,i] - np.mean(data[:,i])
    data[:,i] = data[:,i] / data[:,i].std()



  r,c = maker.shape
  
  matrix = np.zeros((rows,r) ,dtype = float)

  for i in range(r):
    t = np.ones((rows,1) ,dtype = float)

    for j in range(c-3):
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
  
  qq = np.ones((rows,1))
  matrix = np.concatenate((qq, matrix), axis=1)


  return matrix

# def get_output(file_path):
#     """
#     file_path: path to a file in the same format as in the Kaggle competition

#     Return: an n x 1 numpy array where n is the number of examples in the file.
#             The array must contain the Output column values of the file

#     NOTE: Preserve the order of examples in the file
#     """



def grad(w, phi, y, lam, p):
  
  # reg = np.dot((p*lam) , w)
  # reg = np.array(reg, dtype = float)
  reg = (p * lam) * np.linalg.norm(w)
  print (reg)
  # print ("flag1")
  # print (p.shape)
  # print ("flag2")
  # print (np.dot(phi, w).shape)
  # print (y.shape)
  # print ((np.dot(phi, w) - y).shape)
  a = np.dot(phi, w)
  b = a - y
  # print (b.shape)
  b.reshape(1,1)
  c = b * phi
  d = 2 * c
 
  temp = d + reg
  # temp = np.add (np.dot (2, np.dot (phi.transpose() , np.dot(phi, w) - y)), reg)
  # print (w.shape)
  return temp.transpose()


def get_weight_vector(feature_matrix, output, lambda_reg, p):
    """
    feature_matrix: an n x m 2-D numpy array where n is the number of samples
                    and m the feature size.
    output: an n x 1 numpy array reprsenting the outputs for the n samples
    lambda_reg: regularization parameter
    p: p-norm for the regularized regression

    Return: an m x 1 numpy array weight vector obtained through stochastic gradient descent
            using the provided function parameters such that the matrix product
            of the feature_matrix matrix with this vector will give you the
            n x 1 regression outputs

    NOTE: While testing this function we will use feature_matrices not obtained
          from the get_feature_matrix() function but you can assume that all elements
          of this matrix will be of type float
    # """
    # epochs = 10
    # w = np.zeros((m_size,1) , dtype = float)
    # print ("flag1")
    # print (lambda_reg)
    # print ("flag2")
    # eta = 0.5
    # print (feature_matrix)
    # for i in range(20):
    #   p = feature_matrix[i,:].reshape(1,m_size)
    #   # p = feature_matrix
    #   dw = grad(w, p, output[i], lambda_reg, 2)
    #   # print (dw)
    #   tttt = input()
    #   w = w - eta * dw

    # return w




# def coefficients_sgd(train, l_rate, n_epoch):
#   coef = [0.0 for i in range(len(train[0]))]
#   for epoch in range(n_epoch):
#     sum_error = 0
#     for row in train:
#       yhat = predict(row, coef)
#       error = yhat - row[-1]
#       sum_error += error**2
#       coef[0] = coef[0] - l_rate * error


#       for i in range(len(row)-1):
#         coef[i + 1] = coef[i + 1] - l_rate * error * row[i]

#     print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
#   return coef






    a = np.dot(feature_matrix.transpose(), feature_matrix)
    print (a.shape)
    b = np.dot(lambda_reg, np.identity(m_size))
    c = np.linalg.inv(a + b)
    d = np.dot(c , feature_matrix.transpose())
    ww = np.dot(d , output)

    return ww






def get_my_best_weight_vector():
    """
    Return: your best m x 1 numpy array weight vector used to predict the output for the
            kaggle competition.

            The matrix product of the feature_matrix, obtained from get_feature_matrix()
            call with file as test_features.csv, with this weight vector should
            result in you best prediction for the test dataset.

    NOTE: For your final submission you are expected to provide an output.csv containing
          your predictions for the Kaggle test set and the weight vector returned here
          must help us to EXACTLY reproduce that output.csv

          We will also be using this weight to evaluate on a separate hold out test set

          We expect this function to return fast. So you are encouraged to return a pickeled
          file after all your experiments with various values of p and lambda_reg.
    """




# tr = open("train.csv")
# train = csv.reader(tr)
# data = list(train)

# # print (output)
# data = np.array(data)[1:,1:26]
# rows, cols = data.shape
# t = np.zeros((rows, 1)) 
# for i in range(rows):
#   temp = str(data[i,0]).split(" ") 
#   temp2 = str(temp[1]).split(":") 
#   t[i] = temp2[0]
# data = np.concatenate((t, data[:,1:]), axis=1)
# data = np.array(data, dtype = float)


# for i in range(cols):
#   data[:,i] = data[:,i] - np.mean(data[:,i])
#   data[:,i] = data[:,i] / data[:,i].std()


  
# pca = PCA(n_components=17)
# pca.fit(data)

# pp = pca.transform(data)

# print (pp)




feature_maker("train.csv")






# feature_matrix =  get_feature_matrix("train.csv")

# # print (feature_matrix.shape)

# tr = open("train.csv")
# train = csv.reader(tr)
# data = list(train)
# output = np.array((13000,1))
# output = np.array(data)[1:,26]
# output = np.array(output, dtype = float)
# output = output.reshape(13000,1)
# # print (output)
# data = np.array(data)[1:,1:26]
# rows, cols = data.shape
# t = np.zeros((rows, 1)) 
# tt = np.zeros((rows, 1)) 
# for i in range(rows):
#   temp = str(data[i,0]).split(" ") 
#   temp2 = str(temp[1]).split(":") 
#   t[i] = temp2[0]
#   temp3 = str(temp[0]).split("-")
#   t[i] = temp2[0]
#   tt[i] = temp3[1]

# t = np.concatenate((tt, t), axis=1)
# data = np.concatenate((t, data[:,1:]), axis=1)
# data = np.array(data, dtype = float)

# # # for i in range(cols):
# # #   data[:,i] = data[:,i] - np.mean(data[:,i])

# # print (data.std())
# # (Pdb) continue
# # # pca = PCA(n_components=23)
# # # pca.fit(data)

# # # data = pca.transform(data)


# # tt = np.ones((rows, 1))
# feature_matrix = np.concatenate((tt, data), axis=1)
# feature_matrix = np.concatenate((data, feature_matrix) , axis = 1)


# dataframe = pd.DataFrame(data=feature_matrix.astype(float))
# dataframe.to_csv('fff.csv', sep=';')

# # # plt.scatter(data[:,0],output)
# # # plt.show()
# # # print (feature_matrix)
# www = get_weight_vector(feature_matrix, output, 0.005, 2)

# # print (www.shape)


# yyy = np.dot( feature_matrix, www)
# dataframe = pd.DataFrame(data=www.astype(float))
# dataframe.to_csv('www.csv', sep=';')

# print (yyy)

# s,r = yyy.shape
# p = 0
# for i in range(s):
#    p = p + ((yyy[i] - output[i])**2)

# p = p / 13000
# p = p ** 0.5


# print (p)


# # # dataframe = pd.DataFrame(data=ww.astype(float))
# # # dataframe.to_csv('output.csv', sep=';')







