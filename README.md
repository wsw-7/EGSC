# EGSC: Entropy-Guided Similarity Clustering Defense for Federated Learning

 Federated Learning | Targeted Label-Flipping Attacks

## Overview

Federated learning (FL) enables multiple clients to collaboratively train a global model without sharing their raw training data. However, malicious clients may manipulate local training labels and introduce poisoned updates, undermining global model performance. Defending against targeted label-flipping attacks is particularly challenging under heterogeneous (non-IID) data distributions and partial client participation.

**Entropy-Guided Similarity Clustering Defense (EGSC)** is a research framework designed to address this setting by integrating three complementary components:

1. **Entropy-diversity-guided client selection**, to improve class balance and the diversity of client data distributions within the selected set.
2. **Similarity-based suspicious client detection**, to analyze relationships among last-layer model updates.
3. **Robust aggregation**, to aggregate updates from a relatively safe client cluster while excluding potentially suspicious updates.

This repository accompanies the EGSC research project and currently provides a **partial release of the underlying federated learning experimental code**.

## Code Availability

> **Important — partial release:** The EGSC-specific implementations of entropy-diversity-guided client selection, similarity-based client detection, and robust aggregation are **not included in this repository**. These components are withheld pending publication and further release review.

## Repository Structure

```text
EGSC/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── src/
│   ├── aggregation.py             # Baseline aggregation and defense methods
│   ├── sampling.py                # Dataset loading and data partitioning
│   ├── environment_federated.py   # Federated learning training environment
│   ├── experiment_federated.py    # Experiment entry point
│   ├── models.py                  # Neural network architectures
│   ├── datasets.py                # Dataset wrappers and label-flipping utility
│   └── utils.py                   # Supporting utilities
└── notebooks/
    ├── Experiments_CIFAR10.ipynb
    └── Experiments_MNIST.ipynb
```

## Datasets

The public code supports:

| Dataset | Task | Download |
| --- | --- | --- |
| MNIST | Handwritten digit classification | Via `torchvision.datasets.MNIST` |
| CIFAR-10 | Image classification | Via `torchvision.datasets.CIFAR10` |

## Usage

```bash
jupyter notebook notebooks/Experiments_MNIST.ipynb
```

or

```bash
jupyter notebook notebooks/Experiments_CIFAR10.ipynb
```



## License

This repository is distributed under the **Apache License, Version 2.0 (January 2004)** for the material authored or licensed by the EGSC project maintainers. See the [LICENSE](LICENSE) file for the full Apache-2.0 license terms.

## Contact

For questions about the publicly released code, please open an issue in this GitHub repository.
