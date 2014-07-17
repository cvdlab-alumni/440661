
var UNIT = 10;

var map = [ // 1  2  3  4  5  6  7  8  9  0
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], // 0
           [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,], // 1
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,], // 2
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], // 3
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,], // 4
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,], // 5
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,], // 6
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,], // 7
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,], // 8
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0,], // 9
           ]

function canWalk(target) {
  var j = Math.round(target.position.x / UNIT);
  var i = Math.abs(Math.round(target.position.z / UNIT));
  if(i>= 0 && j >=0 && i<10 && j<=16) {
    if(map[i][j] == 1)
      return false;
  }
  return true;
}

function checkCollision(walk, controls, target) {
  var decremented = false;
  if(walk) {
    controls.update();
  } else {
    if(target.position.x/10 >= 9) {
      if(target.position.z/10 > -2 && target.position.z/10 < 0 ){
        target.position.z -= 1;
      }
      else {
      target.position.x -=3;
      controls.update();
    }

    }
    if(target.position.z/10<=-8) {
      target.position.z +=1;
    }
    else {
      target.position.z -= 1;
    }
  }
}