num_range=int(input("Enter the range of numbers"))
odd_count=0
even_count=0

for i in range(1, num_range):
    print(i)
    if i%2==0:
        odd_count+=1
    else:
        even_count+=1

print("Odd Numbers Count ", odd_count)
print("Even Numbers Count ", even_count)
    
