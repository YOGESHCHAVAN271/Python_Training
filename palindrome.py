initial_value=0
next_value=1

print(initial_value)
print(next_value)
value_till=50
boolean=True
while(boolean):
    final_value=initial_value+next_value
    if(final_value<value_till):
        
         print(final_value)
         initial_value=next_value
         next_value=final_value
    else:
        boolean=False
        
    
