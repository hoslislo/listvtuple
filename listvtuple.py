# list vs tuple
my_list = []
for i in range(1, 10):
    my_list.append(i)

print my_list

my_var = my_list[4] + my_list[5]
print "my_var = ", my_var

'''
If you went for a walk, you could note your coordinates at any instant in an (x,y) tuple.
If you wanted to record your journey, you could append your location every few seconds to a list.
But you couldn't do it the other way around.
The values of list can be changed any time but the values of tuples can't be change.
'''
a = 25
b = "yeah"
c = "c"
d = 12.36

my_tuple = (a,b,c,d)
celebrity_tuple = ("John", "Wayne", 90210, "Actor", "Male", "Dead")

print celebrity_tuple[4]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_var =  11
# Male

somelist = [1, 2]
sometuple = (1001, 1002)
print somelist[0],sometuple[1]

# 1 1002