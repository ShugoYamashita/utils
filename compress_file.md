# ファイルの圧縮・解凍  
## 基礎知識  
アーカイブ：複数のファイルやフォルダを1つにまとめる。  
オプションをまとめずにコマンドライン引数として指定するスタイル
```
tar [オプション] [アーカイブファイル名] [ファイルやディレクトリ]
```

tarアーカイブファイルを解凍・展開 (オプション指定しても、しなくても良い)
```
tar -xvf ＜tarアーカイブファイル名＞
tar xvf ＜tarアーカイブファイル名＞
```
optionの意味  
| option | 説明 |
| ---- | ---- |
| c | 新しいtarファイルを作る (create) |
| v | 圧縮・解凍状況を表示 |
| f | 圧縮ファイル名指定 (filename) |
| x | 解凍 (extract) |
| z | gz |
| j | bz2 |
| J | xz |


## tar.gz  
tarコマンドでまとめたアーカイブファイルをgzipコマンドで圧縮したファイルの拡張子  
圧縮
```
tar -zcvf xxxx.tar.gz directory
```
解凍
```
tar -zxvf xxxx.tar.gz
```

## tar.bz2  
tarコマンドでまとめたアーカイブファイルをBZIP2形式で圧縮したファイルの拡張子  
圧縮
```
tar -jcvf xxxx.tar.bz2 directory
```
解凍
```
tar -jxvf xxxx.tar.bz2
```

## tar.xz  
tarコマンドでまとめたアーカイブファイルをLZMA/LZMA2圧縮アルゴリズムで圧縮したファイルの拡張子  

圧縮
```
tar -Jcvf xxxx.tar.xz directory
```
解凍
```
tar -Jxvf xxxx.tar.xz
```

## tar  
tarコマンドでまとめたアーカイブファイルの拡張子
圧縮
```
tar -cvf xxxx.tar directory
```
解凍
```
tar -xvf xxxx.tar
```

## 参考  
https://qiita.com/supersaiakujin/items/c6b54e9add21d375161f  
https://qiita.com/yasushi-jp/items/bd126c96a5d19817f366  
