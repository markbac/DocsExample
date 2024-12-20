## wavedrom

### Timing

```wavedrom
{ signal: [
  { name: "clk",         wave: "p.....|..." },
  { name: "Data",        wave: "x.345x|=.x", data: ["head", "body", "tail", "data"] },
  { name: "Request",     wave: "0.1..0|1.0" },
  {},
  { name: "Acknowledge", wave: "1.....|01." }
]}
```
### timing 2

```wavedrom
{signal: [
 {wave: '01010101010101'}, // toggling
 {wave: '0.1.0.hl'}, // dot(.) holds a value, h/l for high and low
 {wave: '222xxx345.6789'}, // multi-bit, X, 345 = colors, 6789 == x
 {wave:''}, // blank line
 // text
 {wave: '2.2.2.2.2.2.2.',
 data:["abcdefg","hijk","lmnop","qrs","tuv","wx","yz"]},
 {wave:''},
 // names and clocks
 {name: "posclk", wave: 'pPp...........' }, // capital letters for arrows
 {name: "negclk", wave: 'n.N..n........' },
 {name: "divclk", wave: 'lplpl.h.l.h.pl' }, 
 {wave:''},
 // fun
 {name: "Barak", wave: '01.zx=ud.23.45'},
 // gaps
 {name: "gaps", wave: '01|022|0|x|.22' },
 // arrows with nodes and edges
 {name: "arrows", wave: '0n0....2..x2..',
 node: '.a........d' },
 { wave: '1.0.10..x0....',
 node: '....b...c' },
 ],
edge:['a~>b glitch',
 'c<~>d I found the bug!',
 ],
}
```

### SRAM

```wavedrom

    {'signal': [
        {'name': 'Address',     'wave': 'x4......x.', 'data': ['Valid address']},
        {'name': 'Chip Select', 'wave': '1.0.....1.'},
        {'name': 'Out Enable',  'wave': '1.0.....1.'},
        {'name': 'Data Out',    'wave': 'z...x6...z', 'data': ['Valid data']},
    ],
     'edge': ['[0^:1.2]+[0^:8] $t_{WC}$',
              '[0v:1]+[0v:5] $t_{AQ}$',
              '[1:2]+[1:5] $t_{EQ}$',
              '[2:2]+[2:5] $t_{GQ}$',
              '[0^:5]-[3v:5]{lightgray,:}',
             ]
    }
```

### example

```wavedrom
{signal: [
  {name:'clk',         wave: 'p....' },
  {name:'Data',        wave: 'x345x', data: 'a b c' },
  {name:'Request',     wave: '01..0' }
],
 head:{
   text:'WaveDrom example',
   tick:0,
   every:2
 },
 foot:{
   text:'Figure 100',
   tock:9
 },
}
```

### example 2

```wavedrom
{ signal: [
  { name: 'A', wave: '01........0....',  node: '.a........j' },
  { name: 'B', wave: '0.1.......0.1..',  node: '..b.......i' },
  { name: 'C', wave: '0..1....0...1..',  node: '...c....h..' },
  { name: 'D', wave: '0...1..0.....1.',  node: '....d..g...' },
  { name: 'E', wave: '0....10.......1',  node: '.....ef....' }
  ],
  edge: [
    'a~b t1', 'c-~a t2', 'c-~>d time 3', 'd~-e',
    'e~>f', 'f->g', 'g-~>h', 'h~>i some text', 'h~->j'
  ]
}
```

### example 3

```wavedrom
{ signal: [
  { name: 'A', wave: '01..0..',  node: '.a..e..' },
  { name: 'B', wave: '0.1..0.',  node: '..b..d.', phase:0.5 },
  { name: 'C', wave: '0..1..0',  node: '...c..f' },
  {                              node: '...g..h' },
  {                              node: '...I..J',  phase:0.5 },
  { name: 'D', wave: '0..1..0',  phase:0.5 }
  ],
  edge: [
    'b-|a t1', 'a-|c t2', 'b-|-c t3', 'c-|->e t4', 'e-|>f more text',
    'e|->d t6', 'c-g', 'f-h', 'g<->h 3 ms', 'I+J 5 ms'
  ]
}
```

### example 4

```doesntwork
(function (bits, ticks) {
  var i, t, gray, state, data = [], arr = [];
  for (i = 0; i < bits; i++) {
    arr.push({name: i + '', wave: ''});
    state = 1;
    for (t = 0; t < ticks; t++) {
      data.push(t + '');
      gray = (((t >> 1) ^ t) >> i) & 1;
      arr[i].wave += (gray === state) ? '.' : gray + '';
      state = gray;
    }
  }
  arr.unshift('gray');
  return {signal: [
    {name: 'bin', wave: '='.repeat(ticks), data: data}, arr
  ]};
})(5, 16)
```
### IEC 60617 Symbols

```doesntwork
{ assign:[
  ["out",
    ["XNOR",
      ["NAND",
        ["INV", "a"],
        ["NOR", "b", ["BUF","c"]]
      ],
      ["AND",
        ["XOR", "d", "e", ["OR","f","g"]],
        "h"
      ]
    ]
  ]
]}
```