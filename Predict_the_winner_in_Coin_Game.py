def findWinner(M, N):
    if (M % 2 == 0 or N % 2 == 0):
        print("Player 1");
    else:
        print("Player 2");
m,n=map(int,input().split())  
findWinner(m,n)