f=lambda n:n and n*f(n-1) or 1
c=input()
while c:n,r=map(int,raw_input().split());print f(n)/f(r)/f(n-r);c-=1
