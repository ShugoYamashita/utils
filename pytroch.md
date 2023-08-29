・torchvisionのtransforms  
入力はPIL形式の画像を前提とする  

・dataloader.dataset：datasetを見る  
・dataloader.dataset.data：dataを見る  

・転置畳み込み deconvolution  
画像サイズ2倍  
kernel_size=4, stride=2, padding=1  
転置畳み込みの計算式  
https://nisshingeppo.com/ai/whats-deconvolution/  

・tensor.item()  
tensorオブジェクトからpythonのスカラー値として取り出す  

・nn.Moduleのself.apply(self._init_weights)   
全てのsubmoduleに関数を適用  
重みの初期化に使う  

・assert dim % num_heads == 0, f"dim {dim} should be divided by num_heads {num_heads}."   
assertは与えられた条件が真でない場合に例外を発生させる  
真の場合は何もなし  

・interpolatは後ろから2つの次元が指定したsizeに一致するよう補間  
tensor(B,C,H,W)  
torch.nn.functional.interpolate(tensor,size= (h, w))  

・torchinnfoでsummary表示  
https://yiskw713.hatenablog.com/entry/2021/06/01/070144  

・thop PyTorch-OpCounterでmacsを計算  
自作モジュールが反映できているか怪しい  

・saveのdirectoryはちゃんと場所を変える。同じところに保存すると、不具合の原因  
