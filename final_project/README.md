This project is my attempt to reproduce my house.

Scripts:
apartment.js : contains the apartmentMeshInit function, that creates the apartment mesh reading the .obj and add the floor. Besides, it calls furnitureInit(), that places the furniture in the apartment and creates doors and windows.
map.js : contains the apartment map (a grid) for collision detection. It implements "only" hall collision detection.
intersectionHanler.js : it handles object collision (and Tween animations), such as doors and windows.

Htmls:
index.html : the apartment (with clouds and snow)
fp.html : explore the house via first person!

Techniques:
- bump/normal map
- raycaster
- pointerlock
- Tweens
- imported objs

Included:
python file for creating the house obj
