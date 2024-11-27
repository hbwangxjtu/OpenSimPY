# OpenSimPY

## 1. Introduction

This repository provides a simple example of Python scripting for **OpenSim**, demonstrating how to plot **muscle-tendon length** changes in response to variations in shoulder and elbow joint angles. While there are minor discrepancies between my results and OpenSim's built-in plotting functionality, the main focus of this script is on analyzing muscle length variations with a fixed elevation angle of elv_angle.

> The OpenSim model used in this repository comes from "A Model of the Upper Extremity for Simulating Musculoskeletal Surgery and Analyzing Neuromuscular Control." Annals of Biomedical Engineering, 2005. 

anglecontrol.py: fixing the **elv-angle** to **100°** and changing the **shoulder-elv** angle within the scope of **[0,180]°**.

Results of Opensim are obtained under a manual Coordinates that the elv_angle are set to 100°.

## 2. Installation 
#### 1. Create conda environment
```
conda create -n opensim_scripting 
conda activate opensim_env
```
#### 2. Install opensim python package
```
conda install -c kidzik opensim
pip sintall numpy==1.26.0
```
#### Results1:
![alt text](<./muscle length vs shoulder_elv.png>)

#### Reference1:
![alt text](<./Plotter_OpenSim1.png>)

### Results2:
![alt text](<./muscle length vs elbow_flexion.png>)

### Reference2:
![alt text](<./Plotter_OpenSim2.png>)

