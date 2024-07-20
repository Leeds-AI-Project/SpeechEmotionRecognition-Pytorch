import argparse
import functools
import os
from pathlib import Path

from flask import request
from mser.utils.utils import add_arguments, print_arguments

from blueprints.api import api_bp
from pytorch import infer


@api_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        prefix_path = Path(__file__).resolve()
        project_dir = os.path.dirname(prefix_path)
        filename = os.path.splitext(file.filename)[0] + '.wav'
        file_path = os.path.join(project_dir, filename)
        print('filename', file_path)

        file.save(file_path)

        parser = argparse.ArgumentParser(description=__doc__)
        add_arg = functools.partial(add_arguments, argparser=parser)
        add_arg('configs', str, 'pytorch/configs/bi_lstm.yml', '配置文件')
        add_arg('use_gpu', bool, True, '是否使用GPU预测')
        add_arg('audio_path', str, file_path, '音频路径')
        add_arg('model_path', str, 'pytorch/models/BaseModel_Emotion2Vec/best_model/', '导出的预测模型文件路径')
        args = parser.parse_args()
        print_arguments(args=args)

        return infer.run(args), 200
