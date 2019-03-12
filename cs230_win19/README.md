## Introduction
This folder contains the files specific to the Stanford University CS230, Winter 2019 Project. The project aims to modify Piano Genie to take in a chord progression and button contour to provide a more musically structured output.

Files in this folder are generally documentation and datasets.

## Modified Code

New and modified Magenta code are linked below:

[Model configurations](/magenta/models/piano_genie/configs.py) - added IQAE + delta time and IQAE + delta time + chord configurations. Other parameters changed to match what was done for the [baseline IQAE + delta time model](https://arxiv.org/pdf/1810.05246.pdf).

[Model](/magenta/models/piano_genie/model.py) - added the new configurations and capability to include chord progression features.

[Training](/magenta/models/piano_genie/train.py) - proposed model is now default.



The below code modifications are in progress:

[Chord inference](/magenta/music/chord_inference.py) - Currently being modified to ensure alignment with proposed methodology regarding chord progressions.

[Dataset reader](/magenta/models/piano_genie/loader.py) - Currently being modified to provide the information model.py needs.

## Instructions
For development:

It is highly recommended to use TensorFlow GPU (pip install tensorflow-gpu) when possible. Magenta will use whatever version of TensorFlow is installed in your Python environment.

Clone this fork, and while in the main Magenta direcotry, execute the following setup command:

```bash
python setup.py develop
```

This will allow you to develop in the directory where you cloned this fork without needing to go into the site-packages folder in your Python environment. A link will be created in site-packages instead. 

For installation into site-packages:

```bash
python setup.py install
```

If you want to use the Piano Genie updates, "pip install magenta" cannot be used as this will pull from the official repo.
