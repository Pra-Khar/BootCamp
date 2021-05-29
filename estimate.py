def wallis (count):
    pi=1
    for i in range (1,count+1):
        pi=pi*(4*(i**2))/(4*(i**2)-1)
    pi=2*pi
    return pi   

iteration = int(input ("enter value of iteration"))
estimated_py=wallis(iteration)   
print(f"{estimated_py}")

