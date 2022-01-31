import pandas as pd

def gradient_descent(x0, x1, x2, y):
    theta0 = theta1 = theta2 = 0
    iterations = 10000
    n = len(x0)
    learning_rate = 0.0000000005

    for z in range(iterations):
        theta0_gradient = theta1_gradient = theta2_gradient = cost = 0

        for i in range(n):
            theta0_gradient += x0[i] * ((theta0 * x0[i] + theta1 * x1[i] + theta2 * x2[i]) - y[i])
            theta1_gradient += x1[i] * ((theta0 * x0[i] + theta1 * x1[i] + theta2 * x2[i]) - y[i])
            theta2_gradient += x2[i] * ((theta0 * x0[i] + theta1 * x1[i] + theta2 * x2[i]) - y[i])

            """ 
            COST FUNCTION

            cost += ((y[i] - (theta0 * x0[i] + theta1 * x1[i] + theta2 * x2[i])) ** 2) / n
            
            """

        theta0 -= learning_rate * theta0_gradient / n
        theta1 -= learning_rate * theta1_gradient / n
        theta2 -= learning_rate * theta2_gradient / n
    
    return theta0, theta1, theta2
    
def main():
    df = pd.read_csv('car_dataset.csv')

    x2 = df['kms_driven'].to_list()
    x1 = df['year'].to_list()
    x0 = [1 for i in range(len(x1))]

    y = df['Price'].to_list()

    theta0, theta1, theta2 = gradient_descent(x0, x1, x2, y)

    year = int(input('Year: '))
    kms_driven = int(input('Kms driven: '))

    print(f'Price of {year} yr, {kms_driven} kms driven car: {theta0 + theta1 * year + theta2 * kms_driven}')

if __name__=="__main__":
    main()
