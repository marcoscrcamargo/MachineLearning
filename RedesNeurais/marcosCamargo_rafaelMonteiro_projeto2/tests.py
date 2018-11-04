import os

if __name__ == '__main__':
	os.system(f'classifier.py {" ".join(["test_data/" + filename for filename in os.listdir("test_data")])}')