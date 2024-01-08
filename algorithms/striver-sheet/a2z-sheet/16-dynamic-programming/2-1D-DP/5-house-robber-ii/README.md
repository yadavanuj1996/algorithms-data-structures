# Intuition
This problem is same as house robber problem except that here the first house and last are connected (as it is
a circular street). 

If you think about it 

1, 2, 3, ..., n

n, n-2, n-4, ... , upto 2 can be taken (as 1 and n are neighbours)
n-1, n-3, ....upto 0 can be taken 

essentially this problem is broken down into 2 sub problems that we have already solved before

Please not we are omitting cases where house starts from n-2 or n-4, we do not need to move in circular order
because all these cases (n-2, n-4 etc) are already covered in n to 1 case.