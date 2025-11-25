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
bpy.context.object.location[2] = 0
bpy.context.object.rotation_euler[0] = 0 #  0
bpy.context.object.rotation_euler[1] = 0 #  0
bpy.context.object.rotation_euler[2] = 0 #  0
ob.select_set(False)
ob = bpy.context.scene.objects["L02.Bicep"]
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
ob = bpy.context.scene.objects["L03.Forearm"]
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
ob = bpy.context.scene.objects["L04.Wrist1"]
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
ob = bpy.context.scene.objects["L05.Wrist2"]
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
ob = bpy.context.scene.objects["L06.Camera"]
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
ob = bpy.context.scene.objects["L07.Effector"]
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
ob = bpy.context.scene.objects["L08.LeftFinger"]
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
ob = bpy.context.scene.objects["L09.LeftFingerEnd"]
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
ob = bpy.context.scene.objects["L10.RightFinger"]
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
ob = bpy.context.scene.objects["L11.RightFingerEnd"]
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
bpy.context.object.rotation_euler[0] = -1.5707994 #  -90.000175
bpy.context.object.rotation_euler[1] = 2.4071114 #  137.91733
bpy.context.object.rotation_euler[2] = -2.3841858e-06 #  -0.00013660379
ob.select_set(False)
ob = bpy.context.scene.objects["L03.Forearm"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.27478293
bpy.context.object.location[1] = -0.005374124
bpy.context.object.location[2] = -0.019483179
bpy.context.object.rotation_euler[0] = 1.5707946 #  89.9999
bpy.context.object.rotation_euler[1] = 2.4071114 #  137.91733
bpy.context.object.rotation_euler[2] = -2.3841858e-06 #  -0.00013660379
ob.select_set(False)
ob = bpy.context.scene.objects["L04.Wrist1"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.41447318
bpy.context.object.location[1] = 0.0010009715
bpy.context.object.location[2] = -0.17417544
bpy.context.object.rotation_euler[0] = 0.61846346 #  35.435345
bpy.context.object.rotation_euler[1] = 0.42532367 #  24.369251
bpy.context.object.rotation_euler[2] = -2.0962715 #  -120.10751
ob.select_set(False)
ob = bpy.context.scene.objects["L05.Wrist2"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.48536533
bpy.context.object.location[1] = 0.001108408
bpy.context.object.location[2] = -0.25288686
bpy.context.object.rotation_euler[0] = 0.23851779 #  13.666063
bpy.context.object.rotation_euler[1] = -0.99618 #  -57.076912
bpy.context.object.rotation_euler[2] = 2.0485818 #  117.37509
ob.select_set(False)
ob = bpy.context.scene.objects["L06.Camera"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.40351835
bpy.context.object.location[1] = -0.064768314
bpy.context.object.location[2] = -0.23937665
bpy.context.object.rotation_euler[0] = -1.8093177 #  -103.66627
bpy.context.object.rotation_euler[1] = 0.9961799 #  57.076904
bpy.context.object.rotation_euler[2] = -1.0930107 #  -62.624897
ob.select_set(False)
ob = bpy.context.scene.objects["L07.Effector"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.35604057
bpy.context.object.location[1] = -0.103092775
bpy.context.object.location[2] = -0.231476
bpy.context.object.rotation_euler[0] = 1.4189879 #  81.30202
bpy.context.object.rotation_euler[1] = -0.5563947 #  -31.879068
bpy.context.object.rotation_euler[2] = -0.8110561 #  -46.47009
ob.select_set(False)
ob = bpy.context.scene.objects["L08.LeftFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.29437718
bpy.context.object.location[1] = -0.13199411
bpy.context.object.location[2] = -0.19688138
bpy.context.object.rotation_euler[0] = 1.0092012 #  57.822968
bpy.context.object.rotation_euler[1] = 0.12877332 #  7.3781676
bpy.context.object.rotation_euler[2] = 0.6791225 #  38.910854
ob.select_set(False)
ob = bpy.context.scene.objects["L09.LeftFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.26426473
bpy.context.object.location[1] = -0.17027842
bpy.context.object.location[2] = -0.20816395
bpy.context.object.rotation_euler[0] = 1.0092012 #  57.822968
bpy.context.object.rotation_euler[1] = 0.12877332 #  7.3781676
bpy.context.object.rotation_euler[2] = 0.6791225 #  38.910854
ob.select_set(False)
ob = bpy.context.scene.objects["L10.RightFinger"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.30964306
bpy.context.object.location[1] = -0.16141953
bpy.context.object.location[2] = -0.248089
bpy.context.object.rotation_euler[0] = 1.0092012 #  57.822968
bpy.context.object.rotation_euler[1] = 0.12877332 #  7.3781676
bpy.context.object.rotation_euler[2] = 0.6791225 #  38.910854
ob.select_set(False)
ob = bpy.context.scene.objects["L11.RightFingerEnd"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = ob
ob.select_set(True)
bpy.context.object.location[0] = 0.26932183
bpy.context.object.location[1] = -0.17999007
bpy.context.object.location[2] = -0.22508536
bpy.context.object.rotation_euler[0] = 1.0092012 #  57.822968
bpy.context.object.rotation_euler[1] = 0.12877332 #  7.3781676
bpy.context.object.rotation_euler[2] = 0.6791225 #  38.910854
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

