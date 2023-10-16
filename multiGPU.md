# 複数のgpuを使う方法  
DistributedDataParallelが推奨。DataParallelよりも速い。  
## DistributedDataParallel  

## Dataparallel  

参考  
https://torchhogehoge.hatenablog.com/entry/pytorch_DDP#DistributedDataParallel  

https://tmyoda.hatenablog.com/entry/20210314/1615712115  

https://aru47.hatenablog.com/entry/2020/11/06/225052   

https://qiita.com/fam_taro/items/df6061b589c3ccf86089  

・並列化の解説  
https://zenn.dev/turing_motors/articles/0e6e2baf72ebbc  

・PyTorch Lightningで簡単に実装できる？  
https://tech.jxpress.net/entry/2021/11/17/112214   

・DP DDPをPyTorch Lightningだと簡単？  
https://forxai.konicaminolta.com/blog/047   

## GPUの並び順
PyTorchは早い順に番号が小さい  
nvidia-smiと同じ順番に並べることもできる  
https://note.mjunya.com/posts/2021-12-13-multi-gpu-order/  
