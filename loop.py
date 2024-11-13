'''(Count positive and negative numbers and compute the average of numbers)
 Write a program that reads an unspecified number of integers, determines
 how many positive and negative values have been read, and computes the total
 and average of the input values (not counting zeros). Your program ends with the
 input 0. Display the average as a floating-point number'''
count_positive=0
count_negative=0
count=0
total=0
while True:
    num=eval(input("Enter a number "))
    if num==0:
        break
    if num>0:
        count_positive+=1
    else:
        count_negative+=1
    total+=num
    count+=1
if count != 0:
    print(f"total is {total}")
    avg=total/count
    print(f'average is {avg}')
    print(f"positive numbers are:: {count_positive}")
    print(f"Negative numbers are:: {count_negative}")
    print(f"Total numbers are:: {count}")