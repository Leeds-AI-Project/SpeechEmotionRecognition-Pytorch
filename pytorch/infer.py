import argparse
import functools
import sys,mser
from mser.predict import MSERPredictor
from mser.utils.utils import add_arguments, print_arguments


# TODO: 待修改文件

def run(args_dict):
    # 获取识别器
    predictor = MSERPredictor(configs=args_dict.configs, model_path=args_dict.model_path, use_gpu=args_dict.use_gpu)

    label, score = predictor.predict(audio_data=args_dict.audio_path)
    print(args_dict)
    print(f'音频：{args_dict.audio_path} 的预测结果标签为：{label}，得分：{score}')
    return label


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    add_arg = functools.partial(add_arguments, argparser=parser)
    add_arg('configs', str, 'pytorch/configs/bi_lstm.yml', '配置文件')
    add_arg('use_gpu', bool, True, '是否使用GPU预测')
    add_arg('audio_path', str, 'pytorch/dataset/my_music_file/20240620_211706.m4a', '音频路径')
    add_arg('model_path', str, 'pytorch/models/BaseModel_Emotion2Vec/best_model/', '导出的预测模型文件路径')
    args = parser.parse_args()
    print_arguments(args=args)

    run(args)
