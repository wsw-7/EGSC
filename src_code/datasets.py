"""Dataset adapters, including an existing standard label-flip attack."""
from torch.utils.data import Dataset, ConcatDataset


class CustomDataset(Dataset):
    def __init__(self, dataset, indices, source_class=None, target_class=None):
        self.dataset = dataset
        self.indices = [int(i) for i in indices]
        self.source_class = source_class
        self.target_class = target_class

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, index):
        x, y = self.dataset[self.indices[index]]
        if self.source_class is not None and y == self.source_class:
            y = self.target_class
        return x, y


class PoisonedDataset(Dataset):
    def __init__(self, dataset, source_class, target_class):
        self.dataset = dataset
        self.source_class = source_class
        self.target_class = target_class

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        x, y = self.dataset[index]
        if y == self.source_class:
            y = self.target_class
        return x, y


def combine_datasets(list_of_datasets):
    return ConcatDataset(list_of_datasets)
