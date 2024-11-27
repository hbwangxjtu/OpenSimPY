# OpenSimPY

## 1 Introduction

To achieve the python development for OpenSim, this repository gives an simply example to plot the muscle-tendon lengths changing with the shoulder and elbow. There is a little difference between the code results and opensim. The main problem is that the variation is consistent when the elv_angle is fixed at the 100(deg) in this sccript. It should be solved in the future.

> The OpenSim model used in this repository comes from "A Model of the Upper Extremity for Simulating Musculoskeletal Surgery and Analyzing Neuromuscular Control." Annals of Biomedical Engineering, 2005. 

anglecontrol.py: fixing the **elv-angle** to **100 deg** and changing the **shoulder-elv** angle within the scope of **[0,180] deg**.

## 2 Installation 
### 1 create conda environment
>  conda create -n opensim_scripting 
>  conda activate opensim_env

### 2 install opensim python package
> conda install -c kidzik opensim
> pip sintall numpy==1.26.0

### results1:
![alt text](<./muscle length vs shoulder_elv.png>)

### reference1:
![alt text](<./Plotter_OpenSim1.png>)

### results2:
![alt text](<./muscle length vs elbow_flexion.png>)

### reference2:
![alt text](<./Plotter_OpenSim2.png>)