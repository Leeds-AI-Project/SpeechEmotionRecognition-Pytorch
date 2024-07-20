import torch
import torch.nn as nn

class CustomLSTM(nn.Module): # 复现的 LSTM 算法
    def __init__(self, input_size, hidden_size, bidirectional=True):
        super(CustomLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.bidirectional = bidirectional

        # 定义前向LSTMCell
        self.lstm_fw = nn.LSTMCell(input_size, hidden_size)
        # 如果是双向LSTM，则定义后向LSTMCell
        if bidirectional:
            self.lstm_bw = nn.LSTMCell(input_size, hidden_size)

    def forward(self, x, hidden=None):
        batch_size, seq_len, _ = x.size()
        # 如果未提供隐状态，则初始化前向和后向的隐状态和细胞状态
        if hidden is None:
            h_fw = torch.zeros(batch_size, self.hidden_size).to(x.device)
            c_fw = torch.zeros(batch_size, self.hidden_size).to(x.device)
            if self.bidirectional:
                h_bw = torch.zeros(batch_size, self.hidden_size).to(x.device)
                c_bw = torch.zeros(batch_size, self.hidden_size).to(x.device)
        else:
            h_fw, c_fw = hidden[0]
            if self.bidirectional:
                h_bw, c_bw = hidden[1]

        outputs = []
        # 逐时间步进行计算
        for t in range(seq_len):
            # 前向LSTM计算
            h_fw, c_fw = self.lstm_fw(x[:, t, :], (h_fw, c_fw))
            if self.bidirectional:
                # 后向LSTM计算
                h_bw, c_bw = self.lstm_bw(x[:, seq_len - t - 1, :], (h_bw, c_bw))
            # 如果是双向LSTM，则拼接前向和后向的输出
            output = h_fw if not self.bidirectional else torch.cat((h_fw, h_bw), dim=1)
            outputs.append(output.unsqueeze(1))

        outputs = torch.cat(outputs, dim=1)
        if self.bidirectional:
            return outputs, ((h_fw, c_fw), (h_bw, c_bw))
        else:
            return outputs, (h_fw, c_fw)
