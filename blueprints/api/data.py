import os
from flask import request, app
from pydub import AudioSegment

from blueprints.api import api_bp


# TODO: 待修改文件
#  from pytorch import infer
#  调用 infer.run() 使用模型进行分析，
#  参数需要修改


@api_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return 'No file part'

    file = request.files['audio']
    if file.filename == '':
        return 'No selected file'

    if file:
        filename = os.path.splitext(file.filename)[0] + '.wav'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # 将文件保存为临时文件
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(temp_path)

        # 使用 pydub 转换为 WAV 格式
        audio = AudioSegment.from_file(temp_path)
        audio.export(file_path, format="wav")

        # 删除临时文件
        os.remove(temp_path)

        return f'File successfully uploaded and saved as {filename}'
