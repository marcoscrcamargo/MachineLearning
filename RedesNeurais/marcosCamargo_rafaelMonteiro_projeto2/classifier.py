from tensorflow import keras
from PIL import Image
import argparse
import numpy as np

def get_label(prediction_list):
	labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
	return labels[prediction_list.argmax()]

def main():
	# parsing image filename from CLI args
	parser = argparse.ArgumentParser(description="Image classifier trained with CIFAR-10 dataset. Receives image file paths and prints their classes on stdout.")
	parser.add_argument('image_filenames', action='store', help='Path to images to classify', nargs='+')
	args = parser.parse_args()

	# loading trained model
	clf = keras.models.load_model("model.h5")

	images = []
	# loading images and resizing them to correct size
	for image_filename in args.image_filenames:
		images.append( np.array(Image.open(image_filename).resize(size=(32,32))).astype(np.float32) / 255.0 )

	# classifying images
	predicted = clf.predict(np.array(images))

	# printing predicted classes
	for image_filename, result in zip(args.image_filenames, predicted):
		print(f'{image_filename} is a {get_label(result)} with {result.max() :.2%} probability.')


if __name__ == '__main__':
	main()