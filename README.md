# planar-defect-analysis-algorithm (PDA)
Code for classifying various defects, including intrinstic and extrinsic stacking faults, twin boundaries and HCP phase in the FCC crystal. This code can work in the python script modifier of [OVITO](https://www.ovito.org/). To use PDA, you must first activate the common neighbor analysis in the OVITO. After analyzing, atoms can be colored based on their structural types using color coding modifier of OVITO. If the code cannot run due to Python version issues, you can replace "pda[index] = x" (here, x = 0, 1, 2...) with "with pda: pda[index] = x".
