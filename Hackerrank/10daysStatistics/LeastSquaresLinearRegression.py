# Enter your code here. Read input from STDIN. Print output to STDOUT

def predict_from_data(x_train, y_train, x_predict):
    #fit a lin reg to data, use that model to estimate prediction for new data
    n = len(x)
    sum_x = sum(x_train)
    sum_y = sum(y_train)
    sum_xy = 0
    for i in range(n):
        sum_xy+=x_train[i]*y_train[i]
    sum_x_2 = 0
    for i in range(n):
        sum_x_2+=x_train[i]*x_train[i]
    
    b = (n*sum_xy - sum_x*sum_y)/(n*sum_x_2 - sum_x**2)
    y_bar = sum_y/n
    x_bar = sum_x/n
    a = y_bar - b*x_bar
    
    return a + b*x_test

if __name__ == "__main__":
    x = [None]*5
    y = [None]*5
    
    for i in range(5):
        line = list(map(float,input().strip().split()))
        x[i], y[i] = line[0], line[1]
    
    x_test = 80
    print(round(predict_from_data(x, y, x_test), 3))