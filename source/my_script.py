# blender file my_script.py
# by UserNameUnknown
#
import bpy
# to load this file, on the blender python console type the following
# for linux:
# myfile = '/the/full/path/to/my_script.py'
# for windows
# myfile = 'C:\\users\\username\\somefolder\\my_script.py'
# then type:
# exec(compile(open(myfile).read(), myfile, 'exec'))
#
# blender commands below
#
# link transform for pose index 0
#
ob = bpy.context.scene.objects["L00.Base"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 0
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L01.Shoulder"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 0.15643
bpy.context.object.rotation_euler[0] = 3.1415913 #  179.99992
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L02.Bicep"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = -0.005374836
bpy.context.object.location[2] = 0.28481
bpy.context.object.rotation_euler[0] = -1.570794 #  -89.99987
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L03.Forearm"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = -0.0053757955
bpy.context.object.location[2] = 0.69481003
bpy.context.object.rotation_euler[0] = 1.5708 #  90.000206
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L04.Wrist1"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0.00099845
bpy.context.object.location[2] = 0.9032401
bpy.context.object.rotation_euler[0] = -3.1415854 #  -179.99959
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L05.Wrist2"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0.001172733
bpy.context.object.location[2] = 1.00917
bpy.context.object.rotation_euler[0] = 1.5708 #  90.000206
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L06.Camera"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0.0013473995
bpy.context.object.location[2] = 1.1151
bpy.context.object.rotation_euler[0] = -3.1415854 #  -179.99959
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L07.Effector"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0.0013469541
bpy.context.object.location[2] = 1.176625
bpy.context.object.rotation_euler[0] = -2.5352078e-06 #  -0.00014525671
bpy.context.object.rotation_euler[1] = -7.2399807e-06 #  -0.00041482036
bpy.context.object.rotation_euler[2] = 1.5708 #  90.000206
ob.select_set(False)
ob = bpy.context.scene.objects["L08.LeftFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = -0.030500177
bpy.context.object.location[1] = 0.0013463367
bpy.context.object.location[2] = 1.246655
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 1.5707964 #  90
bpy.context.object.rotation_euler[2] = 1.5708 #  90.000206
ob.select_set(False)
ob = bpy.context.scene.objects["L09.LeftFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = -0.010077292
bpy.context.object.location[1] = 0.0013462454
bpy.context.object.location[2] = 1.292291
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 1.5707964 #  90
bpy.context.object.rotation_euler[2] = 1.5708 #  90.000206
ob.select_set(False)
ob = bpy.context.scene.objects["L10.RightFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.030500824
bpy.context.object.location[1] = 0.0013465578
bpy.context.object.location[2] = 1.246628
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 1.5707964 #  90
bpy.context.object.rotation_euler[2] = 1.5708 #  90.000206
ob.select_set(False)
ob = bpy.context.scene.objects["L11.RightFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.0100777075
bpy.context.object.location[1] = 0.0013463186
bpy.context.object.location[2] = 1.2922649
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 1.5707964 #  90
bpy.context.object.rotation_euler[2] = 1.5708 #  90.000206
ob.select_set(False)
obj = bpy.data.objects['L00.Base']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L01.Shoulder']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L02.Bicep']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L03.Forearm']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L04.Wrist1']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L05.Wrist2']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L06.Camera']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L07.Effector']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L08.LeftFinger']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L09.LeftFingerEnd']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L10.RightFinger']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
obj = bpy.data.objects['L11.RightFingerEnd']
obj.keyframe_insert(data_path='location',frame=0)
obj.keyframe_insert(data_path='rotation_euler',frame=0)
#
# link transform for pose index 1
#
ob = bpy.context.scene.objects["L00.Base"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 0
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L01.Shoulder"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0
bpy.context.object.location[1] = 0
bpy.context.object.location[2] = 0.15643
bpy.context.object.rotation_euler[0] = 3.1415918 #  179.99995
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0.73303604 #  41.99987
ob.select_set(False)
ob = bpy.context.scene.objects["L02.Bicep"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.0035965682
bpy.context.object.location[1] = -0.003994247
bpy.context.object.location[2] = 0.28481
bpy.context.object.rotation_euler[0] = -1.5707932 #  -89.99982
bpy.context.object.rotation_euler[1] = 0.59196854 #  33.917297
bpy.context.object.rotation_euler[2] = 0.7330379 #  41.999977
ob.select_set(False)
ob = bpy.context.scene.objects["L03.Forearm"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.17361286
bpy.context.object.location[1] = 0.14908722
bpy.context.object.location[2] = 0.625046
bpy.context.object.rotation_euler[0] = 1.5707846 #  89.99933
bpy.context.object.rotation_euler[1] = 1.8906102 #  108.32399
bpy.context.object.rotation_euler[2] = 0.73302436 #  41.999203
ob.select_set(False)
ob = bpy.context.scene.objects["L04.Wrist1"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.31638703
bpy.context.object.location[1] = 0.2862196
bpy.context.object.location[2] = 0.55951774
bpy.context.object.rotation_euler[0] = -1.1627343 #  -66.61977
bpy.context.object.rotation_euler[1] = -0.6563076 #  -37.603653
bpy.context.object.rotation_euler[2] = 2.0458999 #  117.22143
ob.select_set(False)
ob = bpy.context.scene.objects["L05.Wrist2"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.3912237
bpy.context.object.location[1] = 0.3534507
bpy.context.object.location[2] = 0.52634174
bpy.context.object.rotation_euler[0] = 0.18584275 #  10.6480055
bpy.context.object.rotation_euler[1] = -2.4037814 #  -137.72653
bpy.context.object.rotation_euler[2] = -0.7518296 #  -43.076664
ob.select_set(False)
ob = bpy.context.scene.objects["L06.Camera"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.45281506
bpy.context.object.location[1] = 0.43843076
bpy.context.object.location[2] = 0.511986
bpy.context.object.rotation_euler[0] = -1.38495 #  -79.35179
bpy.context.object.rotation_euler[1] = -0.73781145 #  -42.273483
bpy.context.object.rotation_euler[2] = 2.3897629 #  136.92332
ob.select_set(False)
ob = bpy.context.scene.objects["L07.Effector"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.48852575
bpy.context.object.location[1] = 0.48782012
bpy.context.object.location[2] = 0.503574
bpy.context.object.rotation_euler[0] = -1.771324 #  -101.489395
bpy.context.object.rotation_euler[1] = -0.81423175 #  -46.652042
bpy.context.object.rotation_euler[2] = -0.47927934 #  -27.460684
ob.select_set(False)
ob = bpy.context.scene.objects["L08.LeftFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.5456577
bpy.context.object.location[1] = 0.5286232
bpy.context.object.location[2] = 0.47348252
bpy.context.object.rotation_euler[0] = -0.74646676 #  -42.769394
bpy.context.object.rotation_euler[1] = -0.13715403 #  -7.858347
bpy.context.object.rotation_euler[2] = -2.1968257 #  -125.86884
ob.select_set(False)
ob = bpy.context.scene.objects["L09.LeftFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.56110793
bpy.context.object.location[1] = 0.5755786
bpy.context.object.location[2] = 0.48098096
bpy.context.object.rotation_euler[0] = -0.74646676 #  -42.769394
bpy.context.object.rotation_euler[1] = -0.13715403 #  -7.858347
bpy.context.object.rotation_euler[2] = -2.1968257 #  -125.86884
ob.select_set(False)
ob = bpy.context.scene.objects["L10.RightFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.5126722
bpy.context.object.location[1] = 0.5594293
bpy.context.object.location[2] = 0.5145199
bpy.context.object.rotation_euler[0] = -0.74646676 #  -42.769394
bpy.context.object.rotation_euler[1] = -0.13715403 #  -7.858347
bpy.context.object.rotation_euler[2] = -2.1968257 #  -125.86884
ob.select_set(False)
ob = bpy.context.scene.objects["L11.RightFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.55019945
bpy.context.object.location[1] = 0.58574337
bpy.context.object.location[2] = 0.49454218
bpy.context.object.rotation_euler[0] = -0.74646676 #  -42.769394
bpy.context.object.rotation_euler[1] = -0.13715403 #  -7.858347
bpy.context.object.rotation_euler[2] = -2.1968257 #  -125.86884
ob.select_set(False)
obj = bpy.data.objects['L00.Base']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L01.Shoulder']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L02.Bicep']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L03.Forearm']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L04.Wrist1']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L05.Wrist2']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L06.Camera']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L07.Effector']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L08.LeftFinger']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L09.LeftFingerEnd']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L10.RightFinger']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
obj = bpy.data.objects['L11.RightFingerEnd']
obj.keyframe_insert(data_path='location',frame=60)
obj.keyframe_insert(data_path='rotation_euler',frame=60)
#
# select the target object
#
ob = bpy.context.scene.objects['L07.Effector']
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
#
# end of blender file
#

