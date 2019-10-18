def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


if __name__=='__main__':
    keyword_args(5)            #valid, out(5,1,X,None)
    keyword_args(a=5)          #valid, out(5,1,X,None)
    keyword_args(5,8)          #valid, out(5,8,X,None)
    keyword_args(5,2,c=4)      #valid, out(5,2,4,None)
    keyword_args(5,0,1)        #valid, out(5,0,1,None)
    keyword_args(5,2,d=8,c=4)  #valid, out(5,2,4,8)
    keyword_args(5,2,0,1,"")   #invalid
    keyword_args(c=7,1)        #invalid
    keyword_args(c=7,a=1)      #valid, out(1,1,7,None
    keyword_args(5,2,[],5)     #valid, out(1,7,[],5)
    keyword_args(1,7,e=6)      #invalid
    keyword_args(1,c=7)        #valid, out(1,1,7,None)
    keyword_args(5,2,b=4)      #invalid