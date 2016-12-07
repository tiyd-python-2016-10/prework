function is_prime(n){
    if(n <= 1) return false 
    var i = 2;
    while (i*i <= n)
        if(!(n%i++))
            return false
    return true
}

function is_anagram(lhs, rhs){
    if(lhs.length != rhs.length) return false
    var lhsd = {}
    var rhsd = {}
    for(var i = 0; i < lhs.length; i++){
      if(lhsd.hasOwnProperty(lhs[i])){
        lhsd[lhs[i]]++
      }else{
        lhsd[lhs[i]] = 1
      }
      if(rhsd.hasOwnProperty(rhs[i])){
        rhsd[rhs[i]]++
      }else{
        rhsd[rhs[i]] = 1
      }
    }

    for(var prop in lhsd){
      if(lhsd[prop] != rhsd[prop]) return false
    }
        return true
}












console.log(is_prime(2))
console.log(is_prime(3))
console.log(is_prime(5))
console.log(is_prime(7))
console.log(is_prime(8675309))
console.log(!is_prime(4))
console.log(!is_prime(1))
console.log(!is_prime(25))
console.log(!is_prime(9))
console.log(!is_prime(6))
console.log(!is_anagram('abc', 'def'))
console.log(is_anagram('race', 'care'))
console.log(!is_anagram('race', 'carer'))
console.log(!is_anagram('racer', 'care'))
console.log(is_anagram('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))


