from sklearn import tree
import numpy as np
import pandas as pd
import collections

# for drawing decision tree
import pydotplus

clf = tree.DecisionTreeClassifier()

columnNames = ['pelvic_incidence', 'pelvic_tilt', 'lumbar_lordosis_angle',
               'sacral_slope', 'pelvic_radius', 'degree_spondylolisthesis',
               'pelvic_slope', 'Direct_tilt', 'thoracic_slope',
               'cervical_tilt', 'sacrum_angle', 'scoliosis_slope']

colors = ('lightblue', 'yellow')


def main():
    global clf

    df = pd.read_csv("classifier/Dataset_spine.csv", sep=',', header=0)

    # Add column names to data frame
    data = df.rename(columns={'Col1': 'pelvic_incidence', 'Col2': 'pelvic_tilt', 'Col3': 'lumbar_lordosis_angle',
                              'Col4': 'sacral_slope', 'Col5': 'pelvic_radius', 'Col6': 'degree_spondylolisthesis',
                              'Col7': 'pelvic_slope', 'Col8': 'Direct_tilt', 'Col9': 'thoracic_slope',
                              'Col10': 'cervical_tilt', 'Col11': 'sacrum_angle', 'Col12': 'scoliosis_slope'})

    # Separate data frame to data and classes
    classAttr = data[['Class_att']]
    columnData = data.drop(['Class_att', 'Unnamed: 13'], axis=1)

    # Remove the 150 and 250 row of the dataframe in order to test with these rows later
    columnData = columnData.drop(columnData.index[150])
    columnData = columnData.drop(columnData.index[249])
    classAttr = classAttr.drop(classAttr.index[150])
    classAttr = classAttr.drop(classAttr.index[249])

    # Fix indexes in data frame
    classAttr.index = range(len(classAttr))
    columnData.index = range(len(columnData))

    # Convert data and classes to numpy array and list
    dataForPrediction = np.array(columnData).tolist()
    classesToPredict = np.array(classAttr['Class_att']).tolist()

    # Train data to the given classes
    clf = clf.fit(dataForPrediction, classesToPredict)

    results = {'dataForPrediction': dataForPrediction, 'classesToPredict': classesToPredict}

    return results


def predict(predict_data, data):
    # Make a prediction for the given predict data
    prediction = clf.predict([predict_data])

    # Display accuracy score
    accuracy = int(clf.score(data['dataForPrediction'], data['classesToPredict'])) * 100
    print('Accuracy:', accuracy, '%')

    # Draw decision tree
    imagePath = drawTree()

    # Save results from prediction and image path to a dictionary
    results = {'prediction': list(prediction)[0], 'imagePath': imagePath}

    return results


def drawTree():
    dot_data = tree.export_graphviz(clf, feature_names=columnNames, out_file=None, filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data)

    graphNodes = collections.defaultdict(list)

    for graphNode in graph.get_edge_list():
        source = graphNode.get_source()
        destination = graphNode.get_destination()
        graphNodes[source].append(int(destination))

    for graphNode in graphNodes:
        graphNodes[graphNode].sort()

        for i in range(2):
            filler = str(graphNodes[graphNode][i])
            res = graph.get_node(filler)[0]
            res.set_fillcolor(colors[i])

    # Save decision tree to png file
    graph.write_png('static/images/tree.png')

    return 'tree.png'
