# Federated CIFAR-10 Classification with Flower and PyTorch

This project demonstrates a federated-learning workflow for CIFAR-10 image
classification using PyTorch and the Flower framework. It is organized around
separate client and server applications, with local client training and
evaluation coordinated through Federated Averaging (FedAvg).

> This project uses Flower's PyTorch quickstart structure as its foundation.
> The repository is presented as a learning/implementation project rather than
> as an original federated-learning framework.

## What the project demonstrates

- A convolutional neural network for CIFAR-10 classification
- IID partitioning of CIFAR-10 across simulated federated clients
- Local client-side training and validation
- Server-side FedAvg aggregation across training rounds
- Centralized evaluation of the global model
- Saving the final global model after training

## Model

The CNN contains three convolutional blocks:

1. 3 → 32 channels
2. 32 → 64 channels
3. 64 → 128 channels

Each convolution is followed by ReLU and max pooling. The extracted features
are flattened and passed through a 256-unit fully connected layer followed by
a 10-class output layer.

## Repository structure

```text
Federated_Learning_CIFAR10/
├── pytorchexample/
│   ├── __init__.py
│   ├── client_app.py
│   ├── server_app.py
│   └── task.py
├── .gitignore
├── pyproject.toml
└── README.md
```

### `client_app.py`

Defines the Flower client behavior. Each client receives the current global
model, trains it on its local CIFAR-10 partition, and returns updated model
parameters and training metrics. It also performs local validation.

### `server_app.py`

Defines the Flower server application and FedAvg strategy. The server runs the
configured number of federated rounds, performs centralized evaluation of the
global model, and saves the final model weights.

### `task.py`

Contains the PyTorch CNN, CIFAR-10 preprocessing and partitioning, local
training loop, and evaluation functions.

## Configuration

The default Flower configuration uses:

- 10 server rounds
- 5 local epochs per round
- learning rate of 0.01
- batch size of 32
- evaluation fraction of 0.5

These values can be changed in `pyproject.toml`.

## Running the project

Create and activate a Python environment, then install the project:

```bash
pip install -e .
```

Run the Flower simulation:

```bash
flwr run .
```

Flower downloads and partitions CIFAR-10 automatically through
`flwr-datasets`.

## Generated files

The server saves the final model weights as:

```text
final_model.pt
```

Model checkpoints are intentionally excluded from Git because they are
generated artifacts and are not needed to understand the implementation.

## Technologies

Python · PyTorch · Flower · Flower Datasets · torchvision · CIFAR-10
