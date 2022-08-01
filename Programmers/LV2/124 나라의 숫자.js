function solution(n) {
  var answer = "";
  let num = ["1", "2", "4"];
  while (n >= 1) {
    answer = num[(n - 1) % 3] + answer;
    if (n % 3) {
      n = parseInt(n / 3);
    } else {
      n = parseInt(n / 3) - 1;
    }
  }
  return answer;
}
