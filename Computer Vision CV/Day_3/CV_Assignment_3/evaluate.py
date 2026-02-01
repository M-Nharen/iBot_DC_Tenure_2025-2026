import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import torch
from torchvision import datasets,transforms,models
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

all_labels = []
all_preds = []

val_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
])

test_dataset = datasets.ImageFolder('/home/mnharen/c-projects/iBot/Kaggle_data_set/test',transform = val_transforms)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

model = models.resnet18(weights=None)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features,2)

model.load_state_dict (torch.load ('best_model.pth'))
model.to(device) 
model.eval ()

correct = 0
total = 0

with torch.no_grad ():
    for images , labels in test_loader:
        images , labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data , 1)

        total += labels . size (0)
        correct += ( predicted == labels ).sum().item ()

        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

test_accuracy = 100 * correct / total
print (f'Test Accuracy : { test_accuracy :.2f}% ')
          
cm = confusion_matrix(all_labels,all_preds)
plt.figure(figsize=(8,6))
sns.heatmap(cm,annot= True,fmt='d',cmap = 'Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.savefig('confusion_matrix.png')
plt.show()