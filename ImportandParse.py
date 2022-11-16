import sys 
##Argument Parsing#############################################
n = len(sys.argv)
if(n < 2):
    print("Incorrect format: your_program <input_file_name> <EDF or RM> [EE]")
    sys.exit()
elif(n == 3):
    file = sys.argv[1]
    Alg = sys.argv[2]
    EE = False
elif(n == 4):
    file = sys.argv[1]
    Alg = sys.argv[2]
    EE = True
else:
    print("Incorrect format: your_program <input_file_name> <EDF or RM> [EE]")
    sys.exit()

if (Alg != "EDF" and Alg != "RM"):
    print("Incorrect format: your_program <input_file_name> <EDF or RM> [EE]")
    sys.exit()

#Split the lines into int lists################################
with open(file, "r") as f:
    data = f.read().splitlines()
overview = [int(i) for i in data[0].split()]
task1 = data[1].split()
task1.pop(0)
task2 = data[2].split()
task2.pop(0)
task3 = data[3].split()
task3.pop(0)
task4 = data[4].split()
task4.pop(0)
task5 = data[5].split()
task5.pop(0)
task1 = [int(i) for i in task1]
task2 = [int(i) for i in task2]
task3 = [int(i) for i in task3]
task4 = [int(i) for i in task4]
task5 = [int(i) for i in task5]
#Integer Parsing#################################################
numTasks = int(overview[0])
sysTime = int(overview[1])
aCPU1188 = int(overview[2])
aCPU918 = int(overview[3])
aCPU648 = int(overview[4])
aCPU384 = int(overview[5])
iCPUlow = int(overview[6])

class W1:
    deadline = task1[0]
    WCET1188 = task1[1]
    WCET918 = task1[2]
    WCET648 = task1[3]
    WCET384 = task1[4]
class W2:
    deadline = task2[0]
    WCET1188 = task2[1]
    WCET918 = task2[2]
    WCET648 = task2[3]
    WCET384 = task2[4]
class W3:
    deadline = task3[0]
    WCET1188 = task3[1]
    WCET918 = task3[2]
    WCET648 = task3[3]
    WCET384 = task3[4]
class W4:
    deadline = task4[0]
    WCET1188 = task4[1]
    WCET918 = task4[2]
    WCET648 = task4[3]
    WCET384 = task4[4]
class W5:
    deadline = task5[0]
    WCET1188 = task5[1]
    WCET918 = task5[2]
    WCET648 = task5[3]
    WCET384 = task5[4]

print(Alg)
print("Energy Eficient:", EE)
print(W5.deadline)