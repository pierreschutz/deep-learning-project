
from torch.utils import data

def build_train_loaders(train_input, train_classes, test_input, test_classes, batch_size):
    tr_data = data.TensorDataset(train_input, train_classes)
    te_data = data.TensorDataset(test_input, test_classes)
    
    tr_loader = data.DataLoader(tr_data, batch_size)
    te_loader = data.DataLoader(te_data, batch_size)
    return tr_loader, te_loader


def build_test_loader(test_input, test_target, batch_size):
    test_dataset = data.TensorDataset(test_input, test_target)
    test_loader = data.DataLoader(test_dataset, batch_size)
    return test_loader

def build_two_ch_loader(train_input, train_classes, train_target, test_input,test_classes, test_target, batch_size):
    tr_data = data.TensorDataset(train_input, train_classes, train_target)
    te_data = data.TensorDataset(test_input,test_classes, test_target)
    
    tr_loader = data.DataLoader(tr_data, batch_size)
    te_loader = data.DataLoader(te_data, batch_size)
    return tr_loader, te_loader