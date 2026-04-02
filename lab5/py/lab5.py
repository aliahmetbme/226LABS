
sn_result = 0.0

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

def exp_x(x, n):
    
    term = lambda i: (x ** i) / factorial(i)
    
    total = 0.0
    for i in range(n + 1):
        total += term(i)
        
    return total

def Sn(n):
    
    global sn_result
    
    if n <= 0:
        return
        
    Sn(n - 1)
    
    sign = (-1) ** (n + 1)
    sn_result += sign * (1 / n)


if __name__ == "__main__":
    print("--- Soru 1: Faktoriyel Test ---")
    print(f"5! = {factorial(5)}")
    
    print("\n--- Soru 2: Ust (e^x) Test ---")
    print(f"e^2 (n=10 icin) = {exp_x(2, 10)}")
    
    print("\n--- Soru 3: S_n Test ---")
    sn_result = 0.0 
    Sn(4)

    print(f"S_4 serisinin recursive+global degisken hesabi: {sn_result}")
