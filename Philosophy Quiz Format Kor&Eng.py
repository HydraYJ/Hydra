# Korean Version
def Quiz1K():
    Answer = input("1. 서양철학의 아버지로 여겨지는 사람은 누구입니까?")
    if Answer == "탈레스":
        print("정답입니다!")
        return("한국어 퀴즈가 모두 끝났습니다. 영어 퀴즈로 갑니다. 문제는 동일!")
    else:
        print("틀렸습니다. 다시 도전해보세요!")
        return(Quiz1K())

print(Quiz1K())


# English Version
def Quiz1E():
    Answer = input("1. Who's considered the father of Western Philosophy?")
    if Answer == "Thales" or Answer == "thales":
        return("Correct!")
    else:
        print("Wrong, Try Again!")
        return(Quiz1E())

print(Quiz1E())
