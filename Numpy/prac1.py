import numpy as np
x = np.array([1 , 2 , 3 , 4 , 5],dtype = float)
y = np.array([6 , 7 , 8 , 9 , 10],dtype = float)
x = x.reshape(-1,1)
y = y.reshape(-1,1)
m = x.shape[0]
w = 0.0
b = 0.0

def predict(x,w,b):
    return x*w+b

def compute_cost(x,y,w,b):
    y_pred = predict(x,w,b)
    cost = (1/m)*np.sum((y_pred - y)**2)
    return cost

def Compute_Gradients(x,y,w,b):
    y_pred = predict(x,w,b)

    dw = (2/m)*np.sum((y_pred - y)*x)
    db = (2/m)*np.sum(y_pred - y)

    return dw,db

learing_rate = 0.01
epochs = 1000

for i in range(epochs):
    dw,db = Compute_Gradients(x,y,w,b)
    w = w - learing_rate*dw
    b = b - learing_rate*db
    if i%100 == 0:
        cost = compute_cost(x,y,w,b)
        print(f"Epoch {i}: cost = {cost:.4f}")
print("leaned weight - ",w)
print("leaned bias - ",b)
x_test = np.array([6,7,8]).reshape(-1,1)
y_pred = predict(x_test,w,b)
print("Predictions - ",y_pred.flatten())
