#フルネーム 課題1
class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

#名前結合
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
    

# 田中健15歳
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.display())  

# トム・フォードコネチカット州在中 57歳
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.display())

# 急に出てきた73歳
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.display()) 


# 課題3 入場料
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
    def display_entrance(self):
         return f"{self.full_name()} ({self.get_age()}歳) 入園料: {self.entrance_fee()}円"
    def entrance_fee(self):
# こども料金
        if self.age < 20:
            return 1000
# おとな料金
        elif 20 <= self.age < 65:
            return 1500  
# シニア料金
        else:
            return 1200

# 名前と年齢を一緒に表示する
    def display(self):
        return f"{self.full_name()} ({self.get_age()}歳)"

# 1000円を表示
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.display_entrance())
# 1500円を表示
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.display_entrance())
# 1200円を表示
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.display_entrance())
