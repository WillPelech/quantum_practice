import numpy as np
import os
from PIL import Image
from matplotlib import pyplot as plt

#path for demo
image_path = '/Users/willpelech/Desktop/Quantum_Demo/random.png'
save_path = '/Users/willpelech/Desktop/Quantum_Demo/compressed.png'


#Note that this can only use black and white bc four matrixes would be required for color SVD and I dont have time
def setup(path):
    print("Loading image...")
    image = Image.open(path)
    grey_img = image.convert('L')
    imatrix = np.array(grey_img, dtype=float)
    return imatrix


try:

    print("Loading image...")
    image = Image.open(image_path)
    grey_img = image.convert('L')
    imatrix = np.array(grey_img, dtype=float)


###PART TO SHOW IN DEMO
    #Perform SVD
    num_sing_values = 2000
    print("Performing SVD...")
    U, s, Vt = np.linalg.svd(imatrix, full_matrices=False)#u sigma vt
    S = np.diag(s[:num_sing_values])
    U = U[:, :num_sing_values]
    Vt = Vt[:num_sing_values, :]
    #Image reconstruction and saving
    print("Reconstructing and saving image...")
    plt.imshow(U @ S @ Vt, cmap='gray')
    plt.savefig(save_path)
    print("Image saved at:", save_path)
    plt.show()






#_____Troubleshooting code
except Exception as e:
    print("Failed to process the image:", e)
import os


save_path = '/Users/willpelech/Desktop/Quantum_Demo/test_file.txt'


os.makedirs(os.path.dirname(save_path), exist_ok=True)

try:
    # Write a test file
    with open(save_path, 'w') as f:
        f.write('This is a test file.')
    print(f"File successfully saved at {save_path}")
except Exception as e:
    print(f"Failed to save file: {e}")

def main():
    print()

    # old function which performs SVD
    # def SVD(matrix, sing_values):
    #     print("Performing SVD...")
    #     U, s, Vt = np.linalg.svd(matrix, full_matrices=False)
    #     S = np.diag(s[:sing_values])
    #     U = U[:, :sing_values]
    #     Vt = Vt[:sing_values, :]
    #     return U @ S @ Vt

    #
    # #checks that the path exists
    # if not os.path.exists(os.path.dirname(save_path)):
    #     os.makedirs(os.path.dirname(save_path))
    #     print("Created directory:", os.path.dirname(save_path))