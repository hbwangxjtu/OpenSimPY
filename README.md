# OpenSimPY

## 1. Introduction

To achieve the python scripting for **OpenSim**, this repository gives an simple example to plot the muscle-tendon lengths changing with the joint variation of joint **shoulder** and **elbow**. In fact, there is a little difference between my results and OpenSim plot. However, the main problem is that the muscle length variations are consistent when the elv_angle is fixed at the 100(deg) in this script. It should be solved in the future.

> The OpenSim model used in this repository comes from "A Model of the Upper Extremity for Simulating Musculoskeletal Surgery and Analyzing Neuromuscular Control." Annals of Biomedical Engineering, 2005. 

anglecontrol.py: fixing the **elv-angle** to **100 deg** and changing the **shoulder-elv** angle within the scope of **[0,180] deg**.

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