from tensorflow import keras,lite
import argparse

parser = argparse.ArgumentParser(description='转换h5 -> tflite')

parser.add_argument('--models',type=str,required=True,help='模型文件')

args=parser.parse_args()

def main(models=args.models):
    model=keras.models.load_model(models)

    converter=lite.TFLiteConverter.from_keras_model(model)

    tflite_model=converter.convert()

    with open('convert.tflite', 'wb') as f:
        f.write(tflite_model)

main()