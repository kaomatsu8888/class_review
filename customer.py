class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

#フルネーム 課題1
    def full_name(self):
        return f"{self.first_name} {self.family_name}"

# "Ken Tanaka" 出力
ken = Customer(first_name="Ken", family_name="Tanaka")
print(ken.full_name())

# "Tom Ford" 出力
tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())  

#年齢 課題2
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す

