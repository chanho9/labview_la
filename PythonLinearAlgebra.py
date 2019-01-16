import math
import numpy as np

def Multiplication(a, b):
	a = np.array(a);
	b = np.array(b);
	ans = np.matmul(a, b);
	return ans.tolist();

def Transpose(a):
	a = np.array(a);
	ans = a.T;
	return ans.tolist();

def Determinant(a):
	a = np.array(a);
	ans = np.linalg.det(a);
	return ans;

def Inverse(a):
	a = np.array(a);
	ans = np.linalg.inv(a);
	return ans.tolist();

def EigenValue(a):
	a = np.array(a);
	answ, ansv = np.linalg.eig(a);
	answ = ",".join(str(x) for x in answ);
	ansv = ",".join(str(x) for x in ansv.reshape(1,-1)[0]);
	wLength = str(len(answ));
	wLLength = str(len(wLength));
	return wLLength+wLength+answ+ansv;

def Special(a, b):
	if a==0:
		ans = np.zeros(b);
	else:
		ans = np.identity(b);             
	return ans.tolist();


