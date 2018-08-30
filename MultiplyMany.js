function mul(x) {
  return function(y){
      return function(z){
          if(isNaN(x) || isNaN(y) || isNaN(z)) {
            return "Please enter in 3 numbers";
          }
          else { return x * y * z; };
      };
  };
}

console.log(mul(3)(4)(12))
