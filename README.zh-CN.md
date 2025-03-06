🌍 [English](README.md) | 🇨🇳 [中文](README.zh-CN.md)

# K210-TFlite-keras-conver-kmodel
转换keras模型或者TFlite模型到K210的专用模型格式kmodel的方法

## 环境要求
- [tensorflow](https://tensorflow.google.cn/install)

## 转换成TFlite
一般我们用tensorflow训练模型时，得到的模型文件夹都是扩展名为 __.h5__ 的模型文件
```bash
例如 <models.h5>
```
这种模型需要先转换成 __.tflite__ 格式的模型文件才能进行下一步的操作，运行 __convert_tflite.py__
```bash
python3 convert_tflite.py --dataset <./models/你的模型文件>
 ```
运行后会在目录下生成 __convert.tflite__

## 转换成Kmodel
在转换成Kmodel之前，我们要用到 __[nncase工具箱](https://github.com/kendryte/nncase/tree/release/1.0)__ 下载好后的文件里已经包含了 nncaseV0.2.0beta4 因为 __k210只支持v3/v4的kmodel__ v3的kmodel是用v0.1.0rc5,v4的是用v0.2.0beta4 （官方推荐）

先切换到nncase的工作目录
```bash
cd ./ncc_win_x86_64
```
然后把.tflite文件复制到ncc_win_x86_64文件下，在dataset文件中放入你训练该模型时 __所使用的图片数据__ 作为量化的校准数据集
然后运行以下命令
```bash
./ncc compile ./<你的模型名字>.tflite ./<输出的模型名字>.kmodel -i tflite -o kmodel --dataset dataset --inference-type uint8
```
可以更改 __--inference-type__ 来更改生成模型时所使用的量化方式 (uint8、float)
- 如果选择float则模型不作任何量化

在目录下会生成 __.kmodel__ 文件

## Linux

可以在 [这里](https://github.com/kendryte/nncase/releases/tag/v0.2.0-beta4)下载linux架构的文件，或者使用以下命令下载
```bash
wget https://github.com/kendryte/nncase/releases/download/v0.2.0-beta4/ncc_linux_x86_64.tar.xz
tar -xvf ncc_linux_x86_64.tar.xz
cd /ncc_linux_x86_64
mkdir dataset
mkdir models
```
然后使用方法如上同