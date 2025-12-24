# ==========================================
# Course-6 (week1_Day1) Python Basic Codes
# ==========================================

import random

# 1. Hello World と基本の出力
print("--- 1. Hello World ---")
print("Hello, World!")
print("Cheers, Mate!")

# 2. 変数 (Variables)
print("\n--- 2. Variables & Types ---")
x = 5
y = "John"
print(f"x: {x}, y: {y}")

# 型変換 (Casting)
x_str = str(3)    # '3'
y_int = int(3)    # 3
z_float = float(3) # 3.0
print(f"Types: {type(x_str)}, {type(y_int)}, {type(z_float)}")

# 複数代入とアンパッキング
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(f"Unpacked: {a}, {b}, {c}")

# 3. 数値と乱数 (Numbers & Random)
print("\n--- 3. Numbers & Random ---")
print(f"Random number (1-9): {random.randrange(1, 10)}")

# 4. 文字列操作 (String Methods)
print("\n--- 4. String Methods ---")
text = " Hello, World! "
print(f"Original: '{text}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Strip: '{text.strip()}'") # 前後の空白削除
print(f"Replace: {text.replace('H', 'J')}")
print(f"Split: {text.split(',')}")

# スライシング
b = "Hello, World!"
print(f"Slice [2:5]: {b[2:5]}") # llo

# f-strings
age = 36
print(f"My name is John, I am {age}")

# 5. リスト (Lists)
print("\n--- 5. List Operations ---")
thislist = ["apple", "banana", "cherry"]
print(f"Initial list: {thislist}")
print(f"Length: {len(thislist)}")

# 追加と変更
thislist[1] = "blackcurrant"
thislist.append("orange")
thislist.insert(1, "mango")
print(f"Modified list: {thislist}")

# 削除
thislist.remove("apple")
popped_item = thislist.pop() # 最後を削除
print(f"After removal: {thislist} (Popped: {popped_item})")

# リスト内包表記 (List Comprehension)
# 'a'が含まれるフルーツだけを抽出
newlist = [x for x in thislist if "a" in x]
print(f"Filtered list (contains 'a'): {newlist}")

# ソート
thislist.sort()
print(f"Sorted list: {thislist}")

# 6. ユーザー入力 (User Input)
print("\n--- 6. User Input ---")
# 注意: 実行時にターミナルで入力を求められます
name = input("Enter your name: ")
print(f"Hello, {name}!")

print("\n--- End of Script ---")