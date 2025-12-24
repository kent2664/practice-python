# ==========================================
# Course-6 (week1_Day2) Python Practice Codes
# ==========================================

# --- 1. Tuples (タプル) ---
print("--- 1. Tuples ---")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# アクセス (Accessing)
print(f"Second item: {thistuple[1]}") # banana
print(f"Last item: {thistuple[-1]}")   # mango
print(f"Range [2:5]: {thistuple[2:5]}") # ('cherry', 'orange', 'kiwi')

# 更新の回避策 (Workaround to update)
# タプルをリストに変換して変更し、再度タプルに戻す
y = list(thistuple)
y[1] = "kiwi_modified"
thistuple_updated = tuple(y)
print(f"Updated tuple: {thistuple_updated[1]}")

# アンパッキング (Unpacking)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(f"Unpacked: {green}, {yellow}, {red}")

# --- 2. Sets (セット) ---
print("\n--- 2. Sets ---")
thisset = {"apple", "banana", "cherry"}
print(f"Initial set: {thisset}")

# 追加 (Add)
thisset.add("orange")
print(f"After add: {thisset}")

# 集合の結合 (Join Sets)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(f"Union set: {set3}")

# 積集合 (Intersection - 重複のみ)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(f"Intersection: {z}")

# --- 3. If ... Else (条件分岐) ---
print("\n--- 3. If ... Else ---")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# 短縮形 (Short Hand If Else)
print("A") if a > b else print("B")

# --- 4. Functions (関数) ---
print("\n--- 4. Functions ---")

# 基本的な関数
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")

# 可変長引数 (*args)
def my_kids(*kids):
    print("The youngest child is " + kids[2])

my_kids("Emil", "Tobias", "Linus")

# 戻り値 (Return values)
def multiply_by_five(x):
    return 5 * x

print(f"Return value: {multiply_by_five(3)}")

# --- 5. Recursion (再帰) ---
print("\n--- 5. Recursion ---")
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Results:")
tri_recursion(6)

print("\n--- End of Day 2 Script ---")