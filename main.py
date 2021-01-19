# PyCharm
import pydevd_pycharm

pydevd_pycharm.settrace('127.0.0.1', port=12345, stdoutToServer=False,
                        stderrToServer=False)
import RLPy
import PySide2
from PySide2 import *
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import QThread
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QWidget

from subprocess import Popen

avatar = None
Xchange_path = "D:\Program Files\Reallusion\iClone 3DXchange 7\Bin\iClone3DXchange.exe"


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
        self.info.setPlainText("Default path to 3DXchange  " + Xchange_path)

        self.path_3DXchange_button = QtWidgets.QPushButton("Set path to 3DXchange")
        self.path_3DXchange_button.clicked.connect(self.path_3dxchange)
        self.mocap_layout.addWidget(self.path_3DXchange_button)

        self.import_3DXchange_button = QtWidgets.QPushButton("Import fbx to 3DXchange")
        self.import_3DXchange_button.clicked.connect(self.import_3dxchange)
        self.mocap_layout.addWidget(self.import_3DXchange_button)

        self.update_character_iClone_button = QtWidgets.QPushButton("Update character in iClone")
        self.update_character_iClone_button.clicked.connect(self.update_character_iClone)
        self.mocap_layout.addWidget(self.update_character_iClone_button)

        return

    def path_3dxchange(self):
        global Xchange_path
        Xchange_path = RLPy.RUi.OpenFileDialog("File(*.*)")
        self.info.setPlainText(Xchange_path)

    def import_3dxchange(self):
        global Xchange_path
        file_path = RLPy.RUi.OpenFileDialog("File(*.*)")
        self.info.append(file_path)
        Popen([Xchange_path,
               file_path])

    def update_character_iClone(self):
        self.update_character()

    def update_character(self):
        global avatar
        selection_list = RLPy.RScene.GetSelectedObjects()
        if len(selection_list) > 0:
            for object in selection_list:  # find first avatar
                object_type = object.GetType()
                if object_type == RLPy.EObjectType_Avatar:
                    avatar = object

        if avatar is None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Please click on an avatar")
            msgBox.exec()
            return

        material_component = avatar.GetMaterialComponent()
        mesh_list = avatar.GetMeshNames()
        texture_channel = RLPy.EMaterialTextureChannel_Diffuse

        for mesh_name in mesh_list:
            # print(mesh_name)
            material_list = material_component.GetMaterialNames(mesh_name)
            for material in material_list:
                substring = "_HAIR"  # hair texture png has 01 and 02 plus HAIR
                if substring in material:
                    image_name = image_name.replace(substring, '')
                else:
                    image_name = "_".join(material.split("_")[:-1])  # remove characters after last _
                    print(
                        "   Material_name   " + material + "   Mesh_name  " + mesh_name + "   Image_name  " + image_name)

                image_file = "D:/VroidtoIclone/Shibu/tex_shibu_by_Dan/" + image_name + ".png"
                result = material_component.LoadImageToTexture(mesh_name, material, texture_channel, image_file)


    def show_dialog(self):
        self.transfer_vroid_character_dialog.Show()


x = App()
x.show_dialog()

#### Attempt to find Morph Creator button and push programatically ###
# main_widget = wrapInstance(int(RLPy.RUi.GetMainWindow()), QtWidgets.QWidget)
# lineEdits = form.findChildren(QtGui.QLineEdit)
# children = main_widget.findChildren(QtWidgets.QPushButton)
# children = main_widget.findChildren(QtWidgets.QTabWidget)
# print(children[0].objectName())
# print(children[0].text())
# for child in children:
#     objName = child.objectName()
#     self.info.append(objName)
#     objText = child.text()
#     self.info.append(objText)
