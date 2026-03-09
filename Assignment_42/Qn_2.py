
#dataset
X = [1,2,3,4,5]
Y=[3,4,2,4,5]

n = len(X)

mean_X = sum(X) / n
mean_Y = sum(Y) / n

num = 0
den = 0

for i in range (n):
    num += (X[i] - mean_X) * (Y[i] - mean_Y)
    den += (X[i] -mean_X) **2

m = num/den #slope
c = mean_Y - m * mean_X 

print("Mean of X = ",mean_X)
print("Mean od Y =", mean_Y)

print("\n Slope (m) :",round(m,2))
print("Intercept (c) :", round(c,2))

x_new = 6 
y_pred = m * x_new + c

print("\n predicted Y for X = 6 :", round(y_pred,2))




predicted = []

for x in X:
    predicted.append(m*x+c)

#MSE
mse = sum((Y[i] - predicted[i]) **2 for i in range(n)) / n

#R2
ss_res = sum((Y[i] - predicted[i]) ** 2 for i in range(n))
ss_tot = sum((Y[i] - mean_Y) ** 2 for i in range(n))

r2 = 1 - (ss_res/ss_tot)

print("MSE : ",mse)
print("R2 Score : ", r2)









