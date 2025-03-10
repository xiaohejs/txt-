import os

def split_file(file_path, chunk_size, output_dir):
    try:
        # 不知道该咋命名
        chunk_size = int(chunk_size) * 1024 * 1024  # MB
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        with open(file_path, 'rb') as file:
            part = 1
            while True:
                chunk = file.read(chunk_size)
                if not chunk:  
                    break

                # 检查读取文件是否为空
                if chunk:
                    output_file = os.path.join(output_dir, f"{base_name}_part{part}.txt")
                    with open(output_file, 'wb') as out_file:
                        out_file.write(chunk)
                    part += 1

        print(f"文件已成功分割为{part - 1}个部分！")
    except Exception as e:
        print(f"发生错误：{str(e)}")


def main():
    while True:
        print("\n欢迎使用小说分割器！\n本程序基于DlmOS驱动\n作者:Dlmos火烧云。使用Github开源文件爆改而来\n请输入下方列表选项相对序号启动程序：")
        print("1. 启动程序")
        print("2. 赞助我们")
        print("3. 常见问题")
        print("4. 退出程序")

        choice = input("请输入选项：")

        if choice == '1':
            try:
                # 询问路径
                file_path = input("请输入要分割的txt文件的路径：")
                if not os.path.isfile(file_path):
                    print("文件路径不存在或不是有效的文件。")
                    continue

                size = input("请输入要分割的文件大小（以MB为单位）：")
                output_dir = input("请输入保存分割后文件的目录路径：")
                if not os.path.exists(output_dir):
                    print("目录路径不存在")
                    continue

                # 绝对路径
                if not os.path.isabs(output_dir):
                    output_dir = os.path.abspath(output_dir)

                split_file(file_path, size, output_dir)
            except Exception as e:
                print(f"发生错误：{str(e)}")
        elif choice == '2':
            print("感谢您的支持！不过你还真打算赞助啊...\n要不试试我们的DL报刊论坛：\nhttps://dlbkltos.s7123.xyz")
        elif choice == '3':
            print("为什么我输入路径后回车报错？\n【因为本程序要求输入路径为绝对路径，如：/storage/emulated/0/Download/520.txt。输出路径要求定位到文件夹，如：/storage/emulated/0/Download/】")
        elif choice == '4':
            print("已退出。")
            break
        else:
            print("找乐子是吗？重新输！")

if __name__ == "__main__":
    main()