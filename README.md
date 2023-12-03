# Mesh Utilities
A blender addon that adds a new menu - "Mesh Utilities"

---

### "Generate LODs"
Opens a popup menu, allowing you to:

> Change the mesh name (or use the current mesh name);

> Change the decimate index (how many times the mesh will be decimated/have an LOD produced);

> Change the decimate ratio (how severe the decimate modifier is);

Here! Lets use an example. I'll leave the mesh name, which uses the default. I'll also set the decimate index to 6, this is so we get 6 (Technically 5 due to the original mesh being preserved) LODs.

They will be decimated at a ratio of 0.5, which means each subsequent mesh will be half of the last.

**Before**
![image](https://github.com/SilenceIsFatto/Mesh-Utilities/assets/78276788/9a3996f9-8a65-4a8a-8c4e-8d9c4a6f3c90)

**After (LOD 0-5, Left to Right)**
![image](https://github.com/SilenceIsFatto/Mesh-Utilities/assets/78276788/ae62d836-5f40-4534-9a18-6635512eb20d)
***- Do note, I split the meshes myself and deleted the original mesh.***

---

### "Clear Mesh Normal Data"
Clears the mesh split normal data which is commonly already set when using models from a site like Sketchfab. This allows you to set the auto smoothing to your preferred amount.

---

### "Transfer Weights (Multiple Meshes)"
Transfers weights from 1 model to X amount of meshes. 

This is useful when, for example, trying to rig a uniform to a character and you need to transfer the characters weights to a vest, helmet, and uniform (as seperate meshes).

To use, select all the meshes that you want to transfer the weights to - and finally select the mesh that has the weights and click the button.
