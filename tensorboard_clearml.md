# ClearML  

実験管理の参考  
https://qiita.com/nkriskeeic/items/92902ea033d72c93b6ea  

ClearMLの参考  
https://qiita.com/hkambe/items/87d1aab7bdd13ecd81da  
https://zenn.dev/siy1121/articles/5f44bcfb65ca10  

```python
# 実験スクリプト冒頭で以下を呼ぶ
from clearml import Task  
task = Task.init(project_name='プロジェクト名', task_name='実験名') # 環境情報や標準出力は自動で記録される  

# ハイパーパラメータの記録  
hparams = {
  "learning_rate": 1e-3,
}
task.connect(hparams)

# 学習中  
# スカラー記録  
task.logger.report_scalar(title, series, value, iteration)

# メディアファイル記録  
task.logger.report_media(
            title=title,
            series=series,
            iteration=iteration,
            local_path=path_to_file, # 動画像、音声、htmlファイルなど
            delete_after_upload=True,
        )
task.task
```

# tensorboard  
tensorboardの参考  
https://qiita.com/nj_ryoo0/items/f3aac1c0e92b3295c101  
https://qiita.com/kannkyo/items/3ff9c5c66c449450d7ab  
https://qiita.com/nj_ryoo0/items/f3aac1c0e92b3295c101#tensorboardx-との関係  

