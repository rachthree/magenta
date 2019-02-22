## Introduction
This folder contains the files specific to the CS230, Winter 19 Project. The project aims to modify Piano Genie to take in a chord progression and button contour to provide a more musically structured output.

Files in this folder are generally documentation and datasets.

## Modified Code

New and modified Magenta code are linked below:

[Model configurations](/magenta/models/piano_genie/configs.py) - added IQAE + delta time and IQAE + delta time + chord configurations.

[Model](/magenta/models/piano_genie/model.py) - added the new configurations and capability to include chord progression features.

[Training](/magenta/models/piano_genie/train.py) - proposed model is now default.

The below code modifications are in progress:

[Chord inference](/magenta/music/chord_inference.py) - Currently being modified to ensure alignment with proposed methodology regarding chord progressions.

[Dataset reader](/magenta/models/piano_genie/loader.py) - Currently being modified to provide the information model.py needs.
