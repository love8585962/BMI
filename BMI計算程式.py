height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
height = float(height) #預防用戶輸入小數點
weight = float(weight) #預防用戶輸入小數點
height = height / 100 #換成公尺
BMI = weight / height**2
print("你的BMI為",BMI)

if BMI < 18.5 :
    print("體重過輕")
elif BMI >= 18.5 and BMI < 24 :
    print("正常範圍")
elif BMI >= 24 and BMI < 27 :
    print("過重")
elif BMI >= 27 and BMI < 30 :
    print("輕度肥胖")
elif BMI >= 30 and BMI < 35 :
    print("中度肥胖")
else :
    print("重度肥胖")