🌍 [English](README.md) | 🇨🇳 [中文](README.zh-CN.md)


# K210-TFlite-Keras-Convert-Kmodel
A guide to converting Keras or TFLite models to the K210-specific Kmodel format.

## Requirements
- [TensorFlow](https://tensorflow.google.cn/install)

## Convert to TFLite
When training models with TensorFlow, the resulting model files typically have a __.h5__ extension.
```bash
Example: <models.h5>
```
Before proceeding, these models need to be converted into the __.tflite__ format. Run the `convert_tflite.py` script:
```bash
python3 convert_tflite.py --dataset <./models/your_model_file>
```
After execution, a __convert.tflite__ file will be generated in the directory.

## Convert to Kmodel
Before converting to Kmodel, we need the __[nncase toolbox](https://github.com/kendryte/nncase/tree/release/1.0)__. The downloaded files include `nncase V0.2.0 beta4` because __K210 only supports V3/V4 Kmodel__. V3 Kmodel uses `V0.1.0 rc5`, while V4 uses `V0.2.0 beta4` (officially recommended).

First, navigate to the nncase working directory:
```bash
cd ./ncc_win_x86_64
```
Then, copy the `.tflite` file to the `ncc_win_x86_64` folder. Place the images used for training the model in the `dataset` folder as calibration data for quantization.

Run the following command:
```bash
./ncc compile ./<your_model_name>.tflite ./<output_model_name>.kmodel -i tflite -o kmodel --dataset dataset --inference-type uint8
```
You can modify __--inference-type__ to change the quantization method used when generating the model (`uint8`, `float`).
- If `float` is chosen, the model will not be quantized.

The output __.kmodel__ file will be generated in the directory.

## Linux

You can download the Linux version from [here](https://github.com/kendryte/nncase/releases/tag/v0.2.0-beta4) or use the following command:
```bash
wget https://github.com/kendryte/nncase/releases/download/v0.2.0-beta4/ncc_linux_x86_64.tar.xz
tar -xvf ncc_linux_x86_64.tar.xz
cd /ncc_linux_x86_64
mkdir dataset
```
Then, follow the same usage instructions as above.

