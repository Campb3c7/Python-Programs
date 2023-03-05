#The code below was made by Colin Campbell
#The code placed in the fullcode string is convered to TI-BASIC formatting
#self made commands in the commands string is used to make it easier. 
#The TI-BASIC code is printed and is then copy and pasted into the TI-CONNECT software
#From there the program is put on the calculator to use
run = True
compile = []
def commandTest():
    if command[0].lower() == "stock":
        Stock()
    if command[0].lower() == 'print':
        Print()
    if command[0].lower() == 'input':
        Input()
    if command[0].lower() == 'if':
        If()
    if command[0].lower() == 'then':
        compile.append("Then")
    if command[0].lower() == 'end':
        compile.append("End")
    if command[0].lower() == 'while':
        While()
    if command[0].lower() == 'increment':
        compile.append(command[1].upper() + "+1→" + command[1].upper())
    if command[0].lower() == 'exact':
        Exact()

def Stock():
  compile.append(' '.join(command[2:len(command)]).upper() + "→" + command[1].upper())

def Print():
  if command[1] == 'string':
    words = ('"'+ ' '.join(command[2:len(command)]).upper()+ '"')
    compile.append("Disp "+ words )
  if command[1] == 'variable':
    compile.append(("Disp "+ command[2].upper()))

def Input():
  compile.append(("Input "+ command[1].upper()))

def If():
  for i in range(len(command)):
    if command[i] == '!=':
      command[i] = '≠'
    elif command[i] == ">=":
      command[i] == "≥"
    elif command[i] == "<=":
      command[i] == "≤"
  end = ''
  for i in range(len(command) - 1):
     end = end + command[i + 1].upper()
  compile.append("If "+ end)

def While():
  for i in range(len(command)):
    if command[i] == '!=':
      command[i] = '≠'
    elif command[i] == ">=":
      command[i] == "≥"
    elif command[i] == "<=":
      command[i] == "≤"
    end = ''
    for i in range(len(command) - 1):
      end = end + command[i + 1].upper()
  compile.append("While "+ end)
   
def Exact():
  end = ''
  for i in range(len(command) -1):
    end = end + command[i+1] + ' '
  compile.append(end)

  

""""
↓Commands↓
stock (Variable[A]) (Value[NUM)                               #Stores a value in a variable
print (string[string] or variable[variable]) (Message)        #Prints either a string or value of variable
input (Variable)                                              #Takes the input of user and stores it to variable
if (Variable) (compare) (Variable)                            #Creates if statement
while (Variable) (compare) (Variable)                         #Creates while statement
increment (Variable)                                          #Increments a variable by 1
exact (Everything)                                            #Everything that follows is printed exactly
"""


#The code below  takes input from user 1 or 2. 1 sorts L1 from large to small, 2 sorts L1 from small to large.
fullcode = """
print string type in or import data into list 1 on calculator
print string enter 1 for large to small or 2 for small to large
input x

if x = 1
then
stock b 1

while b = 1
stock b 0
stock i 1
exact dim(L₁)→S
while i < s
if L₁(i) < L₁(i+1)
then
stock p L₁(i)
stock L₁(i) L₁(i+1)
stock L₁(i+1) P
stock b 1
end
increment i
end
end

exact Else
stock b 1
while b = 1
stock b 0
stock i 1
exact dim(L₁)→S
while i < s
if L₁(i) > L₁(i+1)
then
stock p L₁(i)
stock L₁(i) L₁(i+1)
stock L₁(i+1) P
stock b 1
end
increment i
end
end
end
"""


linecode = fullcode.splitlines()
print(" ")
for i in range (1, len(linecode)):
    command = linecode[i]
    if command == "":
       command = "skip"
    command = command.split()
    commandTest()
for i in range(len(compile)):
    print(compile[i])
print(" ")