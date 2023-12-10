# コマンド集  
- パイプ
Linuxコマンドを使って標準出力された内容を次のコマンドへ渡す。  
コマンドの出力を連鎖的に利用できる。  
```shell
command1 | command2
command1 | command2 | command3 # 繰り返し利用できる
```

- cat
ファイルの内容を標準出力に表示する
```shell
cat sample.txt
```

- grep
```shell
grep [オプション] 文字列 ファイル名
# filename.txtの内容から"example"が含まれている行を表示
cat filename.txt | grep "example" # 
```

- lsコマンド
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

- コピー、移動
```shell
# コピー
cp ${src_path} ${dest_path}
# -r: （コピー元がディレクトリのとき）ディレクトリの配下をすべてコピー
# -v: コピー結果を出力
# -f: 	コピー先に同名ファイルがあるとき上書きする

# 移動
mv ${src_path} ${dest_path}
```

- 削除
```
rm ${file_path}
# -r: ディレクトリを削除
```

- タイムスタンプ
```shell
# @の後ろにタイムスタンプを指定  
date -d @1702112987
```
## gpu関係
- nvidia-smiコマンドを1秒ごとに更新する  
watchコマンドは指定したコマンドを定期的に実行し、結果をリアルタイムで表示  
Ctrl+Cを押して表示を終了  
```shell
watch -n 1 nvidia-smi
```

- NVIDIA GPUの情報をリアルタイムでターミナルに表示
```shell
nvidia-smi -l 1
```

- nvidia-smiをgpuメモリ使用量の行だけ表示
```shell
nvidia-smi | grep MiB
```


