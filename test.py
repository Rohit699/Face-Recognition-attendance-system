def fun():
    n = 10
    ans = 0
    while(n>1):
        ans += n&1
        n = n>>1
    print(ans)
    fun()
