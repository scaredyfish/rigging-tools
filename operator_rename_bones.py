import bpy
from bpy.props import StringProperty


class RenameBonesOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "bone.rename_bones"
    bl_label = "Rename Bones"
    bl_options = {'REGISTER', 'UNDO'}

    name_prefix = StringProperty(name='Name prefix', default='__rename')
    starting_index = bpy.props.IntProperty(name='Starting index', default=1)

    @classmethod
    def poll(cls, context):
        return context.active_bone is not None

    def execute(self, context):
        bones = sorted(bpy.context.selected_bones, key = lambda x: x.head.y)[::-1]
        
        for i, bone in enumerate(bones):
            bone.name = self.name_prefix + "." + str(i+self.starting_index)
            
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)


def register():
    bpy.utils.register_class(RenameBonesOperator)


def unregister():
    bpy.utils.unregister_class(RenameBonesOperator)


if __name__ == "__main__":
    register()

