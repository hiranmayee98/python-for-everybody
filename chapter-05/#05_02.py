"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""
total=0
n=0
max=0
min=0
while True:
   num=None
   try:
      num=input("Enter a number: ")
      print(num)
      if num=="Done" or num=="done":
         break
      num=int(num)
      if num is 0 or num>max:
         max=num
      if min is 0 or num<min:
         min=num
         
      total+=num
      n+=1
   except:
      print("Invalid input")
avg=total/n
print(total,n,max,min)
