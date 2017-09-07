Dhaval Limdiwala
173050061

In feature engineering, one variable is date and time combined. So, I have removed it and added four more variables in data which are month (1 to 12), date(1 to 31), time_hour(0 to 23) and time category(1 to 4).

Here, time category is made because entire day can be divided into four quaters. night, morning, afternoon and evening. So, night -> 1, morning -> 2, afternoon -> 3, evening -> 4. 

------------------------------------------------------------------------

For feature selection, I have taken all combinations of degree 3 under consideration (I have tried upto degree 10 but It wasn't affcting accuracy (In feature_maker.py file)).

I found corelation between features and output. If corelation co-efficient is more than some threshold then , I will select that feature for regression.
For example, x*y is one feature. So, I will calculate value of x*y and then calculate corelation co-efficient. If that co-efficient is greater than threshold(I have taken 0.03), then It will be in feature matrix.

I have selected total 67 features including bias term using this corelation criteria.

------------------------------------------------------------------------

After making feature matrix, I have applied min-max normalization on the feature matrix. After that, I will apply gradient descent algorithm to minimize the value of weight vector.


Here, I have submitted on kaggle with error of 95.79. After that I changed the code and applied other normalization techniques like z-score normalization, decimal scaling, mean sutravtion etc. I also tried removing ouliers. For example, in output of train data, there are many values greater than 300 whereas median and mean of the output are 60 and 90 respectively. So, these higher values change the result significantly even after applying regularization. I tried removing entire row of this outlier but it did not affect. I could not find proper method to handle these outliers.


------------------------------------------------------------------------

WIth parameters set as lambda = 0.01, learning rate = 0.001 and number of epochs 20 over entire data with stchastic gradient descent, I have found following results for different values of p -

p = 1 -> rms = 108.26
p = 1.25 -> rms = 110
p = 1.5 -> rms = 105
p = 1.75 -> rms = 104
p = 2 -> rms = 97.5

For testing data, I have made another file test.py in which just give name of file and you will get results in yy.csv file


