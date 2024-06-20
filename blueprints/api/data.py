import os
from pathlib import Path

from flask import request, app
from pydub import AudioSegment
from config import config
from blueprints.api import api_bp
from pytorch import infer
import argparse
import functools
from mser.utils.utils import add_arguments, print_arguments


# TODO: 待修改文件
#  from pytorch import infer
#  调用 infer.run() 使用模型进行分析，
#  参数需要修改

@api_bp.route('/get')
def get_data():
    return 'haha'


@api_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print('11')
        return 'No file part'

    print('22')
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        prefix_path = Path(__file__).resolve()
        project_dir = os.path.dirname(prefix_path)
        filename = os.path.splitext(file.filename)[0] + '.wav'
        file_path = os.path.join(project_dir, filename)
        print('filename', file_path)
        # # 将文件保存为临时文件
        # temp_path = os.path.join(app.config['../../pytorch/dataset/my_music_file'], file.filename)
        # file.save(temp_path)

        # # 确保目录存在
        # os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 保存文件
        file.save(file_path)

        # # # 使用 pydub 转换为 WAV 格式
        # audio = AudioSegment.from_file(save_path)
        # audio.export(save_path, format="wav")
        #
        #
        # parser = argparse.ArgumentParser(description=__doc__)
        # add_arg = functools.partial(add_arguments, argparser=parser)
        # add_arg('configs', str, '../configs/bi_lstm.yml', '配置文件')
        # add_arg('use_gpu', bool, True, '是否使用GPU预测')
        # add_arg('audio_path', str, save_path, '音频路径')
        # add_arg('model_path', str, '../models/BiLSTM_Emotion2Vec/best_model/', '导出的预测模型文件路径')
        # args = parser.parse_args()
        # print_arguments(args=args)
        # print(77)
        # print(infer.run(args))
        #
        # # 删除临时文件
        # os.remove(temp_path)
        # return f'File successfully uploaded and saved as {filename}',200

        parser = argparse.ArgumentParser(description=__doc__)
        add_arg = functools.partial(add_arguments, argparser=parser)
        add_arg('configs', str, 'pytorch/configs/bi_lstm.yml', '配置文件')
        add_arg('use_gpu', bool, True, '是否使用GPU预测')
        add_arg('audio_path', str, file_path, '音频路径')
        add_arg('model_path', str, 'pytorch/models/BiLSTM_Emotion2Vec/best_model/', '导出的预测模型文件路径')
        args = parser.parse_args()
        print_arguments(args=args)
        return infer.run(args), 200
