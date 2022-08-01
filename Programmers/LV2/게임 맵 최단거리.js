function solution(maps) {
  var answer = -1;
  let n = maps.length;
  let m = maps[0].length;

  let visited = [];
  for (let i = 0; i < n; i++) {
    let temp = [];
    for (let j = 0; j < m; j++) {
      temp.push(1000000000);
    }
    visited.push(temp);
  }

  let queue = [[0, 0]];
  visited[0][0] = 1;
  let dr = [-1, 1, 0, 0];
  let dc = [0, 0, -1, 1];
  while (queue.length) {
    let v = queue.shift();
    let r = v[0];
    let c = v[1];
    for (k = 0; k < 4; k++) {
      let new_r = r + dr[k];
      let new_c = c + dc[k];
      if (0 <= new_r && new_r < n && 0 <= new_c && new_c < m) {
        if (maps[new_r][new_c] && visited[new_r][new_c] > visited[r][c] + 1) {
          queue.push([new_r, new_c]);
          visited[new_r][new_c] = visited[r][c] + 1;
        }
      }
    }
  }

  if (visited[n - 1][m - 1] !== 1000000000) {
    answer = visited[n - 1][m - 1];
  }

  return answer;
}
