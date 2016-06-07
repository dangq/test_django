__author__ = 'dqan'
# closest pairs by divide and conquer
from optparse import OptionParser

def optparse():
    parser = OptionParser(usage="usage: %prog [options] filename")
    parser.add_option("-f", "--file",

                      dest="filename",
                      help="Please give me the coordinate of the points!")
    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.error("wrong number of arguments")

    return options, args

def coordinate(filename):
    x_y=dict()
    num_line=0
    for line in filename:
        num_line=num_line+1
        l = []
        for t in line.split():
            try:
                l.append(float(t))
            except ValueError:
                pass
        x_y.update({num_line:l})
    return x_y
    #print ('%f' % x_y[2][1]).rstrip('0').rstrip('.')
   # print "%f"%x_y[1][1]

# Calculate the Euclidean
def square(x): return x*x
def eu_dist(p,q): return square(p[0]-q[0])+square(p[1]-q[1])
def test_pair(p,q,best):
    d=eu_dist(p,q)
    if d<best[0]:
        best[0]=d
        best[1]=p,q

def merge(A,B):
	i = 0
	j = 0
	while i < len(A) or j < len(B):
		if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
			yield A[i]
			i += 1
		else:
			yield B[j]
			j += 1

def brute_force(L):
    best=eu_dist(L[1],L[2])
    for i in range(1,len(L)):
        for j in range(i+1,len(L)):

    return best

if __name__ == '__main__':
    options,args=optparse()
    x_y=dict()
    best=[]
    with open(options.filename) as f:
        x_y=coordinate(f)
        if len(x_y)<=3:
            brute_force(x_y)

        #print ('%f' % x_y[2][1]).rstrip('0').rstrip('.')
        #best.append(eu_dist(x_y[1],x_y[2]))
        #print best