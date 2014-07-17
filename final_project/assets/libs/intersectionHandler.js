function checkIntersections(list, scene, apartment) {

	var intersectsKit = list[0];
	var intersectsHall = list[1];
	var intersectsBath = list[2];
	var intersectsRRoom = list[3];
	var intersectsLRoom = list[4];
	var intersectsUppRoom = list[5];
	var intersectsWinKit = list[6];
	var intersectsWinHall1 = list[7];
	var intersectsWinHall2 = list[8];
	var intersectsWindowHall1 = list[9];
	var intersectsWindowHall2 = list[10];
	var intersectsWindowLR1 = list[11];
	var intersectsWindowLR2 = list[12];
	var intersectsWindowUR1 = list[13];
	var intersectsWindowUR2 = list[14];
	var intersectsWinRRoom = list[15];
	var intersectsMain = list[16];
	var intersectsHallSwitch = list[17];

	if (intersectsKit.length > 0) {

	    var hitObject = intersectsKit[0].object;
	    console.log(hitObject);

	    if(scene.jointKitchen.rotation.y == +0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointKitchen.rotation)
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       //.chain(handleTween1)
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointKitchen.rotation)
	       .to({y: +0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       //.chain(handleTween1)
	       .start();
	   }
	    console.log("hit object: ", hitObject);
	}

	if (intersectsHall.length > 0) {

	    var hitObject = intersectsHall[0].object;
	    console.log(hitObject);
	    if(scene.jointHall.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointHall.rotation)
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointHall.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsBath.length > 0) {

	    var hitObject = intersectsBath[0].object;
	    console.log(hitObject);
	    if(scene.jointBath.rotation.y == +0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointBath.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointBath.rotation)
	       //.to({z:20, y: 10})
	       .to({y: +0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsRRoom.length > 0) {

	    var hitObject = intersectsRRoom[0].object;
	    console.log(hitObject);
	    if(scene.jointRRoom.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointRRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointRRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsLRoom.length > 0) {

	    var hitObject = intersectsLRoom[0].object;
	    console.log(hitObject);
	    if(scene.jointLRoom.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointLRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointLRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsUppRoom.length > 0) {

	    var hitObject = intersectsUppRoom[0].object;
	    console.log(hitObject);
	    if(scene.jointUppRoom.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointUppRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointUppRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWinKit.length > 0) {

	    var hitObject = intersectsWinKit[0].object;
	    console.log(hitObject);
	    if(scene.jointWinKit.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWinKit.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWinKit.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWinHall1.length > 0) {

	    var hitObject = intersectsWinHall1[0].object;
	    console.log(hitObject);
	    if(scene.jointWinHall1.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWinHall1.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWinHall1.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWinHall2.length > 0) {

	    var hitObject = intersectsWinHall2[0].object;
	    console.log(hitObject);
	    if(scene.jointWinHall2.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWinHall2.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWinHall2.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWindowHall1.length > 0) {

	    var hitObject = intersectsWindowHall1[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowHall1.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowHall1.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowHall1.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWindowHall2.length > 0) {

	    var hitObject = intersectsWindowHall2[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowHall2.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowHall2.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowHall2.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: w2", hitObject);

	}
	if (intersectsWindowLR1.length > 0) {

	    var hitObject = intersectsWindowLR1[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowLR1.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowLR1.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowLR1.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWindowLR2.length > 0) {

	    var hitObject = intersectsWindowLR2[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowLR2.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowLR2.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowLR2.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: w2", hitObject);

	}
	if (intersectsWindowUR1.length > 0) {

	    var hitObject = intersectsWindowUR1[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowUR1.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowUR1.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowUR1.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsWindowUR2.length > 0) {

	    var hitObject = intersectsWindowUR2[0].object;
	    console.log(hitObject);
	    if(scene.jointWindowUR2.rotation.y == -0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWindowUR2.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWindowUR2.rotation)
	       //.to({z:20, y: 10})
	       .to({y: -0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: w2", hitObject);

	}
	if (intersectsWinRRoom.length > 0) {

	    var hitObject = intersectsWinRRoom[0].object;
	    console.log(hitObject);
	    if(scene.jointWinRRoom.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointWinRRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointWinRRoom.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	if (intersectsMain.length > 0) {

	    var hitObject = intersectsMain[0].object;
	    console.log(hitObject);
	    if(scene.jointMain.rotation.y == 0.5*Math.PI) {

	     var objectTween1 = new TWEEN.Tween(scene.jointMain.rotation)
	       //.to({z:20, y: 10})
	       .to({y:0}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    else {
	     var objectTween1 = new TWEEN.Tween(scene.jointMain.rotation)
	       //.to({z:20, y: 10})
	       .to({y: 0.5*Math.PI}, 500)
	       .easing(TWEEN.Easing.Elastic.In )
	       .start();
	   }
	    console.log("hit object: ", hitObject);

	}
	//SWITCHES

	if (intersectsHallSwitch.length > 0) {
	 var hitObject = intersectsHallSwitch[0].object;
	 console.log(hitObject);
	 var spotLight1 = apartment.hallLight1.bulbFilament.bulb.spotLight;
	 var spotLight2 = apartment.hallLight2.bulbFilament.bulb.spotLight;
	 console.log(spotLight1);

	 if(spotLight1.castShadow) {
	   //Spotlight 1
	   apartment.hallLight1.bulbFilament.bulb.spotLight.castShadow = false;
	   apartment.hallLight1.bulbFilament.bulb.remove(apartment.hallLight1.bulbFilament.bulb.spotLight);
	   //apartment.hallLight1.bulbFilament.bulb.remove(apartment.hallLight1.bulbFilament.bulb.bulbPointLight);
	   //console.log(spotLight1);
	   renderer.clearTarget( apartment.hallLight1.bulbFilament.bulb.spotLight.shadowMap );
	   apartment.hallLight1.bulbFilament.material.color.setHex( 0x000000 );
	   //Spotlight 2
	   apartment.hallLight2.bulbFilament.bulb.spotLight.castShadow = false;
	   apartment.hallLight2.bulbFilament.bulb.remove(apartment.hallLight2.bulbFilament.bulb.spotLight);
	   //apartment.hallLight2.bulbFilament.bulb.remove(apartment.hallLight2.bulbFilament.bulb.bulbPointLight);
	   //console.log(spotLight1);
	   renderer.clearTarget( apartment.hallLight2.bulbFilament.bulb.spotLight.shadowMap );
	   apartment.hallLight2.bulbFilament.material.color.setHex( 0x000000 );
	  
	 }
	 else {
	   //Spotlight 1
	   //console.log("ajajajj " + spotLight);
	   spotLight1.castShadow = true;
	   apartment.hallLight1.bulbFilament.bulb.add(spotLight1);
	   //apartment.hallLight1.bulbFilament.bulb.add(apartment.hallLight1.bulbFilament.bulb.bulbPointLight);
	   apartment.hallLight1.bulbFilament.material.color.setHex( 0xff0000 );
	   //Spotlight 2
	   spotLight2.castShadow = true;
	   apartment.hallLight2.bulbFilament.bulb.add(spotLight2);
	   //apartment.hallLight2.bulbFilament.bulb.add(apartment.hallLight2.bulbFilament.bulb.bulbPointLight);
	   apartment.hallLight2.bulbFilament.material.color.setHex( 0xff0000 );
	   

	 }
	}
}