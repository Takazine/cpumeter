# アナログ針式CPU負荷メーター

PCA9685とアナログ針メーターを使ったRaspberryPi用のCPU負荷メーターです。ついでにCPUの温度も表示します。RaspberryPi標準のRaspbian liteに導入する方法です。




### CPU情報取得 psutil を導入

```
sudo apt-get update
sudo apt-get install python3-pip python-psutil
sudo pip install psutil
```



### Pythonスクリプトをclone

```
git clone https://github.com/Takazine/cpumeter
cd cpumeter
```



### スクリプト実行

```
sudo chmod +x cpu_meter.py
./cpu_meter.py
```



