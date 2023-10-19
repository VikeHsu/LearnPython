with open('/home/vikehsu/LearnPython/Lesson4/File/Config.txt','a+') as file1:
    file1.seek(0)
    for i in range(4):
        line = file1.readline()
        print(i)
        print(line)
    #file1.write("pi\n")
    file1.seek(0)
    contents_new = file1.read()
    print(contents_new)

# do other thing
a = 10
try:
    b = int(input())
    print(a + b)
except ValueError as ve:
    #print(ve)
    print("please input a integer value.")
