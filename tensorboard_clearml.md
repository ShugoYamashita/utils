# ClearML  

実験管理の参考  
https://qiita.com/nkriskeeic/items/92902ea033d72c93b6ea  

ClearMLの参考  
公式チュートリアルに詳細な説明あり  
https://clear.ml/docs/latest/docs/references/sdk/task/#taskcreate  
日本語  
https://qiita.com/hkambe/items/87d1aab7bdd13ecd81da  
https://zenn.dev/siy1121/articles/5f44bcfb65ca10  

Task.initのdefault  
```python
classmethod init(project_name=None, task_name=None, task_type=<TaskTypes.training: 'training'>,
tags=None, reuse_last_task_id=True, continue_last_task=False, output_uri=None,
auto_connect_arg_parser=True, auto_connect_frameworks=True,
auto_resource_monitoring=True, auto_connect_streams=True, deferred_init=False)
```
同じproject_name, task_nameのTaskを呼び出すときに、reuse_last_task_id=Falseとすると、新しいTaskが作られる。  
既存のTaskを参照したい場合、Task.get_taskメソッドを呼び出す。  
tensorboardで記録すればClearMLから確認できる  

```python
# 実験スクリプト冒頭で以下を呼ぶ
from clearml import Task
# 最低限
task = Task.init(project_name='プロジェクト名', task_name='実験名') # 環境情報や標準出力は自動で記録される
# 推奨 同名のTaskが存在しても新しいTaskを作成。:monitor:gpuと:monitor:machineを記録しない
task = Task.init(project_name='Project', task_name='exp', reuse_last_task_id=False, auto_resource_monitoring=False)


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
task.close()
```


# tensorboard  
tensorboardの参考  
https://qiita.com/nj_ryoo0/items/f3aac1c0e92b3295c101  
https://qiita.com/kannkyo/items/3ff9c5c66c449450d7ab  
https://qiita.com/nj_ryoo0/items/f3aac1c0e92b3295c101#tensorboardx-との関係  

