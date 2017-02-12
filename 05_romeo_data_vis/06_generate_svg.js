var draw = SVG('drawing').size(1000, 5000);
var groups = [];
for (act of [1,2,3,4,5]) {
  groups.push(rect)
}
for (line of romeo_data) {
  var rect = draw.rect(100, 1).attr({ fill: 'blue' });
  var act = line['act'];
  console.log(act);
}

// var svg = document.getElementById('mySvg');
// var count = 0;
// var act = '';
// var scene = '';
// for (line of romeo_data) {
//   count += 1;
//   if (line['act'] != act) {
//     con.beginPath();
//     context.rect(1, count, 1000, 10);
//     context.fill_style = 'red';
//     context.fill();
//     act = line['act']
//   };
//   var height = 1;
//   var width = Math.abs(line['line_polarity']) * 100;
//   var start_position = (function(line) {
//     if (line['line_polarity'] < 0) {
//       return 500 - width;
//     } else {
//       return 500;
//     };
//   }(line));
//   context.beginPath();
//   context.rect(start_position, count, width, 1);
//   context.fillStyle = 'blue';
//   context.fill();
// }

