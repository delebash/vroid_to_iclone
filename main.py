import RLPy
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import *
from PySide2 import *
from PySide2.QtCore import *
from subprocess import Popen

avatar = None

class App:
    """GUI Application using PySide2 widgets"""

    def __init__(self):
        self.initUI()

    def initUI(self):
        # -- Create Pyside layout for RDialog --#
        self.transfer_vroid_character_dialog = RLPy.RUi.CreateRDialog()
        self.transfer_vroid_character_dialog.SetWindowTitle("Transfer Vroid Character")
        self.pyside_dialog = wrapInstance(int(self.transfer_vroid_character_dialog.GetWindow()), QtWidgets.QDialog)
        self.pyside_dialog.setFixedWidth(300)
        self.mocap_layout = self.pyside_dialog.layout()

        # -- Add UI Elements --#
        self.info = QtWidgets.QTextEdit()
        self.mocap_layout.addWidget(self.info)

        self.import_3DXchange_button = QtWidgets.QPushButton("Import fbx to 3DXchange")
        self.import_3DXchange_button.clicked.connect(self.import_3dxchange)
        self.mocap_layout.addWidget(self.import_3DXchange_button)

        self.update_character_iClone_button = QtWidgets.QPushButton("Update character in iClone")
        self.update_character_iClone_button.clicked.connect(self.update_character_iClone)
        self.mocap_layout.addWidget(self.update_character_iClone_button)

        return

    def import_3dxchange(self):
        Popen(["D:\Program Files\Reallusion\iClone 3DXchange 7\Bin\iClone3DXchange.exe",
               "D:\VroidtoIclone\Shibu\shibu.fbx"])

    def update_character_iClone(self):
        self.update_character()

    def update_character(self):
        global avatar
        # avatar_list = RLPy.RScene.GetAvatars()
        # avatar = avatar_list[0]
        selection_list = RLPy.RScene.GetSelectedObjects()
        if len(selection_list) > 0:
            for object in selection_list:  # find first avatar
                # object_type = object.GetType()
                # if object_type == RLPy.EObjectType_Avatar:
                    avatar = object[0]

        if avatar is None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please click on an avatar")
            msgBox.exec()
            return

        # material_component = avatar.GetMaterialComponent()
        # mesh_list = avatar.GetMeshNames()
        # texture_channel = RLPy.EMaterialTextureChannel_Diffuse
        #
        # for mesh_name in mesh_list:
        #     # print(mesh_name)
        #     material_list = material_component.GetMaterialNames(mesh_name)
        #     for material in material_list:
        #         material_name = "_".join(material.split("_")[:-1])  # remove characters after last _
        #         print("   Material_name   " + material + "   Mesh_name  " + mesh_name)

    def show_dialog(self):
        self.transfer_vroid_character_dialog.Show()
x = App()
x.show_dialog()

# file ="F00_000_00_Face_00.png"
# image_file = "D:/VroidtoIclone/Shibu/tex_shibu_by_Dan/" + file
#
#
#
# print(image_file)
# print(mesh_name)
# print(material_name)
# print(texture_channel)
#
# result = material_component.LoadImageToTexture(mesh_name, "Std_Skin_Head", texture_channel, image_file)

# result = material_component.LoadImageToTexture("CC_Base_Body", "Std_Skin_Head", texture_channel, path)
# print(result.Success)