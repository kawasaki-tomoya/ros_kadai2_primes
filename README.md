# ros_kadai2_primes

## 概要
ROSを利用して、0.5秒間隔でカウントアップした数字をパブリッシャ(count.py)が発信し、受信したサブスクライバ(twice.py)で表示し、約数を出力します。

## 動作環境
Ubuntu 18.04.3 LTS(VirtualBoxで動作確認)

ROS melodic

## 導入
mypkgを以下のようなディレクトリに置く。（お使いの環境に合わせてください）

~/catkin_ws/src/

## 使い方
1. roscoreを起動

2. 新しい端末を起動し、rosrun mypkg count.pyを実行

3. 3つめの新しい端末を起動し、rosrun mypkg twice.pyを実行

4. ３つ目の端末にカウントされた数字と約数が表示されます。カウントされた数字が素数の場合はその旨が表示されます。

## ライセンス
このソースコードはMITライセンスで提供されています。LICENCEをお読みください。

## 作者
河崎 智哉
