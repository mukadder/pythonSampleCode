try:
    v = 1/0
except ZeroDivisionError:
    print "Divide by zero"
try:
    v = "AA"
    int(v)
except ValueError:
    print "Value error"

try:
    raise Exception("Exception info")
except Exception as data:
    print str(data.args)