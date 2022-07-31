function solution(arr1, arr2) {
  var answer = [];
  let N = arr1.length;
  let M = arr2[0].length;
  let L = arr2.length;

  for (let i = 0; i < N; i++) {
    let temp_arr = [];
    for (let j = 0; j < M; j++) {
      let temp_v = 0;
      for (let k = 0; k < L; k++) {
        temp_v += arr1[i][k] * arr2[k][j];
      }
      temp_arr.push(temp_v);
    }
    answer.push(temp_arr);
  }

  return answer;
}
