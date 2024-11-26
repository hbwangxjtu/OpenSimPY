import opensim as osim

# 加载模型
model = osim.Model("./Original Files - UpperExtremityModel/Stanford VA upper limb model_0.osim")
state = model.initSystem()

# 设置固定角度
coordinate_set = model.getCoordinateSet()
print(coordinate_set)
# coordinate_set.get("elv_angle").setValue(state, 100)  # 设置肩胛提肌为100度

# # 固定其他角度
# coordinate_set.get("knee_angle_r").setLocked(state, True)
# coordinate_set.get("hip_angle_r").setLocked(state, True)

# # 仿真和导出状态文件
# manager = osim.Manager(model)
# manager.integrate(state)
