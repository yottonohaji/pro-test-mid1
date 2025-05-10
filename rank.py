# ダミーデータ（No, 生徒名, 国語, 数学, 情報）
students = [
    [ 1, '山田太郎', 99, 98, 99],
    [ 2, '佐藤花子', 82, 70, 85],
    [ 3, '鈴木一郎', 68, 64, 71],
    [ 4, '高橋二郎', 90, 90, 95],
    [ 5, '田中三子', 55, 60, 65],
    [ 6, '渡辺四郎', 70, 77, 89],
    [ 7, '伊藤五月', 85, 72, 84],
    [ 8, '中村六子', 60, 69, 73],
    [ 9, '小林七郎', 88, 91, 94],
    [10, '加藤八子', 73, 68, 72]
]

# 合計点を計算し、新しいリストに格納
for student in students:
    total = student[2] + student[3] + student[4]
    student.append(total) # 合計点を追加
    student.append(1) # 順位を初期化

# 順位をつける
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][5] < students[j][5]:
            students[i][6] += 1
        elif students[i][5] > students[j][5]:
            students[j][6] += 1
              
# 表示
print("No 生 徒 名   国語 数学 情報 合計 順位")
for student in students:
    print(f"{student[0]:>2} {student[1]:<7} {student[2]:>3} {student[3]:>3} {student[4]:>4}  {student[5]:>4}{student[6]:>4}")