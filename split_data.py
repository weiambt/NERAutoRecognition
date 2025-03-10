from sklearn.model_selection import train_test_split

def solve_file(input_path,output1_path,output2_path):
    with open(input_path, "r") as f:
        with open(output1_path, "w") as train_out:
            with open(output2_path, "w") as dev_out:
                lines = f.readlines()
                lines = ''.join(lines)
                data = lines.split('\n\n')
                for x in data:
                    print(x)
                train, test = train_test_split(data, test_size=0.2, random_state=38)
                print(f"训练集大小: {len(train)}, 测试集大小: {len(test)}")
                train_out.write("\n\n".join(train) + "\n\n")
                dev_out.write("\n\n".join(test) + "\n\n")


def split_demo():

    # 假设你有一个数据集 X 和对应的标签 y
    X = [x for x in range(100)]  # 你的数据
    y = [x for x in range(100)]  # 你的标签

    # 使用 train_test_split 来随机划分数据，test_size=0.1 表示测试集占 10%，训练集占 90%
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    X_train, X_test = train_test_split(X, test_size=0.1, random_state=42)

    print(f"训练集大小: {len(X_train)}, 测试集大小: {len(X_test)}")

    print(X_train)
    print(X_test)

if __name__ == '__main__':
    solve_file("emergency_2025_02_16/data.csv","emergency_2025_02_16/train.csv","emergency_2025_02_16/dev.csv")