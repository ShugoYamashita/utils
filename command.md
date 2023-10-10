# コマンド集  
lsコマンド
```shell
# 隠しファイルも表示
ls -a
# 詳細表示
ls -l
# 指定したディレクトリの一覧表示
ls path/directory/
# カレントディレクトリのファイルとディレクトリの数を表示
ls -1 | wc -l
# ファイルだけをカウント
ls -l | grep ^- | wc -l
# ディレクトリだけをカウント
ls -l | grep ^d | wc -l
# 指定したディレクトリ直下のファイルとディレクトリの数を表示
ls -1 test_dir_01/ | wc -l
```
コピー、移動
```shell
# コピー
cp ${src_path} ${dest_path}
# -r: （コピー元がディレクトリのとき）ディレクトリの配下をすべてコピー
# -v: コピー結果を出力
# -f: 	コピー先に同名ファイルがあるとき上書きする

# 移動
mv ${src_path} ${dest_path}
```
削除
```
rm ${file_path}
# -r: ディレクトリを削除
```

## gpu関係
nvidia-smiコマンドを1秒ごとに更新する  
watchコマンドは指定したコマンドを定期的に実行し、結果をリアルタイムで表示  
Ctrl+Cを押して表示を終了  
```shell
watch -n 1 nvidia-smi
```
NVIDIA GPUの情報をリアルタイムでターミナルに表示
```shell
nvidia-smi -l 1
```
