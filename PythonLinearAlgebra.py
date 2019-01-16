import math
import numpy as np

def Add(a, b):
	return a+b;
	
def ConcatenateStrings(str1, str2):
	return str1 + str2;

def EuclideanDistance(point1, point2):
	xDiff = point1[0] - point2[0];
	yDiff = point1[1] - point2[1];
	return math.sqrt(xDiff*xDiff + yDiff*yDiff);

def AppendToList(array, newElement):
	array.append(newElement);

def Multiplication(a, b):
	a = np.array(a);
	b = np.array(b);
	ans = np.matmul(a, b);
	return ans.tolist();
