import opensim as osim
import matplotlib.pyplot as plt
import numpy as np

# load opensim model
model = osim.Model("./Original Files - UpperExtremityModel/Stanford VA upper limb model_0.osim")
# state = model.initSystem()

# get muscles of model
# muscles = model.getMuscles()

# model_joints = model.getJointSet()
# for i in range(model_joints.getSize()):
#     joint = model_joints.get(i)
#     print(f"Joint name: {joint.getName()}")

joints = model.getJointSet()
# coords = model.getCoordinateSet()

# for i in range(coords.getSize()):
#     coord = coords.get(i)
#     print(f"coord name: {coord.getName()}")

# 遍历所有关节并获取运动范围
for joint in joints:
    # 获取关节的名称
    joint_name = joint.getName()
    coord = model.getCoordinateSet().get('elv_angle')  # 默认获取第一个自由度
    lower_limit = coord.getMin()  # 最小运动范围
    upper_limit = coord.getMax()  # 最大运动范围

    # 打印关节的运动范围
    print(f"Joint: {joint_name}, Range of Motion: {lower_limit} to {upper_limit}")
    


# model_joints = model.getJointSet()
# for i in range(model_joints.getSize()):
#     joint = model_joints.get(i)
#     print(f"Joint name: {joint.getName()}")

# coords = joint.getCoordinate()
# for i in range(coords.getSize()):
#     coord = coords.get(i)
#     print(f"Coordinate name: {coord.getName()}")
#     print(f"Range: {coord.getRangeMin()} to {coord.getRangeMax()} {coord.getUnits()}")
#     print(f"Motion type: {coord.getMotionType()}")
#     print(f"Locked: {coord.getLocked()}")
#     print("---")

# 
# def get_muscle_lengths_for_shoulder_elv_change(model, elv_angle_fixed, shoulder_angle_range, muscle_names):
#     lengths = {muscle_name: [] for muscle_name in muscle_names}
    
#     # 
#     elv_angle_joint = model.getJointSet().get("elv_angle")  # 假设elv_angle关节名为"elv_angle"
#     elv_angle_coord = elv_angle_joint.getCoordinates()[0]  # 获取角度坐标，假设是第一个坐标
#     elv_angle_coord.setValue(elv_angle_fixed)  # 固定elv_angle角度
    
#     # 模拟不同的shoulder_elv角度
#     for shoulder_elv_angle in shoulder_angle_range:
#         # 设置shoulder_elv角度
#         shoulder_joint = model.getJointSet().get("shoulder_evl")  # 假设肩部关节名为"shoulder"
#         shoulder_elv_coord = shoulder_joint.getCoordinates()[0]  # 假设肩部角度是第一个坐标
#         shoulder_elv_coord.setValue(shoulder_elv_angle)
        
#         # 计算模型的肌肉长度
#         model.realizeDynamics()  # 计算模型的动态
#         for muscle in muscles:
#             muscle_length = muscle.getLength()  # 获取肌肉长度
#             lengths[muscle.getName()].append(muscle_length)
    
#     return lengths

# # fix "elv_angle" angle 
# elv_angle_fixed = 100  

# # set`shoulder_elv` scope
# shoulder_angle_range = np.linspace(0, 180, 100)  # 从0到90度的变化
# muscle_names = [muscle.getName() for muscle in muscles]

# # get data 
# lengths_data = get_muscle_lengths_for_shoulder_elv_change(model, elv_angle_fixed, shoulder_angle_range, muscle_names)

# # visualize muscle length 
# plt.figure(figsize=(10, 6))
# for muscle_name, lengths in lengths_data.items():
#     plt.plot(shoulder_angle_range, lengths, label=muscle_name)

# plt.xlabel('Shoulder Elevation Angle (degrees)')
# plt.ylabel('Muscle Length (m)')
# plt.legend(loc='upper left')
# plt.title('Muscle Length vs. Shoulder Elevation Angle')
# plt.show()