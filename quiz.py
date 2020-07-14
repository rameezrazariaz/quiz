name=input("Enter your name: ")
score =0

print("\nWhich is the first fully supported 64bit system")
print("1. Windows Vista")
print("2. Mac")
print("3. Linux")
print("4. Windows XP")
choice=int(input("Your answer: "))
if choice==3:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is Linux")

print("\nComputer Hard Disk was first introduced in 1956 by")
print("1. Dell")
print("2. Apple")
print("3. Microsoft")
print("4. IBM")
choice=int(input("Your answer: "))
if choice==4:
    score+=1
    print("Correct")

    print("Incorrect. The correct answer is IBM")

print("\nWhich of the following is not a web browser")
print("1. MOSAIC")
print("2. WWW")
print("3. Facebook")
print("4. Netscape navigator")
choice=int(input("Your answer: "))
if choice==3:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is Facebook")

print("\nIn computer world, Trojan refer to")
print("1. Virus")
print("2. Malware")
print("3. Worm")
print("4. Spyware")
choice=int(input("Your answer: "))
if choice==2:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is Malware")

print("\nWhich one of the following is a programming language")
print("1. HTTP")
print("2. HTML")
print("3. HPML")
print("4. FTP")
choice=int(input("Your answer: "))
if choice==2:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is HTML")

print("\nWhich protocol is used to receive e-mail")
print("1. SMTP")
print("2. POP3")
print("3. HTML")
print("4. FTP")
choice=int(input("Your answer: "))
if choice==2:
    score+=1
    print("Corrrect")
else:
    print("Incorrect. The correct answer is POP3")

print("\nWhich protocol is used to send e-mail")
print("1. SMTP")
print("2. POP3")
print("3. HTTP")
print("4. SSH")
choice=int(input("Your answer: "))
if choice==1:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is SMTP")

print("\nWhich program converts Assembly Language to Machine Language")
print("1. Interpreter")
print("2. Compiler")
print("3. Comparator")
print("4. Assembler")
choice=int(input("Your answer: "))
if choice==4:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is Assembler")

print("\nIn which year '@' sign was first chosen for its use in e-mail address")
print("1. 1976")
print("2. 1980")
print("3. 1977")
print("4. 1972")
choice=int(input("Your answer: "))
if choice==4:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is 1972")

print("\nWho is the father of Indian Supercomputing")
print("1. Raghunath Mashelkar")
print("2. Vijay Bhatkar")
print("3. Jayant Narlikar")
print("4. Nandan Nilekani")
choice=int(input("Your answer: "))
if choice==2:
    score+=1
    print("Correct")
else:
    print("Incorrect. The correct answer is Vijay Bhatkar")

print("\nCongratulations {}".format(name))
print("You scored a total of {}/10".format(score))