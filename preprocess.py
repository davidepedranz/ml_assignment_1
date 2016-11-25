import csv
import random
import math

# load the data from the file
def load_data():
    with open('leukemia.dat', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        dataset = list(reader)
    return dataset

# split the dataset in training and test set
def split_data(dataset_with_header):

    # remove the header
    header = dataset_with_header[0]
    dataset = dataset_with_header[1:]

    # compute the size of the sets
    n = len(dataset)
    f = int(math.floor(n * 0.80))

    # shuffle and split
    random.shuffle(dataset)

    # extract a random training set
    train = dataset[1:f]
    test = dataset[f+1:n]
    return (header, train, test) 

def export_datasets(index, (header, train, test)):

    # write the train set
    with open('data/train_' + str(index) + '.dat', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(header)
        for row in train:
            writer.writerow(row)

    # write the test set
    with open('data/test_' + str(index) + '.dat', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerow(header)
        for row in test:
            writer.writerow(row)

def main():
    dataset = load_data()
    for i in range(1, 6):
        export_datasets(i, split_data(dataset))

# entry point
if __name__ == "__main__":
    main()

