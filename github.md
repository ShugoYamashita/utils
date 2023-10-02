・commit メッセージ　書き方  
https://qiita.com/itosho/items/9565c6ad2ffc24c09364  

・一度gitにアップしてもらったものを、.gitignoreに追加した場合の対処  
https://qiita.com/fuwamaki/items/3ed021163e50beab7154  
```
git rm -r --cached [ファイル名]  //ファイル指定してキャッシュ削除
```

・既存のリモートリポジトリにアップロードする場合、git pullコマンドで最新のソースコードを取得する必要がある  
git pull origin main  

・githubでリポジトリを作成  

・ローカルリポジトリを作成  
mkdir ディレクトリ名  
cd ディレクトリ名  
git init // current directoryをgitリポジトリに変換  

git add ファイル名 // ファイルをindexに追加  
*.py, . (カレントディレクトリ以下全ての変更があるファイル)  
git commit -m “comment” // indexに追加されたファイルをローカルリポジトリにコミット  

// リモートリポジトリの情報を追加  
git remote add origin https://github.com/リモートリポジトリ  
// ローカルリポジトリの変更をリモートリポジトリに反映  
// 以降、git pushだけでリモートリポジトリにアップロードできる  
git push -u origin branch名  
git push origin main  
 
・branchの使い方  
git branch // 一覧表示 *は作業中のbranch  
git branch ブランチ名 // branchの作成  
git checkout ブランチ名 // branchに移動  
git checkout -b ブランチ名 // branchの作成と移動  

・branchのマージ  
git checkout main  
git merge branch名  
git push origin main  
  
・コマンド  
git fetch // 最新の更新内容を取得  
git merge // 現在のbranchにソースコードをマージ  
git pull // git fetchとgit mergeを行う  
git clone url  


・ローカルブランチ削除  
コミット漏れがないか確認  
git status  

2つのログを確認してpush漏れがないか確認  
git fetch //リモートリポジトリから最新の変更を取得、現在のブランチにマージしない。リモートリポジトリとの差分を取得して、ローカルリポジトリを最新の状態に更新する  
git log -1 //最新の1つのコミット情報  
git log -1 origin //リモートのリポジトリの最新の1つのコミット情報  

cd ..  //親ディレクトリに移動  
rm -rf リポジトリ名  //ディレクトリを消去  

・cloneしたリポジトリの履歴を初期化  
rm -rf .git // gitフォルダを削除  

・ssh接続  
https://prog-8.com/docs/git-env  
git init  
git brach -M main  
git remote add origin <sshのurl>  
git remote -v  

git add ファイル名  
git commit -m “comment”  
git push origin main  
