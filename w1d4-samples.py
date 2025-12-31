# ==========================================
# Section 1: Python 辞書 (Dictionaries)
# ==========================================

# 練習問題1: 学生情報の管理 [cite: 69]
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
# 新しいキーと値の追加 [cite: 70]
student["favorite_subject"] = "Computer Science"
print(f"Student Dictionary: {student}")

# 練習問題2: 単語の出現回数をカウント [cite: 71]
sentence = "python is fun and python is powerful"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word Counts: {word_count}")


# ==========================================
# Section 2: オブジェクト指向プログラミング (OOP)
# ==========================================

# 1. 基本的なクラスの定義 (Car) [cite: 72, 73]
class Car:
    def __init__(self, make, model):
        self.make = make   # 属性
        self.model = model

my_car = Car("Toyota", "Corolla")
print(f"Car: {my_car.make} {my_car.model}")

# 2. メソッドを持つクラス (Person) [cite: 74]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# 3. 計算メソッドを持つクラス (Rectangle) [cite: 77]
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 4. 継承 (Inheritance) [cite: 80, 81]
class Animal:
    def make_sound(self):
        pass # 子クラスで上書きされる

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# 動作確認
dog = Dog()
cat = Cat()
print(f"Dog says: {dog.make_sound()}")
print(f"Cat says: {cat.make_sound()}")

# 5. 応用: 継承と属性の追加 (Vehicle & Car) [cite: 82, 83]
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricCar(Vehicle): # Vehicleを継承
    def __init__(self, make, model, num_doors):
        super().__init__(make, model) # 親クラスの初期化を呼び出す
        self.num_doors = num_doors

    def display_car_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}")

my_ev = ElectricCar("Tesla", "Model 3", 4)
my_ev.display_car_info()