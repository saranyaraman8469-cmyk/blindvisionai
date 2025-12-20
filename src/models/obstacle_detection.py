import torch
import torch.nn as nn

class ObstacleDetector(nn.Module):
    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(
            nn.Conv2d(3, 16, 3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, stride=2, padding=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(32 * 56 * 56, 128),
            nn.ReLU(),
            nn.Linear(128, 4)  # bounding box output
        )

    def forward(self, x):
        return self.model(x)


if __name__ == "__main__":
    model = ObstacleDetector()
    dummy = torch.randn(1, 3, 224, 224)
    output = model(dummy)
    print("Obstacle detected:", output)
