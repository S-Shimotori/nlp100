# 言語処理100本ノック

> 言語処理100本ノックは，実践的な課題に取り組みながら，プログラミング，データ分析，研究のスキルを楽しく習得することを目指した問題集です

http://www.cl.ecei.tohoku.ac.jp/nlp100/

## 方針等

### Python

```bash
pyenv install 3.5.1
```

### MeCab and CaboCha

```bash
pip3 install mecab-python3==0.7
```

```bash
brew install crf++
crf_learn -v
CRF++ of 0.58

brew install cabocha
cabocha -v
cabocha of 0.69

tar xf cabocha-0.69.tar.bz2
cd cabocha-0.69/python
python3.5 setup.py install
```

### matplotlib

```bash
pip3 install six==1.10.0
pip3 install cycler==0.10.0
pip3 install numpy==1.11.0
pip3 install pyparsing==2.1.1
pip3 install python-dateutil==2.5.3
pip3 install pytz==2016.4
pip3 install matplotlib==1.5.1
```

### Graphviz

```bash
pip3 install graphviz==0.4.10
```

### Zsh

```bash
brew install zsh
echo $ZSH_VERSION
5.2
```
