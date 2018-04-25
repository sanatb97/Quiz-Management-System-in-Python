import time
print("This is an mcq based quiz.")
print("The marking scheme is as follows:")
print("Correct answer: +4")
print("Wrong answer: -1")
print("No answer: -1")
print("Maximum marks=40")
print("Passing marks=20/40")
print("Passing percentage=50%")
print("Enter the correct option for each question when prompted")

name=input("Enter your name  ")
srn=input("Enter your SRN  ")
print("Good Luck, ",name,"!")






a=[]
c=0
count=[]
finalmarks=0
answers=['a','a','a','a','a','b','a','c','b','a']
print("****************************************")
print("Q1:What do the letter 't' and an island have in common?","a)Water","b)Sand","c)Trees","d)Birds",sep="\n")

a1=input() #for the answer
a.append(a1)
if a[0]==answers[0]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
################################################################3
print("Q2.What starts with a T, ends with a T and has T in it?","a)Teapot","b)Taxi","c)Trump","d)Tomato",sep="\n")
a1=input() #for the answer
a.append(a1)
count.append(1)
if a[1]==answers[1]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
#########################################################
print("Q3.What belongs to you,but others use it more than you do?","a)your name","b)your stationery","c)your water bottle","d)your phone",sep="\n")
a1=input() #for the answer
a.append(a1)
count.append(1)
if a[2]==answers[2]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
#############################################################
print("Q4.Who is the most famous skeleton detective?","a)Sherlock Bones","b)Nancy Drew","c)Pablo Escobar","d)None",sep="\n")
a1=input() #for the answer
a.append(a1)
count.append(1)
if a[3]==answers[3]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
 #############################################################
print("Q5.What has eyes but cannot see?","a)A potato","b)A bat","c)an owlf","d)a snake",sep="\n")
a1=input() #for the answer
a.append(a1)
count.append(1)
if a[4]==answers[4]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
##################################################################
print("Q6.What do you call a snakes wife?","a)Mem Saap","b)Aunty Saap","c)Mrs.Saap","d)Mummy Saap",sep="\n")
a6=input() #for the answer
a.append(a6)
count.append(1)
if a[5]==answers[5]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
######################################################################### 
print("Q7:Railroad crossing without any cars.How do you spell that without any R,S?","a)this","b)that","c)here","d)there",sep='\n')
a2=input()
a.append(a2)
count.append(1)
if a[6]==answers[6]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
########################################################################
print("Q8:What is another name for Santa Clauses' elves?","a)Elves","b)Clauses","c)Subordinate Clauses","d)None of the above",sep='\n')
a3=input()
a.append(a3)
count.append(1)
if a[7]==answers[7]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
########################################################################
print("Q9:When does a British potato change its nationality?","a)When BREXIT happens","b)When it becomes French Fries","c)When it gets exported","d)When it feels random",sep='\n')
a4=input()
a.append(a4)
count.append(1)
if a[8]==answers[8]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
##########################################################################
print("Q10.What is the opposite of dominos?","a)Domi doesn't know","b)Owlf","c)CR","d)Shagger",sep='\n')
a1=input()
a.append(a1)
count.append(1) 
if a[9]==answers[9]:
	finalmarks=finalmarks+4
else:
	finalmarks=finalmarks-1
print("This concludes the quiz. Thank you for taking part in it!")
print("Your report will be generated shortly")
time.sleep(5)
print("********************************************************")
print("Name:",name)
print("SRN:",srn)
print("Total Marks:",finalmarks,"/","40")
print("Percentage:",(finalmarks/40)*100,"%")
if(finalmarks<20):
 print("You have failed this test.We are sorry :(")
else:
 print("You have passed!Congrats!!:)")
print()
print("*******************************************************")






