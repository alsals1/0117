a = 1
b = 2

def enclosed():
    a = 10
    c = 3
    
    def local(c):
        print(a, b, c)
        
        # a,b 가 없으므로 LEGB 순서대로 
        # E 에서 a = 10 G = 2 *c= 500*
        
        local(500)
        print(a, b, c)    # 10, 2, 3

enclosed()