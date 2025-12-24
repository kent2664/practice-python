# ==========================================
# Course-6 (week1_Day3) Python File Handling
# ==========================================
import os
import shutil
import tempfile
import filecmp

# --- 1. ファイルの読み取り (Read) ---
# ※あらかじめ "demofile.txt" が存在することを前提としています
try:
    # 基本的なオープン
    f = open("demofile.txt", "r")
    
    # 全体読み取り
    # print(f.read())
    
    # 指定した文字数だけ読み取り
    print("--- First 5 characters ---")
    print(f.read(5))
    
    # 1行ずつ読み取り
    f.seek(0) # ファイルポインタを先頭に戻す
    print("--- First line ---")
    print(f.readline())
    
    # ループによる読み取り
    f.seek(0)
    print("--- Loop through lines ---")
    for x in f:
        print(x.strip())
    
    f.close()
except FileNotFoundError:
    print("demofile.txt not found. Please create it first.")

# --- 2. ファイルへの書き込み (Write/Append) ---
# 追記モード (Append)
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# 上書きモード (Write)
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# --- 3. ファイルとディレクトリの削除 ---
# ファイルの存在確認と削除
if os.path.exists("demofile.txt"):
    # os.remove("demofile.txt") # 実行に注意
    print("File exists")
else:
    print("The file does not exist")

# ディレクトリの作成と削除
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
# os.rmdir("myfolder")

# --- 4. OSとディレクトリ操作 (os module) ---
print("\n--- Directory Operations ---")
print(f"Current Directory: {os.getcwd()}")
print(f"List files: {os.listdir('.')}")

# パスの結合
path = os.path.join("user", "bin", "python")
print(f"Joined path: {path}")

# --- 5. 高度な操作 (shutil, filecmp, tempfile) ---
# ファイルのコピー (shutil)
# shutil.copy('source.txt', 'destination.txt')

# ファイルの比較 (filecmp)
# same = filecmp.cmp('file1.txt', 'file2.txt')
# print(f"Are files identical?: {same}")

# 一時ファイルの作成 (tempfile)
with tempfile.TemporaryFile(mode='w+t') as tf:
    tf.write('Hello World!')
    tf.seek(0)
    print(f"Temp file content: {tf.read()}")
# (withブロックを抜けると自動的に削除されます)

# --- 6. Withステートメント (推奨される書き方) ---
# close() を自動で行ってくれるため安全です
with open("test.txt", "w") as f:
    f.write("This is a safe way to handle files.")