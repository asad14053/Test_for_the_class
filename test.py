from cgi import print_environ_usage


print ("hello world")
f = open ("test.txt");
print(f)
lines  = f.readlines()
print(lines);


the_sum = 0
for line in lines:
    the_sum = the_sum + int(line)
    print(the_sum)  

print("---------------------")
# comment ---- this is a test
print(sum (int (x) for x in lines))
# 