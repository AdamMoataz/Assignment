def calculate_lcm(a,b):
    """
     calculate the least common multiple
    """
    def gcd(x,y):
        while y:
            x,y=y , x%y
        return x
    
    return abs(a*b) //gcd(a,b)

calculate_lcm(6,9)
print(calculate_lcm)