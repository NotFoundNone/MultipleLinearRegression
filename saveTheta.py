import json

def saveThetaToFile(theta, filename):
    with open(filename, 'w') as f:
        json.dump({'theta_0': theta[0], 'theta_1': theta[1], 'theta_2': theta[2]}, f)
