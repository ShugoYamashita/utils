# cpuのコア数

- pythonのコードで確認

```python
import os
os.cpu_count()
```

参考

[1] https://qiita.com/sugulu_Ogawa_ISID/items/62f5f7adee083d96a587

- linuxコマンドで確認

物理cpuの数

```shell
grep physical.id /proc/cpuinfo | sort -u | wc -l
```

CPUごとのコア数
```
grep cpu.cores /proc/cpuinfo | sort -u
```

論理プロセッサーの数
```
grep processor /proc/cpuinfo | wc -l
```

参考

[2] https://access.redhat.com/ja/solutions/2159401
