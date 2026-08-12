inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [0, 0, 0, 1]

w1 = 0.5
w2 = 0.5
bias = -0.7

def activation(net):
    if net >= 0:
        return 1
    else:
        return 0

print("Perceptron AND Gate\n")

for i in range(len(inputs)):
    x1 = inputs[i][0]
    x2 = inputs[i][1]

    net = (x1 * w1) + (x2 * w2) + bias
    output = activation(net)

    print("input:", x1, x2)
    print("weighted sum:", net)
    print("predicted output =", output)
    print("expected output =", targets[i])
    print()