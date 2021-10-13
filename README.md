dvc-sandbox
===

[DVC](https://dvc.org/)の説明用のとてもシンプルなサンプル.

## 使い方
(`git clone`し, numpyが使えるようになっている前提)
```
$ dvc init
$ dvc run -n preprocess \
    -d raw_dataset.csv \
    -o dataset.csv \
    python ./preprocess.py
$ dvc run -n train \
    -p train.epochs \
    -d ./train.py -d dataset.csv \
    -o model.json \
    -M result.json \
    python ./train.py
```