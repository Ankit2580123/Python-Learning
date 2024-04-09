#create a function to calculate average of three numbers

# def average(num1=10,num2=10,num3=10):
#                     return (num1+num2+num3)/3

# ans=average(5,5,5)
# print(ans)

# write a function to check the input number is odd or even return string 

num=int(input("Enter a Number:"))
def odd_or_even(num):
                    if num%2==0:
                                        return "Even"
                    else:
                                        return "Odd"
                    
print(odd_or_even(num))


#write a function of a convert USD to indian rupees

# def convert(us_dollar):
#                     indian_ruppes=83*us_dollar
#                     return indian_ruppes
# ans=convert(5)
# print(ans)

#write a function of a factorail on n

# def factorial(n):
#                     fact=1
#                     for i in range(1,n+1):
#                                         fact*=i
#                     return fact

# ans=factorial(5)
# print(ans)
#Write a function to find its length

# city=["patna",'jamshedpur','indore','bokaro']
# countries=["india","australia",'ireland','pakistan','bangladesh','south africa']
# def length(list):
#                     print(len(list))
                    
                  
                  
# def single_line_print(list):
#                     for el in list:
#                                         print(el,end=" ")  
# length(city)
# length(countries)
# single_line_print(city)