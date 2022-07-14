def add_student(name, score1, score2):
    name=input()
    score1=input()
    score2=input()

student={'name':name,'socre1':score1,'score2':score2}
student_list.append(student)
def grade(score):
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    else :
        grade="D"
    return grade

def information(name, score):
    if add_student:
        return sum(x['score'] for x in add_student) / len(add_student)
        return ValueError("score cannot be empty")
    else:
        return add_student(name, score1, score2)

def delete_student():
    if name = input(' 삭제할 ​​학생의 이름을 입력하세요:')
    while 1:
        list=[]
    for student in student_list:
        if student['name']!=name:
            index=student_list.index(student)

        list.append(student_list[index])

        if len(student_list)==len(list):
            name=input('다시 입력하세요 존재하지 않는 이름입니다:')
        else:
            student_list.clear()

        for dict in list:
            student_list.append(dict)
        break
#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
             add_student(name, score1, score2)
        except ValueError:
            print('No student data!')
            
        except NameError :
            print('Not exist name!')

        try:
            score = int(input('성적을 입력하세요:'))

        except ZeroDivisionError :
            print('입력한 값은 정수가 아닙니다')
        else :
            input( add_student )

    elif choice == "2" :
        try:
            return sum(x[0] for x in student) / len(student)
            raise ValueError('Stduents cannot be empty')
        except ValueError:
            print ('Stduents cannot be empty')

        else :
            input(grade)
            print('Grading to all students.')

    elif choice == "3":
        def add_student():
            if len(student_list)==0:
                raise Exception ()
            except Exception:
                print('Stduents cannot be empty')

        else :
            input(information)

        elif choice == "4" :
            def delete_student():
            if len(student_list)==0:
                raise Exception ()
            except Exception:
                print('Stduents cannot be empty')

            else:
                name = input(' 삭제할 ​​학생의 이름을 입력하세요:')
                while 1:
                    list = []
                    for student in student_list:
                        if student[0] != name:
                            index = add_student_list.index(name,0,len(add_student_list))
                            list.append(add_student_list[index])
                            if len(student_list) == len(list):
                                name = input('Not exist name!')
                            else:
                                del add_student_list[index]
                                input('' 'student information is deleted.')

        elif choice == "5" :
            else:
                input('프로그램을 종료합니다.')

                break

        else :
            print('Wrong number. Choose again.')
            
                

            
            

    

        
        

            
        




    
    

        
