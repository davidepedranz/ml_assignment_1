import csv
import numpy as np
from sklearn.model_selection import KFold

# load the data from the file
def load_data():
    with open('leukemia.dat', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        dataset = list(reader)
    return dataset

# write the datasets
def export_datasets(index, (header, train, test)):

    # write the train set
    with open('data/leukemia_train_' + str(index) + '.dat', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for row in train:
            writer.writerow(row)

    # write the test set
    with open('data/leukemia_test_' + str(index) + '.dat', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for row in test:
            writer.writerow(row)

# execute k-fold on the given dataset
if __name__ == "__main__":
    
    # load the dataset
    dataset_with_header = load_data()

    # remove the header
    header = dataset_with_header[0]
    dataset = np.array(dataset_with_header[1:])
    
    # k-fold
    kf = KFold(n_splits=5, shuffle=True)
    for i, (train_index, test_index) in enumerate(kf.split(dataset)):
        train = dataset[train_index]
        test = dataset[test_index]
        export_datasets(i+1, (header, train, test))
