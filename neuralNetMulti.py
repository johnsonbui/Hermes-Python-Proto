import numpy as np

# Training set 
trainSetXOR = [(np.array([i,j], dtype=float), np.array([(i+j)%2], dtype=float)) for i in range(2) for j in range(2)]

# Neuron class for multi-layer perception
class Neuron:
    # The constructor
    def __init__(self, dimen, beta):
        # Init the dimension of the input and weight vectors
        self.dimension = dimen
        # Create an initial random weight vector
        self.weights = np.random.randn(dimen)
        # Keep track of the value of beta for the activation function
        self.beta = beta
    
    # Sigmoid activation function
    def sigmoid(self, h):
        y = 1 / (1 +np.exp(- self.beta * h))
        return y
    
    # Calc the output given an input vector 
    def output(self, x):
        return self.sigmoid(np.dot(x, self.weights))
    
    # Adjust the weights to reduce the error in the output
    def adjustWeights(self, x, error, eta):
        # Subtract the factor eta * error times the input vector from the weight vector
        self.weights -= eta * error * x

# Class for single layer in a multi-layer perceptron
class Layer:
    # constructor
    def __init__(self, inDimen, numNeus, beta):
        # Create an array of new neurons
        neus = [Neuron(inDimen, beta) for k in range(numNeus)]
        self.neurons = np.array(neus)
        # Keep track of the input dimension and the number of neurons
        self.inputDim = inDimen
        self.numNeurons = numNeus

    # Calc the output vector given an input vector
    def output(self, x):
        # Calc the output from each individual neuron put into a list
        # Convert the list to a vector and return the vector
        outs = [neu.output(x) for neu in self.neurons]
        outVec = np.array(outs)
        return outVec

    '''
    Adjust the weights in all of the neurons in this layer given the input vector and an array of the differences for all of the neurons as well as the training rate eta.
    '''

    def adjustWeights(self, x, diffs, eta):
        # Loop through the neurons in this layer and adjust the weights in each one.
        # At the same time, calc the differences to be used to train the preceding layer.
        # Start with zero vector for new differences.
        newDiffs = np.zeros((self.inputDim))
        for k in range(self.numNeurons):
            # Calc the output from the current neuron
            # Use the output and the difference to calculate the error for the current neuron
            currNeuron = self.neurons[k]
            out = currNeuron.output[x]
            error = out * (1 - out) * diffs[k]
            # Add the error, times the weight vector for the current neuron on the vector of the new diffs.
            newDiffs += error * currNeuron.weights
            # Use the error and the input vector to adjust the weights in the current neuron
            currNeuron.adjustWeights(x, error, eta)

        # Finished with loop.
        # The new differences have been calculated.
        # Return them
        return newDiffs

# Class for multi-layer perceptron networks
class MLPerceptron:
    # constructor
    # The input dimension is the dimension of the inputs to the first layer.
    # The param layerSizes is a list of the numbers of neurons in each layer.
    def __init__(self, inDimen, layerSizes, beta):
        # Create list of the layerSizes
        # Convert the list to an array.
        # Note the number of neurons in one layer is the dimension of its output vector, which beomces the dimension of the input vector for the next layer.
        inDimCurrent = inDimen
        layerList = []
        for layerSize in layerSizes:
            newLayer = Layer(inDimCurrent, layerSize, beta)
            layerList += [newLayer]
            # The layerSize for the current layer becomes the input dimension for the next layer.
            inDimCurrent = layerSize
        # List of layers created
        self.layers = np.array(layerList)
        # Keep track of the original input dimension and the list of the sizes of all the layers.
        self.inputDim = inDimen
        self.layerSize = layerSizes

    # Calc the output from the final layer, given the input to the first layer
    def output(self, x):
        # Calculate the output from each layer in turn, using the output from layer as the input to the next layer
        currentInVec = x
        for oneLayer in self.layers:
            out = oneLayer.output(currentInVec)
            currentInVec = out
        # The last output ( the output from the last layer ) is the output that we want
        return out

    # Adjust the weights in all the neurons in all the layers given the init input and an array of targets
    def multiTrain(self, x, targets, eta):
        # Start by creating a list of the layers together with their inputs
        currentInVec = x
        layerInputList = []
        for oneLayer in self.layers:
            layerInputList += [(oneLayer, currentInVec)]
            out = oneLayer.output(currentInVec)
            currentInVec = out
        '''
        List of layers and inputs created.
        Work backwards using differences and inputs to train each layer.
        Init differences are the output from the last layer minus the targets. 
        Note that the value of the variable 'out' at the end of the 'for' loop is the output from the last layer. 
        '''
        diffs = out - targets
        # Loop through the layer/input pairs in the list in reverse order
        for (layer, inputVec) in layerInputList[::-1]:
            # Adjust the weights in the current layer. 
            # This also returns the new set of differences for the next layer back.
            newDiffs = layer.adjustWeights(inputVec, diffs, eta)
            # Set the differences for the next layer back to be the new differences just returned
            diffs = newDiffs

    # Train the network for one iteration using a list of training pairs, [(input, target)]
    def trainOneIter(self, trainSet, eta):
        # Loop throug hthe pairs in the training set and learn each pair.
        for (x, t) in trainSet:
            self.multiTrain(x, t, eta)

    # Show the input, corresponding output, and target for each pair in a training set.

    def showTSOutputs(self, trainSet):
        # Loop through the pairs and print info from each one.
        for (x, t) in trainSet:
            y = self.output(x)
            line = "Input: {0}, Output: {1}, Target: {2}".format(x, y, t)
            print(line)

    # Show how many outputs match the targets within a given tolerance
    def showTSPerform(self, trainSet, tolerance):
        # Count the number of inputs for whic hthe corresponding out is within the given tolerance of the target
        count = 0 
        for (x, t) in trainSet:
            y = self.output(x)
            if (np.linalg.norm(y - t) <= tolerance):
                count += 1
            # Count finished results.
            # Divide by the size of the training set and return
            return count / len(trainSet)


    

