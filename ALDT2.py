# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    # Your code goes here!
    a = "I am super excited for this course!"
    c = ""
    for i in range(0,5):
        b = " "
        #Pass a temp value or empty value to store result.
        # We say here in each loop add a+b to c not c to c.
        c += (a + b)
    return c

print (show_excitement())
