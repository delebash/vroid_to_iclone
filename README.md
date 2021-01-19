# vroid_to_iclone

Script to partiallly automate converting a vroid character to iClone character.


Most of this tutorial is from Freedom Arts https://www.youtube.com/watch?v=s3aJYZpLA6I

I have changed it to incorporate my script to automate some of the iClone and 3DXchange tasks in the awesome tutorial linked above by Freedom Arts

Requirements:

Blender 2.9

Addon https://github.com/saturday06/VRM_IMPORTER_for_Blender

3DXchange 7

iClone 7

**Install add-on**

1) Download zip file from here https://github.com/saturday06/VRM_IMPORTER_for_Blender. Click on green but and choose download zip.

2) Open Blender

3) Goto menu Edit > Preferences > Add-ons

4) Select testing tab

5) Click Install and select the zip folder for the add-on.  Do not extract the zip file.

6) Check the box that says Import.Export VRM_IMPORTER

7) Close add-on dialog

**Import your vrm file and export as fbx**

1) Go to menu File > Import > VRM (.vrm)

2) Select your vrm file and wait until you see your character in blender

3) Go to menu File > Export > FBX (.fbx)

**Import and configure your character for iClone**

1) Download automation script from https://github.com/delebash/vroid_to_iclone and extract it to whatever folder you want.  I would keep all the files under one folder Freedom Arts tutorial. 

2) Open iClone

3) Go to Menu > Script > Load Python. Select the main.py in the folder from step 1 of this section.

4) A dialog with the title Transfer Vroid Character

5) You will need to specify the path to your 3DXchange program.  The default location for 3DXchange is already set.  If you have a different location click Set path to 3DXchange and navigate to the exe.

6) Click Import fbx to 3DXchange.

7) Select ok at initial prompt

8) On the right panel click Apply to iClone

9) This will load the character into iClone

**Steps in iClone after character is loaded**

1) Under the Modify Panel select the Animation tab

2) Click Morph Creator

3) Morph Create will ask to create morphs for you click Ok.

4) In Morph Creator on the Morph Editor Panel click Update Morph to iClone

5) Close Morph Creator and go back to iClone 

6) From the Modify panel on the right select the Animation tab

7) Click on the button Edit in 3DXchange

**Modify character in 3DXchange**

1) Click Convert to Non-Standard from the Modify panel on the right.

2) A new window will open.  On the top right next to Characterization Profile click Load.  Navigate to my script folder and choose the Vrm_to_3DXchange._bone_map.3dxProfile.  The bones should now be mapped to your character.

3) Click the Convert button

4) Click the Apply to iClone button

5) The TempAvatar should be selected you can delete the original character

6) Click Select texture folder and update

7) Navigate to the texture folder created by the Blender export vrm.  This should be in the same place as your fbx file.

8) Delete the prop version of your character.  The one in white without any textures

9) Click the x on Transfer Vroid Charact to close the dialog.

10) You are done.

Note:  Animation will not work but morphs will as I have not added that to the Vrm_to_3DXchange._bone_map.3dxProfile yet.  Still some fine tuning.  You can watch Freedoms video he demonstrates how to setup animation in 3DXchange for your character.  You can make these changes in 3DXchange after you load Characterization File.  Any changes you make that work for you click Save next to the Characterization Profile.  You can save it as a new name and load this profile or you can just overwrite the existing profile file you loaded.

