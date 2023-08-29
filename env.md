. ~/.venv/std/bin/activate  
・GPU0を使う例  
tmux new -s gpu0  
export CUDA_VISIBLE_DEVICES=0    

https://github.com/ikeharalab/help/blob/main/python/venv.md  
・仮想環境を作る。ディレクトリの形で作成させ、必要なファイルが自動生成される。  
python -m venv ~/.venv/__name__  
・仮想環境に入る。仮想環境のディレクトリ内に作成された activate スクリプトを実行  
. ~/.venv/__name__/bin/activate  
・仮想環境内でpip installコマンドを実行すると、仮想環境内に閉じてパッケージがインストールされる。  
・仮想環境から抜ける  
deactivate  
・仮想環境を削除する  
https://qiita.com/nosniklim/items/1d4c480e3accd3eb8c0f  
・仮想環境を初期化  
python -m venv --clear [仮想環境名]  
・仮想環境を削除  
rm -rf [仮想環境名]  
・デフォルトの仮想環境  
https://tekunabe.hatenablog.jp/entry/2018/12/28/vscode_venv_default_rolad  

nvidia-smi  
ログインしているサーバのGPUに関するリアルタイムな情報がわかる。GPUを使う前に打って確認する。  
cudaのversionは右上に書いてある。  

tmux  
チートシート：https://qiita.com/nmrmsys/items/03f97f5eabec18a3a18b  
SSHが切れてもプログラムが動き続けるようにしてくれる。tmuxのセッションを使わないとSSHの接続が切れたときにプログラムが中断される。  
・新たなセッションを作る  
tmux new -s <セッション名>  
・セッションから抜ける  
Ctrl+Bを押して指を離した後にDを打つ  
・セッションを開き直す  
tmux a -t <セッション名>  
・セッションを削除  
tmux kill-session -t <セッション名>  
・使うGPUの制限。複数枚を同時に使うのは専用のコードを書く必要があるため基本的に1枚に制限する。tmuxを用いて使いたいGPUに合わせた名前のセッションを作ると管理しやすい。  
d<使いたいGPUの番号>  

# セッションの一覧表示    
tmux ls  
# tmuxでコピー  
ドラッグ→スペース→エンターを押すまでに選択した範囲がコピー  
ctr-B →]でペースト、  
# 設定ファイル.tmux.confを編集して反映  
tmux source ~/.tmux.conf  
# tmuxのconsoleのスクロール  
ctr-B -> [      qで終了  

