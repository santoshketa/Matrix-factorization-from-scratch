# 
### Utility functions

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        rows: the number of rows the matrix 
        cols: the number of columns the matrix 
        
        returns list of lists which is a matrix
    """
    M = []
  
    while len(M) < rows:
        
        M.append([])
        while len(M[-1]) < cols:
            
            M[-1].append(0.0)
    return M 



def Intialiation_matrix(rows, cols):
    """
    This function creates different values in matrices A and B ,kind of random initialization
  
        rows: the number of rows the matrix 
        cols: the number of columns the matrix 
    """
    M = []
    count=0
    while len(M) < rows:
        
        M.append([])
        while len(M[-1]) < cols:
            count=count+1   
            M[-1].append(0.01*count) # given random value 0.01 which increase with every iteration giving /
    return M                                            # some kind of variability in matrices A and B during initialization
 

def matrix_multiply(A1, B1):
    """
    Returns the product of the matrix A1 * B1 
        : A1: The first matrix
        : B1: The second matrix
 
    """
    rowsA = len(A1)
    colsA = len(A1[0])
    rowsB = len(B1)
    colsB = len(B1[0])
    
    # Raising error if A1 columns not equal to B1rows
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A1 columns must equal number of B1 rows.')
 
    #  matrix multiplication resulting C
    C = zeros_matrix(rowsA, colsB) # initialize matrix C with zeros
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A1[i][ii] * B1[ii][j]
            C[i][j] = total
 
    return C


def dot(A1, B1):
    """
    Returns the DOTproduct between  A1 and B1
    
    A1: Takes input as lis
    B1: Takes input as lis
    """
    return sum(x*y for x,y in zip(A1,B1))

# Here I used row normalization i.e divide each value in row by the max value present in that row.
def normalization(M):
    """ Returns matrix with normalized values 
        M: Input matrix
    """
    global max_va
    max_va=[]  # storing malx values of each row
    m=[]     # intiliating list for storing normalized values
    for i in M :
        max_va.append(max(i))  #storing  max values for calculating inverse normalization
        l=[]
        for j in i:
            k= j/max(i)
            l.append(k)
        m.append(l) 
    return m


def Inverse_normalization(M):
    """ 
    Returns matrix with inverse-normalized values 
    M: Input matrix
    """
    R=[]
    for i in range(len(M)):
        l=[]
        for j in M[i]:
      # max_va is list of max values in each row
            l.append(j*max_va[i])
        R.append(l)
    return R

def GET_AB(X, K):
    
    """ Function outputs A and B along with  X=A.B
        Approach: Used MATRIX FACTORIZATION to solve the problem
    """
    iteration=10000 # number of iterations
    alpha=0.001 # learning rate
    beta=0.01 # regularization parameter
   
    
    X=normalization(X) # normalizing input matrix
    
    N = len(X) #  rows of X
    
    M = len(X[0])# columns of X
    
    P =Intialiation_matrix(N,K) # initializing matrix P=A
    Q = Intialiation_matrix(K,M) # initializing matrix Q=B
    
  #loop runs until given iteration
    for step in range(iteration):
        
        for i in range(len(X)):
            for j in range(len(X[i])):
                if X[i][j] > 0:
                   
                    eij = X[i][j] - dot(P[i],[row[j] for row in Q]) # CALCULATING ERROR 
                    
             # this loop generates gradient so until error is minimized
                    for k in range(K):
                        P[i][k] = P[i][k] + (alpha) * (2 * eij * Q[k][j] -( beta/(step+1)) * P[i][k]) #partial gradient wrt to p
                        Q[k][j] = Q[k][j] + (alpha) * (2 * eij * P[i][k] -( beta/(step+1)) * Q[k][j])  #partiAL gradient wrt to p
                        
        
        e = 0 
     
    #calculating error after updation
        for i in range(len(X)):
            for j in range(len(X[i])):
                if X[i][j] > 0:
                    e = e + pow(X[i][j] - dot(P[i],[row[j] for row in Q]), 2)
                    #e=float(str(round(e, 4)))
                   
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
                        
   # if error is less than 0.0001 terminate the loop                     
        if e < 0.0001: 
            break
            
    nr= matrix_multiply(P, Q) # calculating original matrix X 
    
    print('Final output matrix A:   ', P)
    print(100*'-')
    print('Final output matrix  B:   ',Q)
    print(100*'-')
    print('Final output matrix  inverse normalized X=A.B :   ',Inverse_normalization(nr))
   
    

K=int(input('enter integer value for K: '))


N = int(input("Enter the number of rows in X:")) 
M = int(input("Enter the number of columns in X:")) 
  
# Initialize matrix 
X = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(N):          # A for loop for row entries 
    a =[] 
    for j in range(M):      # A for loop for column entries 
         a.append(int(input())) 
    X.append(a) 
print(X)
    
GET_AB(X,K)