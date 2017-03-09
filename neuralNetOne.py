import numpy as np

# Input vector of dimension 5
x = np.array([1, 0, 0, 1, 0])

# Threshold function to use for the activation function
def threshold(h):
    if (h >= 0):
        return 1
    else:
        return 0

# A class for neurons - assigns weights to values
class Neuron:
    # Constructor
    def __init__(self, dimen, activ):
        # Initialize the dimension of the input/weight vectors and the activation function
        self.dimension = dimen
        self.activate = activ
        # Create an initial random weight vector
        self.weights = np.random. randn(dimen + 1)

    # Calc the output given an input
    def output(self, x):
        # Add a bias by extending the input vector by adding a -1 on the left
        xext = np.zeros((self.dimension + 1,))
        xext[0] = -1
        xext[1:] = x
        return self.activate(np.dot(xext, self.weights))

    # Adjust the weights to make the output better math the target
    def learn(self, x, target, eta):
        # Calc the output values
        y = self.output(x)
        # Calc the multiplying factor eta * (y - t)
        factor = eta * (y - target)
        # Adjust the weights corresponding to the inputs
        self.weights[1:] -= factor * x
        # Adjust the bias
        self.weights[0] += factor

# Perceptron Network
class PercepNet:
    # Constructor
    def __init__(self, dimen, numNeurons, activ):
        # Create list of numNeurons and convert to array
        neuList = []
        for k in range(0, numNeurons):
            neuList += [Neuron(dimen, activ)]
        self.neurons = np.array(neuList)
        # Keep track of the dimension of the inputs and num of neurons for convenience
        self.dimension = dimen
        self.numNeurons = numNeurons

    # Calc the outputs from all of the neurons
    def output(self, x):
        # Create an array of zeros, then fill in the actual outputs
        out = np.zeros((self.numNeurons))
        for k in range(self.numNeurons):
            out[k] = self.neurons[k].output[x]
        # Return the array of outputs
        return out
    
    # Adjust the weights of all the neurons given array of targets
    def learn(self, x, targets, eta):
        # Loop through the neurons and train each one using its corresponding targets
        for k in range(self.numNeurons):
            self.neurons[k].learn(x, targets[k], eta)

    # Train the network for one iteration using a list of training pairs
    def trainOneIter(self, trainSet, eta):
        # Loop through the pairs in the training set and learn each pairs
        for (x, t) in trainSet:
            self.learn(x, t, eta)