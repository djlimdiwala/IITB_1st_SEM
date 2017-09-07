import numpy as np
import pickle
import csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
import pdb


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
  tt1 = np.zeros((rows, 1)) 
  tt2 = np.zeros((rows, 1)) 
  tt3 = np.zeros((rows, 1)) 
  for i in range(rows):
    temp = str(data[i,0]).split(" ")
    temp2 = str(temp[1]).split(":") 
    temp3 = str(temp[0]).split("-")
    t[i] = temp2[0]
    tt1[i] = int(temp2[0]) / 4 + 1
    tt2[i] = temp3[1]
    tt3[i] = temp3[2]

  t = np.concatenate((t, tt1), axis=1)
  t = np.concatenate((t, tt2), axis=1)  
  t = np.concatenate((t, tt3), axis=1)
  data = np.concatenate((t, data[:,1:25]), axis=1)
  data = np.array(data, dtype = float)
  rows , cols = data.shape
  matrix_maker =  np.dot ( -1 , np.ones((10000,10)))
  mm_flag = 0




  data1 = np.array(data)
 
  
  output1 = np.array(output)

  counter = 0
  for i in range(rows):

    if output[counter] > 300: 
      data = np.delete(data, (counter), axis = 0)
      output = np.delete(output, (counter), axis = 0)
    
    else:
      counter = counter + 1

      print(counter)
  # print (data1.shape)
  # data = np.array(data1)
  # output = np.array(output1)
  # data = np.matrix(data)
  # output = np.matrix(output)
  rows , cols = data.shape
  print (output.shape)
  # print (data.shape)
  p = np.zeros((rows,1))
  print (data.shape)
  counter = 0
  threshold = 0.03
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

      if i == j:
        p = np.corrcoef(temp1, output)[0,1]
        if abs(p) > threshold:
          print ("2--  " + str(i) + "   " + str(j) + "   " + str(p))
          counter = counter + 1
          fl = fl + 1
          matrix_maker[mm_flag,0] = i
          matrix_maker[mm_flag,1] = j
          mm_flag = mm_flag + 1


        for k in range(j, cols):
          if j == k: 
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

        # for m in range(k, cols):
        #   temp3 = np.multiply(temp2,data[:,m])
        #   p = np.corrcoef(temp3, output)[0,1]
        #   if abs(p) > threshold:
        #     print ("4--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(p))
        #     counter = counter + 1
        #     fl = fl + 1
        #     matrix_maker[mm_flag,0] = i
        #     matrix_maker[mm_flag,1] = j
        #     matrix_maker[mm_flag,2] = k
        #     matrix_maker[mm_flag,3] = m
        #     mm_flag = mm_flag + 1
        #   for n in range(m, cols):
        #     temp4 = np.multiply(temp3,data[:,n])
        #     p = np.corrcoef(temp4, output)[0,1]
        #     if abs(p) > threshold:
        #       print ("5--  " + str(i) + "   " + str(j) + "   " + str(k) + "   " + str(m) + "   " + str(n) + "   " + str(p))
        #       counter = counter + 1  
        #       fl = fl + 1
        #       matrix_maker[mm_flag,0] = i
        #       matrix_maker[mm_flag,1] = j
        #       matrix_maker[mm_flag,2] = k
        #       matrix_maker[mm_flag,3] = m
        #       matrix_maker[mm_flag,4] = n
        #       mm_flag = mm_flag + 1

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
  
  print (matrix_maker.shape)
  # np.savetxt("matrix_maker.csv", matrix_maker, delimiter=",")
  dataframe = pd.DataFrame(data=matrix_maker[0:m_size,:].astype(float))
  dataframe.to_csv('matrix_maker.csv', sep=',')
  return matrix_maker[0:m_size,:]

p = feature_maker("train.csv")
print (p.shape)