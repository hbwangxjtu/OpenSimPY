import opensim as osim
import matplotlib.pyplot as plt
import numpy as np

# load model
model = osim.Model("./Original Files - UpperExtremityModel/Stanford VA upper limb model_0.osim")
state = model.initSystem()

muscleset = model.getMuscles()
for i in range(muscleset.getSize()):
    current_muscle = muscleset.get(i)
    current_muscle.setActivation(state, 0.5)

def get_biceps_length_vs_angle(model, state, elv_angle_fixed, shoulder_angle_range):
    
    elv_coord = model.getCoordinateSet().get("elv_angle")
    elv_coord.setValue(state, elv_angle_fixed)

    # mmuscle list
    muscle_names = [
        "BIClong",  
        "BICshort",  
        "TRIlong",   
        "TRIlat",    
        "TRImed"     
    ]
    
    muscles = {name: model.getMuscles().get(name) for name in muscle_names}
    lengths = {name: [] for name in muscle_names}
    
    for angle in shoulder_angle_range:
        # set shoulder_elv
        shoulder_coord = model.getCoordinateSet().get("shoulder_elv")
        shoulder_coord.setValue(state, angle)
        
        # update state
        model.realizeDynamics(state)
        
        # obtain lengths of each muscle
        for name, muscle in muscles.items():
            muscle_length = muscle.getLength(state)
            lengths[name].append(muscle_length)
    
    return lengths

# set parameters
elv_angle_fixed = 100*np.pi/180
shoulder_angle_range = np.linspace(0, 130*np.pi/180, 130) 

lengths = get_biceps_length_vs_angle(model, state, elv_angle_fixed, shoulder_angle_range)

plt.figure(figsize=(12, 8))

muscle_styles = {
    'BIClong': {'color': 'm', 'linestyle': '-', 'label': 'Biceps Long Head'},
    'BICshort': {'color': 'b', 'linestyle': '-', 'label': 'Biceps Short Head'},
    'TRIlong': {'color': 'y', 'linestyle': '-', 'label': 'Triceps Long Head'},
    'TRIlat': {'color': 'c', 'linestyle': '-', 'label': 'Triceps Lateral Head'},
    'TRImed': {'color': 'k', 'linestyle': '-', 'label': 'Triceps Medial Head'}
}


shoulder_angle_range = np.degrees(shoulder_angle_range)

for muscle_name, style in muscle_styles.items():
    plt.plot(shoulder_angle_range, 
            lengths[muscle_name], 
            color=style['color'], 
            linestyle=style['linestyle'], 
            label=style['label'])

plt.xlabel('Shoulder Elevation Angle (degrees)')
plt.ylabel('Muscle Length (m)')
plt.title('Arm Muscles Length vs. shoulder Flexion Angle')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

plt.tight_layout()
plt.show()