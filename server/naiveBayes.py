
import json



example_data = {
    'yes': [
        [1,1,1,1],
        [1,1,1,0],
        [0,1,1,1],
        [1,0,0,1],
        [0,0,0,1]
    ],
    'no': [
        [0,0,0,0],
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [1,1,0,0]
    ]
}



class Dataset:
    def __init__(self, data: dict):
        self.data = data
        self.classes = list(data.keys())
        self.length = sum([len(i) for i in data.values()])

    def get_class(self, class_name):
        return self.data[class_name]
    
    def get_probability(self, value, class_name):
        class_data = self.get_class(class_name)
        print(class_data)
        return sum([1 for i in class_data if i == value]) / len(class_data)

    def get_class_probability(self, class_name):
        # print(self.length)
        return len(self.get_class(class_name)) / self.length
    
    def get_probability(self, value, class_name):
        class_data = self.get_class(class_name)
        return sum([1 for i in class_data if i == value]) / len(class_data)
    
    
    def add_data(self, class_name, values):
        self.data[class_name].append(values)
        self.classes = list(self.data.keys())
        self.length += 1



class NaiveBayes:
    def __init__(self, dataset: Dataset):
        self.dataset = dataset
        
    def get_class_probability(self, class_name):
        
        return self.dataset.get_class_probability(class_name)
    
    def get_probability(self, value, class_name):
        return self.dataset.get_probability(value, class_name)
    
    def get_probability_of_class(self, class_name, values):
        
        probability = self.get_class_probability(class_name)
        
        for value in values:
            probability *= self.get_probability(value, class_name)
            
        return probability
    
    def get_class(self, values):
        classes = self.dataset.classes
        
        return max(classes, key=lambda x: self.get_probability_of_class(x, values))
    
    def classify(self, values):
        return self.get_class(values)
    
dataset = Dataset(example_data)
nb = NaiveBayes(dataset)

print(nb.classify([0, 0, 0, 0]))