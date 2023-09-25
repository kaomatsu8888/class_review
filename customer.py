#フルネーム 課題1
class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

# "Ken Tanaka" 出力
ken = Customer(first_name="Ken", family_name="Tanaka")
print(ken.full_name())

# "Tom Ford" 出力
tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())




#年齢 課題2
class Customer:
    def __init__(self, first_name, family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def get_age(self):
        return self.age
    
# 名前と年齢を一緒に表示する
    def display(self):
        return f"{self.full_name()} ({self.get_age()}歳)"
    

# 15歳
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.display())  

# 57歳
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.display())

# 急に出てきた73歳
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.display()) 

