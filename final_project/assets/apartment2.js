
function apartmentInit(lightsOn) {
      var apartment = apartmentMeshInit();
      apartment = furnitureInit(apartment, lightsOn);
      return apartment;
}


function apartmentMeshInit() {
      var apartment = new THREE.Object3D();

      var loader = new THREE.OBJLoader();
      loader.load('assets/models/casa.obj', function (obj) {

        global_o = obj;

        // var material = new THREE.MeshLambertMaterial({color: 0xaaaaaa});
        // material.side = THREE.DoubleSide;
        // obj.children[0].material = material;
        // mesh = obj.children[0];

        var multiMaterial = [
          new THREE.MeshLambertMaterial({color: 0xffffff, side: THREE.DoubleSide, shading: THREE.FlatShading}),
          new THREE.MeshBasicMaterial({wireframe: false, overdraw: true, color: 0xffffff, side: THREE.DoubleSide})
          ];

        mesh = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, multiMaterial);

        apartment.add(mesh);
        console.log(apartment)

        //scene.add(apartment);
      });

      // ground
/*
      var initColor = new THREE.Color( 0x497f13 );
      var initTexture = THREE.ImageUtils.generateDataTexture( 1, 1, initColor );

      var groundMaterial = new THREE.MeshPhongMaterial( { color: 0xffffff, specular: 0x111111, map: initTexture } );

      var groundTexture = THREE.ImageUtils.loadTexture( "assets/textures/general/grasslight-big.jpg", undefined, function() { groundMaterial.map = groundTexture } );
      groundTexture.wrapS = groundTexture.wrapT = THREE.RepeatWrapping;
      groundTexture.repeat.set( 25, 25 );
      groundTexture.anisotropy = 16;

      var mesh = new THREE.Mesh( new THREE.PlaneGeometry( 20000, 20000 ), groundMaterial );
      //mesh.position.y = -250;
      mesh.rotation.x = - Math.PI / 2;
      mesh.receiveShadow = true;
      apartment.add( mesh );*/

      //Grass
      var floorTex = THREE.ImageUtils.loadTexture("assets/textures/general/grass2.jpg");
      floorTex.wrapS = THREE.RepeatWrapping;
      floorTex.wrapT = THREE.RepeatWrapping;
      floorTex.repeat.x = 400 / 16;
      floorTex.repeat.y = 400 / 16;
      var plane = new THREE.Mesh(
        new THREE.CubeGeometry(600, 600, 0.1, 30), 
        new THREE.MeshPhongMaterial({map: floorTex})
      );
      //plane.rotation.x = -0.5 * Math.PI;
      apartment.add(plane);

      //scene.add(plane);


      /*FLOORS*/
      var hallFloor = createMesh(new THREE.PlaneGeometry( 8.3, 10.2, 20, 20 ), "parquet.jpg", "prova3.jpg");
      //var hallFloor = createMesh(new THREE.PlaneGeometry( 8.3, 10.2, 20, 20 ), "Natural Anagre_DIFFUSE.jpg", "Natural Anagre_NORMAL.jpg");
      hallFloor.position.x = (2.6+8.3/2);
      hallFloor.position.y = (0.3+10.2/2);
      hallFloor.position.z = 0.4;
      apartment.add(hallFloor);

      var kitchenFloor = createMesh(new THREE.PlaneGeometry( 5.1, 5, 20, 20 ), "marble.jpg");
      kitchenFloor.position.x = (hallFloor.position.x + 8.3/2 + 0.1 + 5.1/2);
      kitchenFloor.position.y = (0.3 + 5/2);
      kitchenFloor.position.z = 0.4;
      apartment.add(kitchenFloor);

      var balconyFloor = createMesh(new THREE.PlaneGeometry( 2, 10.2, 20, 20 ), "15_DIFFUSE.jpg", "15_NORMAL.jpg" );
      balconyFloor.position.x = (0.3 + 2/2);
      balconyFloor.position.y = (0.3 + 10.2/2);
      balconyFloor.position.z = 0.4;
      apartment.add(balconyFloor);

      var balconyFloor2 = balconyFloor.clone();
      balconyFloor.position.x = (kitchenFloor.position.x + 5.1/2 + 0.3 + 2/2);
      apartment.add(balconyFloor2);

      var rightRoomFloor = createMesh(new THREE.PlaneGeometry( 5.1, 5.1, 20, 20 ), "marble.jpg");
      rightRoomFloor.position.x = (hallFloor.position.x + 8.3/2 + 0.1 + 5.1/2);
      rightRoomFloor.position.y = (kitchenFloor.position.y + 5/2 + 0.1 + 5.1/2);
      rightRoomFloor.position.z = 0.4;
      apartment.add(rightRoomFloor);

      var leftRoomFloor =  createMesh(new THREE.PlaneGeometry( 4, 5.1, 20, 20 ), "Natural Anagre_DIFFUSE.jpg", "Natural Anagre_NORMAL.jpg");
      leftRoomFloor.position.x = (2.6 + 4/2);
      leftRoomFloor.position.y = (balconyFloor.position.y + 10.2/2 + 0.3 + 5.1/2);
      leftRoomFloor.position.z = 0.4;
      apartment.add(leftRoomFloor);

      var bathroomFloor = createMesh(new THREE.PlaneGeometry( 4, 3, 20, 20 ), "bathroom.jpg", "bathroom-normal.jpg");
      bathroomFloor.position.x = (leftRoomFloor.position.x + 4/2 + 0.3 + 4/2);
      bathroomFloor.position.y = (balconyFloor.position.y + 10.2/2 + 0.3 + 2 + 3.1/2);
      bathroomFloor.position.z = 0.4;
      apartment.add(bathroomFloor);

      var corridorFloor = createMesh(new THREE.PlaneGeometry( 7.1, 2, 20, 20 ), "Natural Anagre_DIFFUSE.jpg", "Natural Anagre_NORMAL.jpg");
      corridorFloor.position.x = (leftRoomFloor.position.x + 4/2 + 0.3 + 7.1/2);
      corridorFloor.position.y = (hallFloor.position.y + 10.2/2 + 0.3 + 2/2);
      corridorFloor.position.z = 0.4;
      apartment.add(corridorFloor);

      var upperRoomFloor1 = createMesh(new THREE.PlaneGeometry( 5.1, 3, 20, 20 ), "Natural Anagre_DIFFUSE.jpg", "Natural Anagre_NORMAL.jpg");
      upperRoomFloor1.position.x = (rightRoomFloor.position.x);
      upperRoomFloor1.position.y = (bathroomFloor.position.y);
      upperRoomFloor1.position.z = 0.4;
      apartment.add(upperRoomFloor1);

      var upperRoomFloor2 = createMesh(new THREE.PlaneGeometry( 2, 2.1, 20, 20 ), "Natural Anagre_DIFFUSE.jpg", "Natural Anagre_NORMAL.jpg");
      upperRoomFloor2.position.x = (14.1+2/2);
      upperRoomFloor2.position.y = (corridorFloor.position.y);
      upperRoomFloor2.position.z = 0.4;
      apartment.add(upperRoomFloor2);

      /*WALLS*/
      //Hall South walls
      /*var lenX = 5.9;
      var hallWall = createMesh(new THREE.CubeGeometry( lenX, 2.7, 0.01), "stone.jpg");
      hallWall.position.x = (2.6+lenX/2);
      hallWall.position.y = (0.3);
      hallWall.position.z = 0.3+2.7/2;
      hallWall.rotation.x = 0.5 * Math.PI;
      //scene.add(hallWall);

      var kitchLenX = 5.1;
      lenX = 1.45+kitchLenX;
      var hallWall2 = createMesh(new THREE.CubeGeometry( lenX, 2.7, 0.01), "stone.jpg");
      hallWall2.position.x = (2.6+5.9+1.08+lenX/2);
      hallWall2.position.y = (0.3);
      hallWall2.position.z = 0.3+2.7/2;
      hallWall2.rotation.x = 0.5 * Math.PI;
      //scene.add(hallWall2);

      lenX = 1.08;
      var lenZ = 0.4; 
      var hallWall3 = createMesh(new THREE.CubeGeometry( lenX, lenZ, 0.01), "stone.jpg");
      hallWall3.position.x = (2.6+5.9+lenX/2);0
      hallWall3.position.y = (0.3);
      hallWall3.position.z = 0.3+2.3+lenZ/2;
      hallWall3.rotation.x = 0.5 * Math.PI;
      //scene.add(hallWall3);*/


      /*WALLS*/
      //Hall South walls
      var options = {
        amount: 0,
        bevelThickness: 0,
        bevelSize: 0,
        bevelSegments: 0,
        bevelEnabled: 0,
        curveSegments: 0,
        steps: 0
      };

      //Hall south wall
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("hall"), options), "stone.jpg");
      var shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = Math.PI;
      shape.position.x = 2.6 + shapeLength;
      shape.position.y = 0.31;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Hall west hall
      var hallY = 10.2; //hall Y length 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("hallSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      shape.position.x = 2.6+0.01;
      shape.position.y = 0.3;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Hall north wall
      var hallY = 10.2; //hall Y length 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("hall"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = Math.PI;
      shape.position.x = 2.6 + shapeLength;
      shape.position.y = 0.29 + hallY;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Hall East wall
      var hallY = 10.2; //hall Y length 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("hallDx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 8.3+2.599;
      shape.position.y = 0.3+10.2;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Kitchen west wall 
      var hallY = 10.2; //hall Y length 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("kitchenSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.3+5.0;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Kitchen east wall 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("kitchenSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1+5.089;
      shape.position.y = 0.3+5.0;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape); 

      //Kitchen North wall
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 0.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.299+5.0;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);      

      //Kitchen South wall
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 0.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.31;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);  


      //Right Room South wall
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 0.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.301+5.0+0.1;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape); 

      //Right room west
      var hallY = 10.2; //hall Y length 
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomSx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.3+10.2;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Right room east
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomDx"), options), "stone.jpg");
      shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1+5.089;
      shape.position.y = 0.3+10.2;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Right room north
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomNth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 2*Math.PI;
      shape.position.x = 8.3+2.61+0.1;
      shape.position.y = 0.301+5.0+0.1+5.09;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Left room south
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Left room east
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomDx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      shape.position.x = 2.6+4-0.01;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.1;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Left room west
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      shape.position.x = 2.6+0.01;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Left room north
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);



      //Bathroom north
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Bathroom west
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("bath"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.301;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Bathroom east
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("bath"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+3.99;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Bathroom south
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("bathSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3;
      shape.position.y = 0.3+10.2+0.3+2+0.01+0.1;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);


      //Upper room north
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("rRoomSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+4+0.1;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Upper room south
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("uppRoomSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+4+0.1;
      shape.position.y = 0.3+10.2+0.3+2+0.01+0.1;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Upper room south2
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("uppRoomSth2"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+4+0.1+3.1;
      shape.position.y = 0.3+10.2+0.3+0.01;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Upper room west
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("bath"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+4+0.101;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32+5.08;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Upper room west 2
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("uppRoomSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+0.01+7.1+0.1;
      shape.position.y = 0.3+10.2+0.3;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Upper room east
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("lRoomSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      shape.position.x = 8.3+2.61+0.1+5.089;
      shape.position.y = 0.301+5.0+0.1+5.09+0.32;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Corridor north
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("corridorNth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3;
      shape.position.y = 0.3+10.2+0.3+1.99;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Corridor south
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("corridorSth"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      //shape.rotation.y = 1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3;
      shape.position.y = 0.3+10.2+0.3+0.01;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Corridor west
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("corridorSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3+0.01;
      shape.position.y = 0.3+10.2+0.3+0.01;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);

      //Corridor east
      var shape = createMesh(new THREE.ExtrudeGeometry(drawShapeHall("corridorSx"), options), "stone.jpg");
      //shapeLength = 8.3;
      shape.rotation.x = 0.5 * Math.PI;
      shape.rotation.y = -1.5*Math.PI;
      //shape.rotation.y = 2*Math.PI;
      shape.position.x = 2.6+4+0.3-0.01+7.1;
      shape.position.y = 0.3+10.2+0.3;
      shape.position.z = 0.3;
      shape.scale.set(10,10,10);
      apartment.add(shape);


      apartment.rotation.x = -0.5 * Math.PI;
      apartment.scale.set(10, 10, 7);

      return apartment;
}
      //apartment.rotation.z = -0.25*Math.PI;



function furnitureInit(apartment, lightsOn) {

      // addHallFurniture(apartment);
      // addKitchenFurniture(apartment);
      // addBathroomFurniture(apartment);
      // addLeftRoomFurniture(apartment);
      // addLights(apartment, lightsOn);
      // addRightRoomFurniture(apartment);
      // addUpperRoomFurniture(apartment);
      addGarden(apartment);
      return apartment;
}

function addGarden(apartment) {
      loadFurniture('blackTupelo', apartment, 13, -2, 0, 0.5 * Math.PI, 0, 0, 1/3, 1/3, 1/3);
      loadFurniture('bench', apartment, 10.5, -2, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/2, 1/2, 1/2);
      loadFurniture('mofx_mailbox', apartment, 8, -1, 0, 0.5 * Math.PI, 0, 0, 1/80, 1/80, 1/80);


}

function addUpperRoomFurniture(apartment) {
      loadFurniture('radiator_7section', apartment, 16, 12, 0.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('lettoCiliegio', apartment, 10.2, 16.5, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/100, 1/90, 1/80);
      loadFurniture('mobileCiliegio', apartment, 14, 15.2, 0.4, 0.5 * Math.PI, 0, 0, 1/100, 1/98, 1/80);
      loadFurniture('sneakers', apartment, 14, 14.2, 0.4, 0.5 * Math.PI, 0, 0, 1/100, 1/98, 1/80);

}


function addRightRoomFurniture(apartment) {
      loadFurniture('radiator_7section', apartment, 16, 8.75, 0.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('bedWithTexture', apartment, 14, 6.8, 0.4, 0.5 * Math.PI, -Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('desk', apartment, 15, 10.2, 0.3, 0.5 * Math.PI, 0, 0, 1/4, 1/4, 1/4);
      loadFurniture('oakChair', apartment, 15, 9.5, 0.4, 0.5 * Math.PI, -Math.PI, 0, 1/100, 1/110, 1/100);
      loadFurniture('wardrobeWithSlidingDoors', apartment, 11.8, 6.8, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/90, 1/95, 1/80);
}

function addLights(apartment, turnedOn) {

      apartment.hallLight1 = createLight(apartment, 10, 5, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.hallLight2 = createLight(apartment, 4, 5, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      /*apartment.kitLight = createLight(apartment, 13.5, 3, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.LRLight = createLight(apartment, 5, 13, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.BathLight = createLight(apartment, 9, 14, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.RRLight = createLight(apartment, 13.5, 8, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.URLight = createLight(apartment, 13.5, 14, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.CLight1 = createLight(apartment, 9, 12, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);
      apartment.CLight2 = createLight(apartment, 12, 12, 2.7, 0.5*Math.PI, 0, 0, 1/20, 1/20, 1/20);*/
}


function addDoors(scene,list) {
      
      scene.jointKitchen = createDoor(scene,list, 'wood-2.jpg', 109.5, 10.5, -43, 1.12, 0.1, 1.6, 0.5*Math.PI, 0, 0.5*Math.PI, 10, 10, 10);
      scene.jointHall = createDoor(scene,list, 'wood-2.jpg', 85, 10.5, -106.5, 1.1, 0.1, 1.6, 0.5*Math.PI, 0, 0, 10, 10, 10);
      scene.jointBath = createDoor(scene,list, 'wood-2.jpg', 85, 10.5, -128.5, 1.1, 0.1, 1.6, 0.5*Math.PI, 0, 0, 10, 10, 10);
      scene.jointRRoom = createDoor(scene,list, 'wood-2.jpg', 124, 10.5, -106.5, 1.1, 0.1, 1.6, 0.5*Math.PI, 0, 0, 10, 10, 10);
      scene.jointLRoom = createDoor(scene,list, 'wood-2.jpg', 67.5, 10.5, -123, 1.12, 0.1, 1.6, 0.5*Math.PI, 0, 0.5*Math.PI, 10, 10, 10);
      scene.jointUppRoom = createDoor(scene,list, 'wood-2.jpg', 140.5, 10.5, -123, 1.12, 0.1, 1.6, 0.5*Math.PI, 0, 0.5*Math.PI, 10, 10, 10);
      scene.jointWinKit = createWinDoor(scene,list, 'wood-2.jpg', 162, 2, -32.6, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 10, 16, 20);
      scene.jointWinHall1 = createWinDoor(scene,list, 'wood-2.jpg', 23.9, 2.1, -79.8, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 7.3, 16, 20);
      scene.jointWinHall2 = createWinDoor(scene,list, 'wood-2.jpg', 23.8, 2.1, -94.85, 1.12, 0.1, 1.6, 0, -0.5*Math.PI, 0, 7.3, 16, 20);
      scene.jointWindowHall1 = createWinDoor(scene,list, 'wood-2.jpg', 23.8, 11.7, -4.9, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 17.8, 7.5, 20);
      scene.jointWindowHall2 = createWinDoor(scene,list, 'wood-2.jpg', 23.7, 11.7, -40.5, 1.12, 0.1, 1.6, 0, -0.5*Math.PI, 0, 17.8, 7.5, 20);
      scene.jointWindowLR1 = createWinDoor(scene,list, 'wood-2.jpg', 23.8, 11.7, -136.5, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 7.3, 8, 20);
      scene.jointWindowLR2 = createWinDoor(scene,list, 'wood-2.jpg', 23.7, 11.7, -151.5, 1.12, 0.1, 1.6, 0, -0.5*Math.PI, 0, 7.3, 8, 20);
      scene.jointWindowUR1 = createWinDoor(scene,list, 'wood-2.jpg', 162.1, 11.7, -136.5, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 7.3, 8, 20);
      scene.jointWindowUR2 = createWinDoor(scene,list, 'wood-2.jpg', 162, 11.7, -151.5, 1.12, 0.1, 1.6, 0, -0.5*Math.PI, 0, 7.3, 8, 20);
      scene.jointWinRRoom = createWinDoor(scene,list, 'wood-2.jpg', 162, 2, -58.9, 1.12, 0.1, 1.6, 0, 0.5*Math.PI, 0, 10, 16, 20);
      scene.jointMain = createDoor(scene,list, 'wood-2.jpg', 85, 10.5, -1.5, 1.1, 0.1, 1.6, 0.5*Math.PI, 0, 0, 10, 10, 10);

}

function addSwitch(scene, list) {
      scene.hallSwitch = createSwitch(scene, list, 80, 10, -3.2, 0 , Math.PI, 0, 1, 1, 1);
      scene.kitSwitch = createSwitch(scene, list, 110.28, 10, -31, 0 , 0.5*Math.PI, 0, 1, 1, 1);
}

function createLight(apartment, x, y, z, rX, rY, rZ, sX, sY, sZ) {
      var shadeGeometry = new THREE.SphereGeometry( 3, 80, 80, 0, Math.PI * 2, 0, Math.PI / 2 );
      var shadeMaterial = new THREE.MeshPhongMaterial( {color : 0xdadada, side : THREE.DoubleSide} );
      var shade = new THREE.Mesh(shadeGeometry, shadeMaterial);
      shade.castShadow = true;
      //shade.rotation.x = - 1 * Math.PI;

      //Bulb filament
      var bulbFilamentGeometry = new THREE.TorusGeometry( 0.4, 0.1); 
      var bulbFilamentMaterial = new THREE.MeshPhongMaterial( {color: 0xff0000} ); 
      var bulbFilament = new THREE.Mesh(bulbFilamentGeometry, bulbFilamentMaterial);
      bulbFilament.position.set(shade.position.x, shade.position.y, shade.position.z);
      //scene.add(bulbFilament);

      //Bulb
      var bulbGeometry = new THREE.SphereGeometry( 1, 20, 20 );
      var bulbMaterial = new THREE.MeshBasicMaterial( {transparent : true, opacity : 0.6} );
      var bulb = new THREE.Mesh(bulbGeometry, bulbMaterial);
      bulb.castShadow = true;

      shade.add(bulbFilament);
      shade.bulbFilament = bulbFilament;
      bulbFilament.add(bulb);
      bulbFilament.bulb = bulb;

      //SpotLight
      var spotLight = new THREE.SpotLight(0xffffff);
      spotLight.position.set( x, y, z );

      var target = new THREE.Object3D();
      target.position.set(x-2,y-16,0);
      shade.add(target);
      

      //spotLight.rotation.x =  -1 * Math.PI/2;
      spotLight.target = target;
      var spotLightHelper = new THREE.SpotLightHelper(spotLight, 3);
      //apartment.add(spotLightHelper)
      
      bulb.add(spotLight);
      bulb.spotLight = spotLight;
      spotLight.castShadow = true;
      spotLight.shadowMapWidth = 4096; 
      spotLight.shadowMapHeight = 4096; 
      spotLight.shadowCameraNear = 1; 
      spotLight.shadowCameraFar = 4000; 
      spotLight.shadowCameraFov = 30;
      spotLight.intensity = 2;

      //Bulb PointLight
      var bulbPointLightColor = "#ffff7f"
      var bulbPointLight = new THREE.PointLight(bulbPointLightColor, 0.8, 10);
      //bulb.add(bulbPointLight);
      bulb.pointLight = bulbPointLight;


      var target = new THREE.Object3D();
      target.position = new THREE.Vector3( bulb.position.x, bulb.position.y, 30);

      shade.rotation.x = rX;
      shade.rotation.y = rY;
      shade.rotation.z = rZ;
      shade.position.set(x, y, z);
      shade.scale.set(sX, sY, sZ);

      shade.light = spotLight;

      apartment.add(shade);
      return shade;
}


function createSwitch(scene, list, x, y, z, rX, rY, rZ, sX, sY, sZ) {
      //var lightSwitch = loadFurnitureNoMTL(url, scene, x, y, z, rX, rY, rZ, sX, sY, sZ );
      var lightSwitchGeom = new THREE.CubeGeometry( 1, 1, 0.1 );
      var lightSwitchMat = new THREE.MeshPhongMaterial( {color: 0xffffff} );
      var lightSwitch = new THREE.Mesh(lightSwitchGeom, lightSwitchMat);

      var switchGeom = new THREE.CubeGeometry( 0.1, 0.1, 0.2);
      var switchMat = new THREE.MeshPhongMaterial( {color: 0x000000} );
      var switchL = new THREE.Mesh(switchGeom, switchMat);

      lightSwitch.add(switchL);

      lightSwitch.rotation.x = rX;
      lightSwitch.rotation.y = rY;
      lightSwitch.rotation.z = rZ;
      lightSwitch.position.set(x, y, z);
      lightSwitch.scale.set(sX, sY, sZ);

      scene.add(lightSwitch);
      list.push(lightSwitch);
      return lightSwitch; 
}


function createDoor(scene, list, url, x, y, z, lenX, lenY, lenZ, rX, rY, rZ, sX, sY, sZ) {
      var door = createMesh(new THREE.CubeGeometry( lenX, lenY, lenZ ), url);
      door.name = "door";
      //var joint = new THREE.Object3D();
      var cub = new THREE.CubeGeometry(1, 1, 1);
      var cubM = new THREE.MeshLambertMaterial( {color: 0xffffff} );
      //joint = new THREE.Mesh(cub, cubM);
      joint = new THREE.Object3D();
      joint.name = "joint";
      joint.position.set(x, y, z);
      if(rZ == 0.5*Math.PI)
            door.position.set(0,0,lenZ*2+2);
      else
            door.position.set(lenX*2+3,0,0);
      //door.scale.set(sX, sY, sZ);
      //handle base
      var handleBaseGeom = new THREE.CylinderGeometry( 0.03, 0.03, 0.2, 10, 10, false );
      var handleBaseMat = new THREE.MeshPhongMaterial( {color : 0xffffff} );
      var handleBase = new THREE.Mesh(handleBaseGeom, handleBaseMat);
      door.add(handleBase);
      handleBase.position.set(0.3, 0, 0);
      door.handle = handleBase;
      //handle 1
      var handleGeom = new THREE.CylinderGeometry( 1/50, 1/50, 0.08, 10, 10, false );
      var handleMat = new THREE.MeshPhongMaterial( {color : 0xffffff} );
      var handle1 = new THREE.Mesh(handleBaseGeom, handleBaseMat);
      handle1.rotation.z = -0.5*Math.PI;
      handleBase.add(handle1);
      handle1.position.set(-0.075, 0.1, 0)
      handleBase.handle1 = handle1;
      //handle 2
      var handle2 = new THREE.Mesh(handleBaseGeom, handleBaseMat);
      handle2.rotation.z = -0.5*Math.PI;
      handleBase.add(handle2);
      handle2.position.set(-0.075, -0.1, 0)
      handleBase.handle2 = handle2;

      door.rotation.x = rX;
      door.rotation.y = rY;
      door.rotation.z = rZ;
      door.scale.set(sX, sY, sZ);
      joint.add(door);
      joint.door = door;
      scene.add(joint);
      list.push(door);
      return joint;

}

function createWinDoor(scene, list, url, x, y, z, lenX, lenY, lenZ, rX, rY, rZ, sX, sY, sZ) {
      var shape = new THREE.Shape();
      shape.moveTo(0, 0);
      shape.lineTo(1, 0);
      shape.lineTo(1, 1);
      shape.lineTo(0, 1);
      shape.lineTo(0, 0);
      //Window
      var hole = new THREE.Path( [new THREE.Vector2( 0.1, 0.1 ), new THREE.Vector2( 0.9, 0.1 ),
                                    new THREE.Vector2( 0.9, 0.9 ), new THREE.Vector2( 0.1, 0.9 )]);
      shape.holes.push(hole);
      var options = {
              amount: 100,
              bevelThickness: 0,
              bevelSize: 0,
              bevelSegments: 0,
              bevelEnabled: false,
              curveSegments: 0,
              steps: 0
            };
      var windoor = createMesh(new THREE.ExtrudeGeometry(shape, {amount:1/20, bevelEnabled: false}), url);

      //var windoor = new THREE.Mesh(geometry, material);
      //windoor.position.set(x, y, z);
      windoor.scale.set(sX, sY, sZ);
      windoor.rotation.x = rX;
      windoor.rotation.y = rY;
      windoor.rotation.z = rZ;
      var glassGeom = new THREE.CubeGeometry( 0.8, 0.8, 0.01);
      var glassMat = new THREE.MeshLambertMaterial( {color: 0xd1eeee,transparent: true, opacity: 0.5} );
      var glass = new THREE.Mesh(glassGeom, glassMat);

      glass.rotation.x = rX;
      glass.rotation.z = rY;
      glass.rotation.y = rZ;
      windoor.add(glass);
      glass.position.set(0.5,0.5,0.01);

      var glass2 = new THREE.Mesh(glassGeom, glassMat);
      glass2.rotation.x = rX;
      glass2.rotation.z = rY;
      glass2.rotation.y = rZ;
      windoor.add(glass2);
      glass2.position.set(0.5,0.5,0.04);

/*      var cub = new THREE.CubeGeometry(1, 1, 1);
      var cubM = new THREE.MeshLambertMaterial( {color: 0x000000} );
      joint = new THREE.Mesh(cub, cubM);*/
      joint = new THREE.Object3D();
      joint.name = "joint";
      joint.position.set(x, y, z);
      if(rY == 0.5*Math.PI)
            windoor.position.set(0,0,lenY*2-0.5);
      else
            windoor.position.set(lenX,0,0);
      //door.scale.set(sX, sY, sZ);
      // windoor.rotation.x = rX;
      // windoor.rotation.y = rY;
      // windoor.rotation.z = rZ;
      // windoor.scale.set(sX, sY, sZ);
      joint.add(windoor);
      joint.windoor = windoor;
      scene.add(joint);
      list.push(windoor);
      return joint;

}

// function loadDoor(url, apartment, x, y, z, rX, rY, rZ, sX, sY, sZ) {
//             var loader = new THREE.OBJMTLLoader();
//             loader.addEventListener('load', function (event) {

//               object = event.content;

//               var door = new THREE.Object3D();
//               door.add(object.children[2]);
//               door.name = "door";
              

//               //mesh = object;
//               object.position.set(x,y,z);
//               object.scale.set(sX, sY, sZ);
//               object.rotation.x = rX;
//               object.rotation.y = rY;
//               object.rotation.z = rZ;
//               object.name = "door";
//               door.position.set(x,y,z);
//               door.scale.set(sX, sY, sZ);
//               door.rotation.x = rX;
//               door.rotation.y = rY;
//               door.rotation.z = rZ;
//               //object.name = "door";
//               apartment.add(object);

//               apartment.add(door);
//               return door;
//             });

//             var baseUrl = 'assets/models/';
//             loader.load(
//               baseUrl + url + '.obj', 
//               baseUrl + url + '.mtl', 
//               {side: THREE.DoubleSide}
//             );
            
// }



function addLeftRoomFurniture(apartment) {
      loadFurniture('radiator_7section', apartment, 2.73, 12.5, 0.5, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('kids_desk_table', apartment, 3.5, 11.9, 1.1, 0.5 * Math.PI, Math.PI, 0, 1/55, 1/70, 1/80);
      loadFurniture('officeChair', apartment, -1.65, 15, 2.15, 0.5 * Math.PI,0, 0, 1/65, 1/70, 1/80);
      loadFurniture('full-bookcase', apartment, 3.4, 15.75, 1.3, 0.5 * Math.PI,0, 0, 1/65, 1/80, 1/80);
      loadFurniture('juniorBed', apartment, 5.75, 14.6, 0.4, 0.5 * Math.PI, 0, 0, 1/80, 1/90, 1/80);
      loadFurniture('kleed_grieks', apartment, 3.75, 13, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/90, 1/110);
      loadFurniture('bedsideTable', apartment, 4.9, 15.7, 0.4, 0.5 * Math.PI, 0, 0, 1/80, 1/90, 1/110);
      loadFurniture('wardrobe', apartment, 5.75, 10.8, 0.41, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/90, 1/110);
      loadFurniture('deskLamp1', apartment, 4.7, 15.9, 0.92, 0.5 * Math.PI, 0, 0, 1/90, 1/90, 1/110);
      loadFurniture('livreAvecReliure', apartment, 4.7, 15.6, 0.96, 0.5 * Math.PI, 0, 0, 1/90, 1/90, 1/110);


}


function addHallFurniture(apartment) {
      loadFurniture('cornerSofa', apartment, 7.5, 5, 0.3, 0.5 * Math.PI, 1 * Math.PI, 0, 1/80, 1/80, 1/50);
      loadFurniture('contemp_living_room', apartment, 5.5, 10.5, 0.35, 0.5 * Math.PI, 0, 0, 1/80, 1/80, 1/50);
      loadFurniture('piano', apartment, 7, 0.6, 1.1, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('glass-dining-table', apartment, 5.5, 3, 0.88, 0.5 * Math.PI, Math.PI, 0, 1/5, 1/5, 1/5);
      loadFurniture('cafe_set_tonon_chair', apartment, 5.5, 2.5, 0.36, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('cafe_set_tonon_chair', apartment, 5.5, 3.5, 0.36, 0.5 * Math.PI, 0, 0, 1/80, 1/80, 1/70);
      loadFurniture('cafe_set_tonon_chair', apartment, 4, 3, 0.36, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('cafe_set_tonon_chair', apartment, 7, 3, 0.36, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('ficus', apartment, 3.2, 1, 0.36, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/60, 1/60, 1/60);
      loadFurniture('kitchenUpperCabinet', apartment, 5, 0.7, -1.3, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('internal-unity-air-conditioning', apartment, 2.7, 6, 2.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('picture', apartment, 8.7, 6.8, 1.3, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('saloon_table', apartment, 3.5, 6.8, 0.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1, 1, 1);
      loadFurniture('dining_room', apartment, 10.6, 6.8, 0.5, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/80, 1/90, 1/80);
      loadFurniture('radiator_7section', apartment, 10.75, 1.25, 0.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('TucanFrame', apartment, 10.88, 1.5, 2, 0.5 * Math.PI, -0.5 * Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('TucanFrame', apartment, 10.88, 9.5, 2, 0.5 * Math.PI, -0.5 * Math.PI, 0, 1/70, 1/80, 1/60);
      loadFurnitureNoMTL('rideau', apartment, 2.8, 4, 3, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/10, 1/10, 1/6);
      loadFurnitureNoMTL('tringleRideau', apartment, 2.65, 2.5, 2.9, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/1.5, 1/10, 1/6);
      loadFurniture('livres', apartment, 10.6, 6.8, 1.55, 0.5 * Math.PI, -0.5 * Math.PI, 0, 1/70, 1/80, 1/60);
      loadFurniture('livingroom_lamp1', apartment, 10.6, 6.4, 1.4, 0.5 * Math.PI, -0.5 * Math.PI, 0, 1/70, 1/80, 1/60);
      loadFurniture('flowers', apartment, 8.5, 4.5, 1.7, 0.5 * Math.PI, -0.5 * Math.PI, 0, 1/70, 1/90, 1/60);
      loadFurniture('livres', apartment, 10.6, 6.85, 1.55, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4, 10, 2.4, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4.5, 10, 2.4, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4, 10, 1.85, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4.5, 10, 1.85, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4, 10, 1.38, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('livres', apartment, 4.5, 10, 1.38, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/60);
      loadFurniture('deer', apartment, 3.8, 10, 1.2, 0.5 * Math.PI, 0, 0, 1/70, 1/40, 1/60);
      loadFurnitureNoMTL('p40', apartment, 3.8, 10, 1.77, 0, 0, 0, 1/50, 1/40, 1/60);
      loadFurnitureNoMTL('bougeoir', apartment, 7, 10, 1.95, 0.5 * Math.PI, 0, 0, 1/5, 1/4, 1/6);

}


function addKitchenFurniture(apartment) {
      loadFurniture('white_kitchen_table', apartment, 13.5, 3, 0.3, 0.5 * Math.PI, 0, 0, 1/80, 1/80, 1/50);
      loadFurniture('chairWithCushion', apartment, 13.5, 1.5, 0.3, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/100);
      loadFurniture('chairWithCushion', apartment, 13.5, 4.5, 0.3, 0.5 * Math.PI, 0, 0, 1/80, 1/80, 1/100);
      loadFurniture('chairWithCushion', apartment, 12, 3, 0.3, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/80, 1/100);
      loadFurniture('chairWithCushion', apartment, 15, 3, 0.3, 0.5 * Math.PI, 1.5*Math.PI, 0, 1/80, 1/80, 1/100);
      loadFurniture('cucina', apartment, 15, 1.3, 0.4, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('lavello', apartment, 15, 3.3, 0.4, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('cassettiera', apartment, 13.8, -1.41, 0.4, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/70);
      loadFurniture('mobilettoGrande', apartment, 13.8, -9, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/70, 1/70);
      loadFurniture('dishwasher', apartment, 13.1, 0.8, 0.8, 0.5 * Math.PI, Math.PI, 0, 1/7, 1/6.5, 1/7);
      loadFurniture('frigorifero_Scene', apartment, 15.8, 2.8, 2.3, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/2.5, 1/3, 1/2);
      loadFurniture('hood', apartment, 13.58, 1.3, 0.5, 0.5 * Math.PI, Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('radiator_7section', apartment, 16, 4.75, 0.5, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/95, 1/90, 1/80);
      loadFurniture('doppio', apartment, 9, 2.8, 0.4, 0.5 * Math.PI, 0, 0, 1/50, 1/90, 1/80);
      loadFurniture('spatifilum', apartment, 11.7, 4.8, 0.5, 0.5 * Math.PI, 0, 0, 1/80, 1/90, 1/80);
      loadFurniture('monitorLCD', apartment, 13.2, 4, 1.85, 0.5 * Math.PI, 0, 0, 1, 1, 1);
}

function addBathroomFurniture(apartment) {
      loadFurniture('bidet', apartment, 8.5, 15.3, 0.3, 0.5 * Math.PI, 0, 0, 1/70, 1/80, 1/50);
      loadFurniture('water', apartment, 8.75, 15.3, 0.3, 0.5 * Math.PI, 0, 0, 1/70, 1/60, 1/50);
      loadFurniture('doccia', apartment, 10.9, 10.1, 0.4, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/70, 1/80, 1/50);
      loadFurniture('clothes_washing_machine', apartment, 10.5, 13.3, 0.9, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/80, 1/80, 1/80);
      loadFurniture('com_bath3_toalla', apartment, 10.5, 13.6, 1.42, 0.5 * Math.PI, -0.5*Math.PI, 0, 1/50, 1/50, 1/50);
      loadFurniture('radiator_7section', apartment, 7.8, 13.05, 0.5, 0.5 * Math.PI, 0, 0, 1/95, 1/90, 1/80);
      loadFurniture('shower', apartment, 10.5, 15.87, 0.5, 0.5 * Math.PI, 0, 0, 1/95, 1/90, 1/80);
      loadFurniture('towel3', apartment, 7.3, 15.87, 0.5, 0.5 * Math.PI, 0, 0, 1/95, 1/90, 1/80);
      loadFurniture('towel3', apartment, 6.9, 15.5, 1, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/90, 1/80);
      loadFurniture('toiletPaperDispenser', apartment, 8.2, 15.87, 1.1, 0.5 * Math.PI, 0, 0, 1/95, 1/90, 1/80);
      loadFurniture('washbasin', apartment, 6.9, 14, 0.3, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/60, 1/80);
      loadFurniture('mirror', apartment, 6.9, 14, 2, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/60, 1/80);
      loadFurniture('potBrossesADent', apartment, 6.965, 14.155, 1.6, 0.5 * Math.PI, 0.5*Math.PI, 0, 1/80, 1/60, 1/80);
      loadFurniture('savon', apartment, 7, 13.8, 1.7, 0.5 * Math.PI, 0.5 * Math.PI, 0, 1/50, 1/50, 1/50);
}

function loadFurniture(url, apartment, x, y, z, rX, rY, rZ, sX, sY, sZ) {
            var loader = new THREE.OBJMTLLoader();
            loader.addEventListener('load', function (event) {

              object = event.content;

              /*var wing2 = object.children[5].children[0];
              var wing1 = object.children[4].children[0];

              wing1.material.alphaTest = 0.5;
              wing1.material.opacity = 0.6;
              wing1.material.transparent = true;

              wing2.material.alphaTest = 0.4;
              wing2.material.opacity = 0.7;
              wing2.material.transparent = true;*/

              //object.scale.set(140, 140, 140);
              mesh = object;
              object.position.set(x,y,z);
              object.scale.set(sX, sY, sZ);
              object.rotation.x = rX;
              object.rotation.y = rY;
              object.rotation.z = rZ;
              apartment.add(mesh);

      /*        object.rotation.x = 0.2;
              object.rotation.y = -1.3;*/
            });

            var baseUrl = 'assets/models/';
            loader.load(
              baseUrl + url + '.obj', 
              baseUrl + url + '.mtl', 
              {side: THREE.DoubleSide}
            );
            
}

function loadFurnitureNoMTL(url, apartment, x, y, z, rX, rY, rZ, sX, sY, sZ) {
            var baseUrl = 'assets/models/';
            var loader = new THREE.OBJLoader();
                  loader.load(baseUrl + url + '.obj', function (object) {
                    var material = new THREE.MeshLambertMaterial({color: 0xffffff, shading: THREE.FlatShading});

                    object.traverse(function (child) {
                      if (child instanceof THREE.Mesh) {
                        child.material = material;
                      }
                    });

                  mesh = object;
                  object.position.set(x,y,z);
                  object.scale.set(sX, sY, sZ);
                  object.rotation.x = rX;
                  object.rotation.y = rY;
                  object.rotation.z = rZ;
                  apartment.add(mesh);
                  });
}


/*      function createMesh2(geom, imageFile, bumpFile) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        geom.computeVertexNormals();
        var mat = new THREE.MeshPhongMaterial();
        mat.map = texture;

        var bump = THREE.ImageUtils.loadTexture("assets/textures/general/" + bumpFile);
        mat.bumpMap = bump;
        mat.bumpScale = 0.2;
      }*/
  
      function createMesh2(geom, imageFile, bumpFile) {
        var texture = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile)
        geom.computeVertexNormals();
        var mat = new THREE.MeshPhongMaterial();
        mat.map = texture;

        if (bump) {
          var bump = THREE.ImageUtils.loadTexture("assets/textures/general/" + bumpFile);
          mat.bumpMap = bump;
          mat.bumpScale = 0.2;
        }

        var mesh = new THREE.Mesh(geom, mat);

        return mesh;
      }
  
      function createMesh(geom, imageFile, normal) {

              if (normal) {
                  var t = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile);
                  var m = THREE.ImageUtils.loadTexture("assets/textures/general/" + normal);
                  var mat2 = new THREE.MeshPhongMaterial({
                      map: t,
                      normalMap: m
                  });
                  //mat2.normalScale.set(2,2);
                  var mesh = new THREE.Mesh(geom, mat2);
                  return mesh;
              } else {
                  var t = THREE.ImageUtils.loadTexture("assets/textures/general/" + imageFile);
                  var mat1 = new THREE.MeshPhongMaterial({
                      map: t
                  })
                  var mesh = new THREE.Mesh(geom, mat1);
                  return mesh;
              }

              return mesh;
          }

      function drawShapeHall(room) {

        // create a basic shape
        var shape = new THREE.Shape();

        if(room == "hall") {
        shape.moveTo(0, 0);
        shape.lineTo(0.132, 0);
        shape.lineTo(0.132, 0.23);
        shape.lineTo(0.24, 0.23);
        shape.lineTo(0.24, 0);
        shape.lineTo(0.83, 0);
        shape.lineTo(0.83, 0.27);
        shape.lineTo(0, 0.27);
        shape.lineTo(0, 0);
        } 
        if(room=="hallDx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.62, 0);
          shape.lineTo(0.62, 0.23); 
          shape.lineTo(0.72, 0.23);
          shape.lineTo(0.72, 0);
          shape.lineTo(1.02, 0);
          shape.lineTo(1.02, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }
        if(room=="kitchenSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.1, 0);
          shape.lineTo(0.1, 0.23); 
          shape.lineTo(0.2, 0.23);
          shape.lineTo(0.2, 0);
          shape.lineTo(0.5, 0);
          shape.lineTo(0.5, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }
        if(room=="rRoomSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.51, 0);
          shape.lineTo(0.51, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="rRoomDx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.36, 0);
          shape.lineTo(0.36, 0.23);
          shape.lineTo(0.46, 0.23);
          shape.lineTo(0.46, 0);
          shape.lineTo(0.51, 0);
          shape.lineTo(0.51, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="rRoomNth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.14, 0);
          shape.lineTo(0.14, 0.23);
          shape.lineTo(0.23, 0.23);
          shape.lineTo(0.23, 0);
          shape.lineTo(0.51, 0);
          shape.lineTo(0.51, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="lRoomSth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.4, 0);
          shape.lineTo(0.4, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="bath") {
          shape.moveTo(0, 0);
          shape.lineTo(0.3, 0);
          shape.lineTo(0.3, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="corridorNth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.16, 0);
          shape.lineTo(0.16, 0.23);
          shape.lineTo(0.268, 0.23);
          shape.lineTo(0.268, 0);
          shape.lineTo(0.71, 0);
          shape.lineTo(0.71, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="corridorSth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.16, 0);
          shape.lineTo(0.16, 0.23);
          shape.lineTo(0.268, 0.23);
          shape.lineTo(0.268, 0);
          shape.lineTo(0.55, 0);
          shape.lineTo(0.55, 0.23);
          shape.lineTo(0.64, 0.23);
          shape.lineTo(0.64, 0);
          shape.lineTo(0.72, 0);
          shape.lineTo(0.72, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="bathSth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.16, 0);
          shape.lineTo(0.16, 0.23);
          shape.lineTo(0.268, 0.23);
          shape.lineTo(0.268, 0);
          shape.lineTo(0.4, 0);
          shape.lineTo(0.4, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="uppRoomSth") {
          shape.moveTo(0, 0);
          shape.lineTo(0.31, 0);
          shape.lineTo(0.31, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="uppRoomSth2") {
          shape.moveTo(0, 0);
          shape.lineTo(0.2, 0);
          shape.lineTo(0.2, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="corridorSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.05, 0);
          shape.lineTo(0.05, 0.23);
          shape.lineTo(0.15, 0.23);
          shape.lineTo(0.15, 0);
          shape.lineTo(0.2, 0);
          shape.lineTo(0.2, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }
        if(room=="uppRoomSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.05, 0);
          shape.lineTo(0.05, 0.23);
          shape.lineTo(0.15, 0.23);
          shape.lineTo(0.15, 0);
          shape.lineTo(0.21, 0);
          shape.lineTo(0.21, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="lRoomDx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.36, 0);
          shape.lineTo(0.36, 0.23);
          shape.lineTo(0.46, 0.23);
          shape.lineTo(0.46, 0);
          shape.lineTo(0.51, 0);
          shape.lineTo(0.51, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
        }

        if(room=="lRoomSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.51, 0);
          shape.lineTo(0.51, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);

          //Window
          var hole = new THREE.Path( [new THREE.Vector2( 0.285, 0.135 ), new THREE.Vector2( 0.435, 0.135 ),
                                      new THREE.Vector2( 0.435, 0.245 ), new THREE.Vector2( 0.285, 0.245 )]);
          shape.holes.push(hole);

        }

        if(room=="hallSx") {
          shape.moveTo(0, 0);
          shape.lineTo(0.77, 0);
          shape.lineTo(0.77, 0.23);
          shape.lineTo(0.92, 0.23);
          shape.lineTo(0.92, 0);
          shape.lineTo(1.02, 0);
          shape.lineTo(1.02, 0.27);
          shape.lineTo(0, 0.27);
          shape.lineTo(0, 0);
          //Window
          var hole = new THREE.Path( [new THREE.Vector2( 0.02, 0.135 ), new THREE.Vector2( 0.375, 0.135 ),
                                      new THREE.Vector2( 0.375, 0.245 ), new THREE.Vector2( 0.02, 0.245 )]);
          shape.holes.push(hole);

        }

        return shape;
      }