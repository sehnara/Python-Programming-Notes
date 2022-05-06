# 소수 판별(에라토스테네스의 체) > True or False
def is_prime(n) :
    prime = [False,False]+ [True] * n;
    for i in range(2, int((n+1)**0.5)+1):
        if prime[i] :
            for j in range(2*i, n+1, i):
                prime[j] = False;
    return prime;