import opensim as osim
import matplotlib.pyplot as plt
import numpy as np

# 加载模型
model = osim.Model("./Original Files - UpperExtremityModel/Stanford VA upper limb model_0.osim")
state = model.initSystem()

def get_biceps_length_vs_angle(model, state, elv_angle_fixed, shoulder_angle_range):
    
    # 需要分析的肌肉名称列表
    muscle_names = [
        "BIClong",   # 肱二头肌长头
        "BICshort",  # 肱二头肌短头
        "TRIlong",   # 肱三头肌长头
        "TRIlat",    # 肱三头肌外侧头
        "TRImed"     # 肱三头肌内侧头
    ]
     # 获取所有目标肌肉
    muscles = {name: model.getMuscles().get(name) for name in muscle_names}
    # 固定肘部角度
    #elv_coord = model.getCoordinateSet().get("elv_angle")
    #elv_coord.setValue(state, elv_angle_fixed)
    
    # 存储不同角度下的肌肉长度
    lengths = {name: [] for name in muscle_names}
    
    # 遍历不同的肩关节角度
    for angle in shoulder_angle_range:
        # 设置肩关节角度
        shoulder_coord = model.getCoordinateSet().get("elbow_flexion")
        shoulder_coord.setValue(state, angle)
        
        # 更新模型状态
        model.realizeDynamics(state)
        
        # 获取每个肌肉的长度
        for name, muscle in muscles.items():
            muscle_length = muscle.getLength(state)
            lengths[name].append(muscle_length)
    
    return lengths

# 设置参数
elv_angle_fixed = 100  # 固定肘部角度
shoulder_angle_range = np.linspace(0, 130, 99)  # 肩关节角度范围

# 获取肌肉长度数据
lengths = get_biceps_length_vs_angle(model, state, elv_angle_fixed, shoulder_angle_range)

# 创建图表
plt.figure(figsize=(12, 8))

# 设置不同肌肉的颜色和线型
muscle_styles = {
    'BIClong': {'color': 'red', 'linestyle': '-', 'label': 'Biceps Long Head'},
    'BICshort': {'color': 'red', 'linestyle': '--', 'label': 'Biceps Short Head'},
    'TRIlong': {'color': 'blue', 'linestyle': '-', 'label': 'Triceps Long Head'},
    'TRIlat': {'color': 'blue', 'linestyle': '--', 'label': 'Triceps Lateral Head'},
    'TRImed': {'color': 'blue', 'linestyle': ':', 'label': 'Triceps Medial Head'}
}

# 绘制每个肌肉的长度曲线
for muscle_name, style in muscle_styles.items():
    plt.plot(shoulder_angle_range, 
            lengths[muscle_name], 
            color=style['color'], 
            linestyle=style['linestyle'], 
            label=style['label'])

# 设置图表属性
plt.xlabel('Shoulder Elevation Angle (degrees)')
plt.ylabel('Muscle Length (m)')
plt.title('Arm Muscles Length vs. Shoulder Elevation Angle')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# 调整布局以确保图例完全显示
plt.tight_layout()
plt.show()