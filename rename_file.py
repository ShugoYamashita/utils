# 指定したディレクトリ内のファイル名を変更する
import os

def main():
    # ファイルが存在するディレクトリパス
    directory_path = "./gt"

    # ディレクトリ内のファイルを取得
    files = os.listdir(directory_path)

    # ファイル名を変更
    for filename in files:
        if "clean" in filename:
            new_filename = filename.replace("clean", "rain")
            old_filepath = os.path.join(directory_path, filename)
            new_filepath = os.path.join(directory_path, new_filename)
            os.replace(old_filepath, new_filepath)
            # print(f"ファイル名を変更しました: {filename} -> {new_filename}")

if __name__ == '__main__':
    main()
