import os

def write_file_names(directory_path, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            file.write(file_path + '\n')

def main():
    # ディレクトリパスと出力ファイルパスを指定
    directory_path = './raindrop/input'
    output_file_path = './output.txt'

    # ファイル名を出力
    write_file_names(directory_path, output_file_path)

if __name__ == '__main__':
    main()
