import math
import numpy as np
import scipy
import scipy.linalg

# cluster input (below)

#def EuclideanDistance(point1, point2):
#	xDiff = point1[0] - point2[0]; <- cluster1, 2
#	yDiff = point1[1] - point2[1];
#	return math.sqrt(xDiff*xDiff + yDiff*yDiff);




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

def Rank(a):
        ans = np.linalg.matrix_rank(a);
        return ans;

def LUD(a):
        P, L, U = scipy.linalg.lu(a);
        ans = (P.tolist(), L.tolist(), U.tolist());
        return ans;

def SolveLin(matrix, vector):
        ans=np.linalg.solve(matrix,vector);
        return ans.tolist();

def SVD(a, only_specific):
        if only_specific == 1:
                full_matrices = False;
        else:
                full_matrices = True;
        u, sv, vh = np.linalg.svd(a, full_matrices);
        s = np.diag(sv);
        ans = (sv.tolist(), u.tolist(), s.tolist(), vh.tolist());
        return ans;
