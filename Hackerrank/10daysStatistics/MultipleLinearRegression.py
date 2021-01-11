# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn import linear_model

def compute_predictions(X_train, y_train, X_predict):
    lm = linear_model.LinearRegression()
    lm.fit(X_train, y_train)
    y_pred = lm.predict(X_predict)
    for ele in y_pred:
        print(ele)

if __name__ == "__main__":
    m, n = list(map(int, input().rstrip().split()))
    X = [None]*n
    y = [None]*n
    for i in range(n):
        line = list(map(float, input().rstrip().split()))
        X[i] = line[:m]
        y[i] = line[m]
        
    q = int(input().rstrip())
    X_predict = [None]*q
    for i in range(q):
        X_predict[i] = list(map(float, input().rstrip().split()))
    
    compute_predictions(X, y, X_predict)