from time import localtime, strftime
print "Netlog , \n"
t=strftime("%a, %d %b %Y %I:%M:%S", localtime())
s=raw_input("Enter logs: \n")
f = open('netlog.txt', 'a')
f.write("\n"+t+"\t"+s)
print  "\n"
