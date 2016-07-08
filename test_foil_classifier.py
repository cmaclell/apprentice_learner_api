from ilp.foil_classifier import FoilClassifier

x = FoilClassifier(closed_world=False)

e1 = {}
e1['value'] = '7'

e2 = {}
e2['value'] = '7'

e3 = {}
e3['value'] = '8'

e4 = {}
e4['value'] = '8'

e5 = {}
e5['value'] = '7'

x.fit([e1, e2, e3, e4, e1, e1, e1, e5], 
      [1, 0, 1, 1, 1, 1, 1, 0])
print(x.predict([e4]))
data = [{'sepal width': 3.1, 'sepal length': 4.8, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 3.4, 'sepal length': 5.1, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 3.0, 'sepal length': 7.7, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 6.1}, {'sepal width': 3.0, 'sepal length': 4.9, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 2.8, 'sepal length': 5.6, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 4.9}, {'sepal width': 3.0, 'sepal length': 5.9, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.2}, {'sepal width': 3.1, 'sepal length': 6.7, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.4}, {'sepal width': 3.0, 'sepal length': 5.9, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.0, 'sepal length': 6.8, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 5.5}, {'sepal width': 2.3, 'sepal length': 4.5, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 3.0, 'sepal length': 5.6, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.1}, {'sepal width': 3.0, 'sepal length': 7.1, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 5.9}, {'sepal width': 2.9, 'sepal length': 6.6, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.6}, {'sepal width': 3.0, 'sepal length': 6.7, 'petal width': 1.7, 'class': 'Iris-versicolor', 'petal length': 5.0}, {'sepal width': 3.0, 'sepal length': 5.4, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 3.7, 'sepal length': 5.3, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.8, 'sepal length': 6.3, 'petal width': 1.5, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.4, 'sepal length': 4.8, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 2.8, 'sepal length': 6.8, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.8}, {'sepal width': 2.9, 'sepal length': 6.2, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.3}, {'sepal width': 2.7, 'sepal length': 5.2, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 3.9}, {'sepal width': 3.1, 'sepal length': 6.4, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 5.5}, {'sepal width': 3.4, 'sepal length': 6.3, 'petal width': 2.4, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 2.8, 'sepal length': 6.1, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.0}, {'sepal width': 3.0, 'sepal length': 6.7, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.2}, {'sepal width': 2.5, 'sepal length': 5.7, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 5.0}, {'sepal width': 3.1, 'sepal length': 6.9, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.2, 'sepal length': 4.6, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 2.6, 'sepal length': 6.1, 'petal width': 1.4, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 3.2, 'sepal length': 7.0, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.7}, {'sepal width': 3.7, 'sepal length': 5.4, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 3.0, 'sepal length': 6.5, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 5.5}, {'sepal width': 4.2, 'sepal length': 5.5, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.0, 'sepal length': 5.0, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 2.8, 'sepal length': 5.8, 'petal width': 2.4, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.0, 'sepal length': 6.0, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 4.8}, {'sepal width': 3.2, 'sepal length': 6.8, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.9}, {'sepal width': 3.1, 'sepal length': 6.7, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.7}, {'sepal width': 2.9, 'sepal length': 6.1, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.7}, {'sepal width': 2.5, 'sepal length': 6.3, 'petal width': 1.9, 'class': 'Iris-virginica', 'petal length': 5.0}, {'sepal width': 3.4, 'sepal length': 6.0, 'petal width': 1.6, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 3.8, 'sepal length': 5.7, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.7}, {'sepal width': 3.2, 'sepal length': 4.4, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 3.5, 'sepal length': 5.2, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 3.1, 'sepal length': 6.9, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 5.4}, {'sepal width': 3.0, 'sepal length': 7.6, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 6.6}, {'sepal width': 3.6, 'sepal length': 4.6, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.0}, {'sepal width': 3.0, 'sepal length': 6.1, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 4.9}, {'sepal width': 3.3, 'sepal length': 5.1, 'petal width': 0.5, 'class': 'Iris-setosa', 'petal length': 1.7}, {'sepal width': 3.3, 'sepal length': 6.7, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 5.7}, {'sepal width': 3.6, 'sepal length': 7.2, 'petal width': 2.5, 'class': 'Iris-virginica', 'petal length': 6.1}, {'sepal width': 3.2, 'sepal length': 6.4, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 2.7, 'sepal length': 6.0, 'petal width': 1.6, 'class': 'Iris-versicolor', 'petal length': 5.1}, {'sepal width': 2.8, 'sepal length': 7.4, 'petal width': 1.9, 'class': 'Iris-virginica', 'petal length': 6.1}, {'sepal width': 2.6, 'sepal length': 5.8, 'petal width': 1.2, 'class': 'Iris-versicolor', 'petal length': 4.0}, {'sepal width': 4.0, 'sepal length': 5.8, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.2}, {'sepal width': 2.8, 'sepal length': 6.2, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 4.8}, {'sepal width': 3.1, 'sepal length': 4.9, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 3.1, 'sepal length': 4.9, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 4.4, 'sepal length': 5.7, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 3.0, 'sepal length': 5.7, 'petal width': 1.2, 'class': 'Iris-versicolor', 'petal length': 4.2}, {'sepal width': 3.5, 'sepal length': 5.0, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 3.2, 'sepal length': 6.4, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.3}, {'sepal width': 2.9, 'sepal length': 4.4, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.4, 'sepal length': 5.2, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 2.7, 'sepal length': 5.6, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.2}, {'sepal width': 3.9, 'sepal length': 5.4, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.7}, {'sepal width': 3.3, 'sepal length': 6.3, 'petal width': 1.6, 'class': 'Iris-versicolor', 'petal length': 4.7}, {'sepal width': 3.5, 'sepal length': 5.5, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 2.5, 'sepal length': 5.1, 'petal width': 1.1, 'class': 'Iris-versicolor', 'petal length': 3.0}, {'sepal width': 3.2, 'sepal length': 7.2, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 6.0}, {'sepal width': 2.2, 'sepal length': 6.0, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 4.0}, {'sepal width': 3.0, 'sepal length': 6.5, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 5.2}, {'sepal width': 2.6, 'sepal length': 5.5, 'petal width': 1.2, 'class': 'Iris-versicolor', 'petal length': 4.4}, {'sepal width': 2.6, 'sepal length': 7.7, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 6.9}, {'sepal width': 3.2, 'sepal length': 5.9, 'petal width': 1.8, 'class': 'Iris-versicolor', 'petal length': 4.8}, {'sepal width': 3.3, 'sepal length': 5.0, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.8, 'sepal length': 5.1, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.9}, {'sepal width': 2.9, 'sepal length': 5.7, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.2}, {'sepal width': 3.8, 'sepal length': 5.1, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 3.4, 'sepal length': 4.8, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.9}, {'sepal width': 2.9, 'sepal length': 6.3, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 2.8, 'sepal length': 5.7, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.1}, {'sepal width': 3.2, 'sepal length': 4.7, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 2.6, 'sepal length': 5.7, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 3.5}, {'sepal width': 3.4, 'sepal length': 5.4, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.7}, {'sepal width': 3.0, 'sepal length': 4.3, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.1}, {'sepal width': 3.4, 'sepal length': 5.4, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.3, 'sepal length': 5.5, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.0}, {'sepal width': 3.0, 'sepal length': 6.6, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.4}, {'sepal width': 3.0, 'sepal length': 5.6, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 2.5, 'sepal length': 4.9, 'petal width': 1.7, 'class': 'Iris-virginica', 'petal length': 4.5}, {'sepal width': 2.8, 'sepal length': 6.5, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.6}, {'sepal width': 3.0, 'sepal length': 4.4, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 3.1, 'sepal length': 6.9, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.9}, {'sepal width': 2.7, 'sepal length': 5.8, 'petal width': 1.2, 'class': 'Iris-versicolor', 'petal length': 3.9}, {'sepal width': 3.2, 'sepal length': 4.7, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 3.3, 'sepal length': 6.3, 'petal width': 2.5, 'class': 'Iris-virginica', 'petal length': 6.0}, {'sepal width': 2.5, 'sepal length': 6.3, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.9}, {'sepal width': 2.8, 'sepal length': 6.1, 'petal width': 1.2, 'class': 'Iris-versicolor', 'petal length': 4.7}, {'sepal width': 4.1, 'sepal length': 5.2, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.5, 'sepal length': 6.7, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 5.8}, {'sepal width': 2.2, 'sepal length': 6.0, 'petal width': 1.5, 'class': 'Iris-virginica', 'petal length': 5.0}, {'sepal width': 3.0, 'sepal length': 7.2, 'petal width': 1.6, 'class': 'Iris-virginica', 'petal length': 5.8}, {'sepal width': 2.7, 'sepal length': 6.3, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 4.9}, {'sepal width': 3.5, 'sepal length': 5.1, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 2.0, 'sepal length': 5.0, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 3.5}, {'sepal width': 3.0, 'sepal length': 4.8, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 2.7, 'sepal length': 5.8, 'petal width': 1.9, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.9, 'sepal length': 5.4, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.3}, {'sepal width': 3.4, 'sepal length': 5.0, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.7, 'sepal length': 5.8, 'petal width': 1.9, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 3.3, 'sepal length': 6.7, 'petal width': 2.5, 'class': 'Iris-virginica', 'petal length': 5.7}, {'sepal width': 2.2, 'sepal length': 6.2, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 3.4, 'sepal length': 6.2, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.4}, {'sepal width': 3.4, 'sepal length': 4.6, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.1, 'sepal length': 4.6, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.5, 'sepal length': 5.5, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.0}, {'sepal width': 3.0, 'sepal length': 6.1, 'petal width': 1.4, 'class': 'Iris-versicolor', 'petal length': 4.6}, {'sepal width': 2.4, 'sepal length': 4.9, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 3.3}, {'sepal width': 3.0, 'sepal length': 6.5, 'petal width': 2.2, 'class': 'Iris-virginica', 'petal length': 5.8}, {'sepal width': 3.1, 'sepal length': 4.9, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.4, 'sepal length': 5.5, 'petal width': 1.1, 'class': 'Iris-versicolor', 'petal length': 3.8}, {'sepal width': 2.7, 'sepal length': 6.4, 'petal width': 1.9, 'class': 'Iris-virginica', 'petal length': 5.3}, {'sepal width': 2.8, 'sepal length': 5.7, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 2.9, 'sepal length': 7.3, 'petal width': 1.8, 'class': 'Iris-virginica', 'petal length': 6.3}, {'sepal width': 2.9, 'sepal length': 5.6, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 3.6}, {'sepal width': 2.4, 'sepal length': 5.5, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 3.7}, {'sepal width': 2.8, 'sepal length': 6.4, 'petal width': 2.1, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 2.7, 'sepal length': 5.8, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 4.1}, {'sepal width': 3.8, 'sepal length': 7.7, 'petal width': 2.2, 'class': 'Iris-virginica', 'petal length': 6.7}, {'sepal width': 3.8, 'sepal length': 5.1, 'petal width': 0.3, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.8, 'sepal length': 7.7, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 6.7}, {'sepal width': 3.2, 'sepal length': 6.9, 'petal width': 2.3, 'class': 'Iris-virginica', 'petal length': 5.7}, {'sepal width': 2.8, 'sepal length': 6.4, 'petal width': 2.2, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 3.4, 'sepal length': 5.0, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.6}, {'sepal width': 3.5, 'sepal length': 5.1, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.8, 'sepal length': 7.9, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 6.4}, {'sepal width': 2.5, 'sepal length': 5.6, 'petal width': 1.1, 'class': 'Iris-versicolor', 'petal length': 3.9}, {'sepal width': 3.0, 'sepal length': 4.8, 'petal width': 0.1, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.2, 'sepal length': 5.0, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.2}, {'sepal width': 3.1, 'sepal length': 6.7, 'petal width': 2.4, 'class': 'Iris-virginica', 'petal length': 5.6}, {'sepal width': 2.9, 'sepal length': 6.4, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.3}, {'sepal width': 2.3, 'sepal length': 6.3, 'petal width': 1.3, 'class': 'Iris-versicolor', 'petal length': 4.4}, {'sepal width': 3.6, 'sepal length': 5.0, 'petal width': 0.2, 'class': 'Iris-setosa', 'petal length': 1.4}, {'sepal width': 3.7, 'sepal length': 5.1, 'petal width': 0.4, 'class': 'Iris-setosa', 'petal length': 1.5}, {'sepal width': 2.9, 'sepal length': 6.0, 'petal width': 1.5, 'class': 'Iris-versicolor', 'petal length': 4.5}, {'sepal width': 3.2, 'sepal length': 6.5, 'petal width': 2.0, 'class': 'Iris-virginica', 'petal length': 5.1}, {'sepal width': 2.3, 'sepal length': 5.0, 'petal width': 1.0, 'class': 'Iris-versicolor', 'petal length': 3.3}, {'sepal width': 3.5, 'sepal length': 5.0, 'petal width': 0.6, 'class': 'Iris-setosa', 'petal length': 1.6}]

X = [{attr: x[attr] for attr in x if attr != 'class'} for x in data]
y = [1 if x['class'] == 'Iris-setosa' else 0 for x in data]

test_x = {'sepal width': 2.9, 'sepal length': 6.4, 'petal width': 0.5, 
           'petal length': 1.8}

x.fit(X, y)
print("trying to predict?")
print(x.predict([test_x]))
yh = x.predict(X)

error = []
for i,v in enumerate(yh):
    error.append(abs(v - y[i]))

print("Avg. Error on training set",)
print(sum(error) / len(error))
