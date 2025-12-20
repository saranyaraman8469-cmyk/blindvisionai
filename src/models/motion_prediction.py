import torch
import torch.nn as nn

class MotionPredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=4, hidden_size=64, num_layers=2, batch_first=True)
        self.fc = nn.Linear(64, 4)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])


if __name__ == "__main__":
    model = MotionPredictor()
    dummy_seq = torch.randn(1, 10, 4)  # 10 time steps
    prediction = model(dummy_seq)
    print("Future obstacle position:", prediction)
