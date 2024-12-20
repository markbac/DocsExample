## dod

### ports

```dot
digraph H {

  parent [
   shape=plaintext
   label=<
     <table border='1' cellborder='1'>
       <tr><td colspan="3">The foo, the bar and the baz</td></tr>
       <tr><td port='port_one'>First port</td><td port='port_two'>Second port</td><td port='port_three'>Third port</td></tr>
     </table>
  >];

  child_one [
   shape=plaintext
   label=<
     <table border='1' cellborder='0'>
       <tr><td>1</td></tr>
     </table>
  >];

  child_two [
   shape=plaintext
   label=<
     <table border='1' cellborder='0'>
       <tr><td>2</td></tr>
     </table>
  >];

  child_three [
   shape=plaintext
   label=<
     <table border='1' cellborder='0'>
       <tr><td>3</td></tr>
     </table>
  >];

  parent:port_one   -> child_one;
  parent:port_two   -> child_two;
  parent:port_three -> child_three;

}
```

### Project Dependencies

```dot
digraph D {

  node [shape=plaintext fontname="Sans serif" fontsize="8"];

  task_menu [ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 1</b></td></tr>
     <tr><td align="left">Choose Menu</td></tr>
     <tr><td align="left"><font color="darkgreen">done</font></td></tr>
   </table>>];

  task_ingredients [ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 2</b></td></tr>
     <tr><td align="left">Buy ingredients</td></tr>
     <tr><td align="left"><font color="darkgreen">done</font></td></tr>
   </table>>];

  task_invitation [ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 4</b></td></tr>
     <tr><td align="left">Send invitation</td></tr>
     <tr><td align="left"><font color="darkgreen">done</font></td></tr>
   </table>>];

  task_cook [ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 5</b></td></tr>
     <tr><td align="left">Cook</td></tr>
     <tr><td align="left"><font color="red">todo</font></td></tr>
   </table>>];

  task_table[ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 3</b></td></tr>
     <tr><td align="left">Lay table</td></tr>
     <tr><td align="left"><font color="red">todo</font></td></tr>
   </table>>];

  task_eat[ label=<
   <table border="1" cellborder="0" cellspacing="1">
     <tr><td align="left"><b>Task 6</b></td></tr>
     <tr><td align="left">Eat</td></tr>
     <tr><td align="left"><font color="red">todo</font></td></tr>
   </table>>];


  task_menu        -> task_ingredients;
  task_ingredients -> task_cook;
  task_invitation  -> task_cook;
  task_table       -> task_eat;
  task_cook        -> task_eat;
}
```
### organization chart

```dot
// Inspired by
//    https://stackoverflow.com/a/7374543/180275

digraph ORG {

  ranksep=0.2;

  node[shape=box3d width=2.3 height=0.6 fontname="Arial"];

  CEO     [ label = "Important CEO"      ]
  CFO     [ label = "Less important CFO" ]
  HR      [ label = "Human Resources"    ]
  CxO     [ label = "An unknown CxO"     ]

  staff_1 [ label = "Staff 1"]
  staff_2 [ label = "Staff 2"]
  staff_3 [ label = "Staff 3"]
  staff_4 [ label = "Staff 4"]

  node[shape=none, width=0, height=0, label=""];

  edge[dir=none];

  CEO -> hierarchy_1 -> hierarchy_2 -> hierarchy_3;

  {rank=same; CFO -> hierarchy_1 -> HR;}
  {rank=same; CxO -> hierarchy_2;}
  {rank=same; staff_1 -> staff_2 -> hierarchy_4 -> staff_3 -> staff_4 }

  hierarchy_3 -> hierarchy_4


}

```

### Basic Git Concepts and Operations

```dot
digraph git_basics {
	graph [
		label = "Basic git concepts and operations\n\n"
		labelloc = t
		fontname = "Helvetica,Arial,sans-serif"
		fontsize = 20
		layout = dot
		rankdir = LR
		newrank = true
	]
	node [
		style=filled
		shape=rect
		pencolor="#00000044" // frames color
		fontname="Helvetica,Arial,sans-serif"
		shape=plaintext
	]
	edge [
		arrowsize=0.5
		fontname="Helvetica,Arial,sans-serif"
		labeldistance=3
		labelfontcolor="#00000080"
		penwidth=2
		style=dotted // dotted style symbolizes data transfer
	]
	changes [
		color="#88000022"
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>changes</b><br/>in the working tree </td> </tr>
			<tr> <td align="left"><i>To view: </i><br align="left"/>
			git diff
			<br align="left"/></td> </tr>
		</table>>
		shape=plain
	]
	staging [
		fillcolor="#ff880022"
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>staging area</b><br/>(cache, index)</td> </tr>
			<tr> <td align="left"><i>To view: </i><br align="left"/>
			git diff --staged
			<br align="left"/></td> </tr>
		</table>>
		shape=plain
	]
	staging -> HEAD:push [label="git commit" weight=1000 color="#88000088"]
	stash [
		fillcolor="#0044ff22"
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>stash</b></td> </tr>
			<tr> <td align="left"><i>To view:</i><br align="left"/>
			git stash list
			<br align="left"/></td> </tr>
		</table>>
		shape=plain
	]
	stash_push [
		label="git stash [push]"
		style=""
		shape=plain
		color="#00008844"
	]
	{
		edge [arrowhead=none color="#00008844"]
		changes ->  stash_push
		stash_push -> staging
	}
	changes -> stash [
		dir=back
		xlabel="git stash pop"
		color="#00000088" weight=0]
	stash_push -> stash [xdir=back color="#00008844" minlen=0]
	HEAD [
		fillcolor="#88ff0022"
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="3">
			<tr> <td port="push" sides="ltr"> <b>HEAD </b>of</td> </tr>
			<tr> <td port="pull" sides="lbr"> the current branch</td> </tr>
			<tr> <td port="switch" align="left">
				<i>To view:</i>
				<br align="left"/>
				git show<br align="left"/>
				git log
				<br align="left"/>
			</td> </tr>
			<tr> <td align="left">
				<i>To change branch:</i><br align="left"/>
				git switch ...
				<br align="left"/>
				git checkout ...
				<br align="left"/>
			</td> </tr>
		</table>>
		shape=plain
	]
	remote [
		label="remote branch"
		shape=box
		color="#00000022"
		fillcolor="#00ff0022"
	]

	HEAD:push -> remote [label="git push" color="#88000088"]
	HEAD:pull -> remote [dir=back label="git pull" color="#00440088"]
	branches [
		fillcolor="#00888822"
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>local branches</b> </td> </tr>
			<tr> <td align="left"><i>To view:</i><br align="left"/>
			git branch [--list]
			<br align="left"/></td> </tr>
			</table>>
		shape=plain
	]
	changes -> staging [label="git add ...    \ngit reset      " color="#88000088"]
	discard [shape=plaintext style=""]
	changes -> discard [label="git restore ..." color="#88000088"]
	{rank=same changes discard}
	// UML style aggregation
	HEAD:switch -> branches [
		dir=back
		style=""
		penwidth=1
		arrowtail=odiamond
		arrowhead=none
		color="#00000088"
	]
}
// © 2022 Costa Shulyupin, licensed under EPL
```

### data structures

```dot
digraph g {
fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]
graph [
rankdir = "LR"
];
node [
fontsize = "16"
shape = "ellipse"
];
edge [
];
"node0" [
label = "<f0> 0x10ba8| <f1>"
shape = "record"
];
"node1" [
label = "<f0> 0xf7fc4380| <f1> | <f2> |-1"
shape = "record"
];
"node2" [
label = "<f0> 0xf7fc44b8| | |2"
shape = "record"
];
"node3" [
label = "<f0> 3.43322790286038071e-06|44.79998779296875|0"
shape = "record"
];
"node4" [
label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
shape = "record"
];
"node5" [
label = "<f0> (nil)| | |-1"
shape = "record"
];
"node6" [
label = "<f0> 0xf7fc4380| <f1> | <f2> |1"
shape = "record"
];
"node7" [
label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
shape = "record"
];
"node8" [
label = "<f0> (nil)| | |-1"
shape = "record"
];
"node9" [
label = "<f0> (nil)| | |-1"
shape = "record"
];
"node10" [
label = "<f0> (nil)| <f1> | <f2> |-1"
shape = "record"
];
"node11" [
label = "<f0> (nil)| <f1> | <f2> |-1"
shape = "record"
];
"node12" [
label = "<f0> 0xf7fc43e0| | |1"
shape = "record"
];
"node0":f0 -> "node1":f0 [
id = 0
];
"node0":f1 -> "node2":f0 [
id = 1
];
"node1":f0 -> "node3":f0 [
id = 2
];
"node1":f1 -> "node4":f0 [
id = 3
];
"node1":f2 -> "node5":f0 [
id = 4
];
"node4":f0 -> "node3":f0 [
id = 5
];
"node4":f1 -> "node6":f0 [
id = 6
];
"node4":f2 -> "node10":f0 [
id = 7
];
"node6":f0 -> "node3":f0 [
id = 8
];
"node6":f1 -> "node7":f0 [
id = 9
];
"node6":f2 -> "node9":f0 [
id = 10
];
"node7":f0 -> "node3":f0 [
id = 11
];
"node7":f1 -> "node1":f0 [
id = 12
];
"node7":f2 -> "node8":f0 [
id = 13
];
"node10":f1 -> "node11":f0 [
id = 14
];
"node10":f2 -> "node12":f0 [
id = 15
];
"node11":f2 -> "node1":f0 [
id = 16
];
}
```

### Linux kernel diag

```dot
digraph "Linux_kernel_diagram" {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	graph [
		newrank = true,
		nodesep = 0.3,
		ranksep = 0.2,
		overlap = true,
		splines = false,
	]
	node [
		fixedsize = false,
		fontsize = 24,
		height = 1,
		shape = box,
		style = "filled,setlinewidth(5)",
		width = 2.2
	]
	edge [
		arrowhead = none,
		arrowsize = 0.5,
		labelfontname = "Ubuntu",
		weight = 10,
		style = "filled,setlinewidth(5)"
	]
	subgraph system {
		node [color = "#e27dd6ff"]
		edge [color = "#e27dd6ff"]
		system_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			shape = point
		]
		system [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/System",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		system -> system_ [
			arrowhead = "",
			row = func];
		SCI [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Syscalls",
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "System calls",
			row = usr,
			shape = ellipse]
		sysfs [
			fillcolor = "#b2d3e4",
			label = "proc & sysfs\nfile systems"]
		SCI -> sysfs
		DM [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "Device\nModel",
			shape = octagon,
			width = 2]
		sysfs -> DM
		log_sys [
			fillcolor = "#6a9ab1",
			fontsize = 20,
			label = "system run,\nmodules,\ngeneric\nHW access "]
		DM -> log_sys
		bus_drv [
			fillcolor = "#71809b",
			label = "bus drivers"]
		log_sys -> bus_drv
		buses [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "buses:\nPCI, USB ...",
			row = chip]
		bus_drv -> buses
	}
	subgraph networking {
		node [color = "#61c2c5"]
		edge [color = "#61c2c5"]
		networking_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			shape = point
				width = 0]
		networking [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Networking",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		networking -> networking_ [
			arrowhead = "",
			row = func]
		sock [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = Sockets,
			row = usr,
			shape = ellipse]
		prot_fam [
			fillcolor = "#b2d3e4",
			label = "protocol\nfamilies"]
		sock -> prot_fam
		log_prot [
			fillcolor = "#6a9ab1",
			label = "protocols:\nTCP, UDP, IP"]
		prot_fam -> log_prot
		netif [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "network\ninterfaces\nand drivers"]
		log_prot -> netif
		net_hw [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "network:\nEthernet, WiFi ...",
			row = chip]
		netif -> net_hw
		NFS [
			color = "#8383cc",
			fillcolor = "#91b5c9",
			fixedsize = true,
			height = 0.8,
			label = NFS,
			shape = octagon,
			width = 1.2]
		NFS -> log_prot [weight = 0]
	}
	subgraph processing {
		node [color = "#c46747"]
		edge [color = "#c46747"]
		processing_ [
			fixedsize = true,
			height = 0,
			shape = point
				style = invis,
			width = 0]
		processing [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Processing",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		processing -> processing_ [
			arrowhead = "",
			row = func]
		proc [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = Processes,
			row = usr,
			shape = ellipse]
		Tasks [
			fillcolor = "#b2d3e4"]
		proc -> Tasks
		sync [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			fontname = "Arial Narrow"
			label = synchronization,
			height = 0.7,
			//width = 2,
			shape = octagon]
		Tasks -> sync
		sched [
			fillcolor = "#6a9ab1",
			label = Scheduler]
		sync -> sched
		IRQ [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "interrupts\ncore,\nCPU arch"]
		sched -> IRQ
		CPU [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			row = chip]
		IRQ -> CPU
	}	// processing
	subgraph mem {
		node [
			color = "#51bf5b",
			height = 1
		]
		edge [color = "#51bf5b"]
		MA [
			color = "#51bf5b",
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "memory\naccess",
			row = usr,
			height = 1,
			shape = ellipse]
		MA -> VM
		mmap [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "memory\nmapping",
			shape = octagon,
			width = 2]
		mmap -> log_mem
		log_mem -> PA
		SW [
			color = "#8383cc",
			fillcolor = "#91b5c9",
			fixedsize = true,
			label = Swap,
			height = 0.8,
			shape = octagon,
			width = 1.2]
		mmap -> SW [weight = 1]
		SW -> block [
			color = "#8383cc", weight = 1]
		PA [
			fillcolor = "#71809b",
			label = "Page\nAllocator"
		]
		PC -> PA [weight = 0 color="#51bf5b"]
		RAM [
			color = "#51bf5b",
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "MMU, RAM",
			height = 1,
			row = chip]
		PA -> RAM
		memory -> memory_ [
			arrowhead = "",
			row = func]
		VM -> mmap
	}	// mem
	subgraph storage {
		node [color = "#8383cc"]
		edge [color = "#8383cc"]
		NFS;
		storage_ [
			shape = point,
			fixedsize = true,
			height = 0,
			style = invis,
			width = 0]
		storage [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Storage",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		storage -> storage_ [
			arrowhead = "",
			row = func]
		FS [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "files and\ndirectories",
			row = usr,
			shape = ellipse]
		VFS [
			fillcolor = "#b2d3e4",
			label = "Virtual\nFile System"]
		FS -> VFS
		VFS -> mmap [weight = 0]
		VFS -> NFS [weight = 0]
		logFS [
			fillcolor = "#6a9ab1",
			fontsize = 20,
			label = "logical\nfilesystems:\next3, xfs ..."]
		VFS -> logFS
		PC [
			fillcolor = "#91b5c9",
			fixedsize = true,
			fontsize = 20,
			height = 0.8,
			label = "page\ncache",
			shape = octagon,
			width = 1.2]
		VFS -> PC [weight = 0]
		block [
			fillcolor = "#71809b",
			fontsize = 20,
			label = "Block\ndevices\nand drivers"]
		logFS -> block
		SD [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 20,
			label = "storage devices:\nSCSI, NVMe ...",
			row = chip]
		block -> SD
	}	// storge
	subgraph HI {
		node [color = "#cfbf57ff"]
		edge [
			color = "#cfbf57ff",
			weight = 10
		]
		HI_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		HI [
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Human_interfaces",
			fillcolor = white,
			fixedsize = true,
			fontsize = 12,
			height = 0.6,
			label = "human\ninterface",
			row = func,
			width = 2]
		HI -> HI_ [
			arrowhead = "",
			row = func]
		char [
			fillcolor = "#d9e7ee",
			fixedsize = true,
			label = "char\ndevices",
			row = usr,
			shape = ellipse]
		input [
			fillcolor = "#b2d3e4",
			label = "input\nsubsystem"]
		char -> input
		F7 [
			fillcolor = "#6a9ab1",
			label = "HI class\ndrivers"]
		input -> F7
		HID [
			fillcolor = "#71809b",
			fontsize = 20,
			URL = "https://www.kernel.org/doc/html/latest/hid/",
			label = "HI\nperipherals\ndrivers"]
		F7 -> HID
		display [
			fillcolor = "#777777",
			fontcolor = white,
			fontsize = 19,
			label = "keyboard, mouse,\ndisplay, audio",
			row = chip]
		HID -> display
	} // HI
	subgraph functions {
		graph [rank = same]
		edge [
			style = invis,
			weight = 1
		]
		system;
		networking;
		system -> processing [weight = 1]
		storage -> networking [weight = 1]
		memory [
			color = "#51bf5b",
			URL = "https://en.wikibooks.org/wiki/The_Linux_Kernel/Memory",
			fillcolor = white,
			fixedsize = true,
			height = 0.6,
			row = func,
			width = 2]
		memory -> storage [weight = 1]
		processing -> memory [weight = 1]
		functions_ [
			fixedsize = true,
			height = 0,
			shape = point
			style = invis,
			width = 0]
		functions_ -> HI -> system [weight = 1]
		functions [
			color = gray,
			tooltip = "Columns represent main functionalities of the kernel",
			URL = "http://www.makelinux.net/ldd3/chp-1-sect-2.shtml",
			fillcolor = gray,
			fixedsize = true,
			height = 0.6,
			row = func,
			style = dashed,
			width = 1.6]
		functions -> functions_ [
			arrowhead = "",
			color = gray,
			style = "",
			weight = ""]
	}
	subgraph interfaces {
		graph [rank = same]
		SCI;
		sock;
		FS;
		proc;
		char;
		usr_ [
			fixedsize = true,
			height = 0,
			shape = point
				style = invis,
			width = 0.5]
		usr [
			fillcolor = "#d9e7eeff",
			fixedsize = true,
			label = "user space\ninterfaces",
			row = usr,
			shape = ellipse,
			style = "filled,setlinewidth(0)"]
		MA;
	}
	{
		edge [style = invis weight = 10 ]
		system_;
		SCI;
		system_ -> SCI;
		networking_;
		sock;
		networking_ -> sock;
		storage_;
		FS;
		storage_ -> FS;
		processing_;
		proc;
		processing_ -> proc;
		HI_;
		char;
		HI_ -> char;
		MA;
		memory_ [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		memory_ -> MA;
	}
	subgraph virtual {
		graph [rank = same]
		sysfs;
		prot_fam;
		VFS;
		Tasks;
		input;
		D0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		virt [
			fillcolor = "#b2d3e4",
			label = "virtual\nsubsystems",
			URL = "https://en.wikipedia.org/wiki/Proxy_pattern",
			tooltip = "proxy between standard user space interfaces and internal implementations",
			style = "filled,setlinewidth(0)"]
		VM [
			color = "#51bf5b",
			fillcolor = "#b2d3e4",
			label = "Virtual\nmemory"]
	}
	subgraph bridges {
		graph [rank = same]
		bridges [
			fillcolor = "#91b5c9",
			shape = octagon,
			tooltip = "bridges between uniform virtual interfaces and various implementations",
			URL = "https://en.wikipedia.org/wiki/Bridge_pattern",
			style = "filled,setlinewidth(0)"]
		DM;
		NFS;
		mmap;
		sync;
		E0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		//PC
	}
	subgraph logical {
		graph [rank = same]
		log_sys;
		log_prot;
		logFS;
		sched;
		F7;
		F0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		logical [
			fillcolor = "#6a9ab1",
			style = "filled,setlinewidth(0)"]
		log_mem [
			color = "#51bf5b",
			fillcolor = "#6a9ab1",
			label = "logical\nmemory"]
		//SW
	}
	subgraph HWI {
		graph [rank = same]
		HWI [
			fillcolor = "#71809b",
			label = "hardware\ninterfaces",
			style = "filled,setlinewidth(0)"]
		bus_drv;
		netif;
		block;
		//PA;
		IRQ;
		HID;
		G0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
	}
	subgraph HW {
		graph [rank = same]
		HW [
			fillcolor = "#777777",
			fontcolor = white,
			label = "electronics,\nhardware",
			row = chip,
			style = "filled,setlinewidth(0)"]
		buses;
		net_hw;
		SD;
		CPU;
		display;
		H0 [
			fixedsize = true,
			height = 0,
			shape = point,
			style = invis,
			width = 0]
		RAM;
	}
	bottom [
		label = "© 2007-2022 Costa Shulyupin http://www.MakeLinux.net/kernel/diagram",
		URL = "http://www.MakeLinux.net/kernel/diagram",
		shape = plaintext,
		style = ""]
	CPU -> bottom [style = invis]
	layers [
		fillcolor = lightgray,
		tooltip = "Functionalities are divided to common layers. It is approximate division.",
		height = 0.1,
		style = "filled,setlinewidth(0)",
		width = 0.5]
	functions -> layers [style = invis ]
	usr -> usr_ [
		arrowhead = "",
		color = "#d9e7eeff",
		minlen = 2]
	usr -> virt [
		color = "#d9e7eeff"]
	virt -> D0 [
		arrowhead = "",
		color = "#b2d3e4",
		minlen = 2]
	virt -> bridges [
		color = "#b2d3e4"]
	bridges -> E0 [
		arrowhead = "",
		color = "#91b5c9",
		minlen = 2,
		style = "filled,setlinewidth(6)",
		weight = ""]
	bridges -> logical [
		color = "#91b5c9",
		style = "filled,setlinewidth(6)"]
	logical -> F0 [
		arrowhead = "",
		color = "#6a9ab1",
		minlen = 2,
		row = logical,
		style = "filled,setlinewidth(6)",
		weight = ""]
	logical -> HWI [
		color = "#6a9ab1",
		row = logical,
		style = "filled,setlinewidth(6)"]
	HWI -> G0 [
		arrowhead = "",
		color = "#71809b",
		minlen = 2,
		row = HWI,
		style = "filled,setlinewidth(6)",
		weight = ""]
	HWI -> HW [
		color = "#71809b",
		row = HWI,
		style = "filled,setlinewidth(6)"]
	HW -> H0 [
		arrowhead = "",
		color = "#777777",
		minlen = 2,
		row = chip,
		style = "filled,setlinewidth(6)",
		weight = ""]
	layers -> usr [
		arrowhead = "",
		color = gray,
		style = "filled,setlinewidth(1)"]
	LKD [
		fontsize = 40,
		label = "Linux kernel diagram",
		shape = plain,
		style = ""]
	LKD -> processing [style = invis]
}
```

### Unix family tree

```dot
/* courtesy Ian Darwin and Geoff Collyer, Softquad Inc. */
digraph unix {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [color=lightblue2, style=filled];
	"5th Edition" -> "6th Edition";
	"5th Edition" -> "PWB 1.0";
	"6th Edition" -> "LSX";
	"6th Edition" -> "1 BSD";
	"6th Edition" -> "Mini Unix";
	"6th Edition" -> "Wollongong";
	"6th Edition" -> "Interdata";
	"Interdata" -> "Unix/TS 3.0";
	"Interdata" -> "PWB 2.0";
	"Interdata" -> "7th Edition";
	"7th Edition" -> "8th Edition";
	"7th Edition" -> "32V";
	"7th Edition" -> "V7M";
	"7th Edition" -> "Ultrix-11";
	"7th Edition" -> "Xenix";
	"7th Edition" -> "UniPlus+";
	"V7M" -> "Ultrix-11";
	"8th Edition" -> "9th Edition";
	"1 BSD" -> "2 BSD";
	"2 BSD" -> "2.8 BSD";
	"2.8 BSD" -> "Ultrix-11";
	"2.8 BSD" -> "2.9 BSD";
	"32V" -> "3 BSD";
	"3 BSD" -> "4 BSD";
	"4 BSD" -> "4.1 BSD";
	"4.1 BSD" -> "4.2 BSD";
	"4.1 BSD" -> "2.8 BSD";
	"4.1 BSD" -> "8th Edition";
	"4.2 BSD" -> "4.3 BSD";
	"4.2 BSD" -> "Ultrix-32";
	"PWB 1.0" -> "PWB 1.2";
	"PWB 1.0" -> "USG 1.0";
	"PWB 1.2" -> "PWB 2.0";
	"USG 1.0" -> "CB Unix 1";
	"USG 1.0" -> "USG 2.0";
	"CB Unix 1" -> "CB Unix 2";
	"CB Unix 2" -> "CB Unix 3";
	"CB Unix 3" -> "Unix/TS++";
	"CB Unix 3" -> "PDP-11 Sys V";
	"USG 2.0" -> "USG 3.0";
	"USG 3.0" -> "Unix/TS 3.0";
	"PWB 2.0" -> "Unix/TS 3.0";
	"Unix/TS 1.0" -> "Unix/TS 3.0";
	"Unix/TS 3.0" -> "TS 4.0";
	"Unix/TS++" -> "TS 4.0";
	"CB Unix 3" -> "TS 4.0";
	"TS 4.0" -> "System V.0";
	"System V.0" -> "System V.2";
	"System V.2" -> "System V.3";
}
```

### Color Wheel

```dot
graph Color_wheel {
	graph [
		layout = neato
		label = "Color wheel, 33 colors.\nNeato layout"
		labelloc = b
		fontname = "Helvetica,Arial,sans-serif"
		start = regular
		normalize = 0
	]
	node [
		shape = circle
		style = filled
		color = "#00000088"
		fontname = "Helvetica,Arial,sans-serif"
	]
	edge [
		len = 2.7
		color = "#00000088"
		fontname = "Helvetica,Arial,sans-serif"
	]
	subgraph Dark {
		node [fontcolor = white width = 1.4]
		center [width = 1 style = invis shape = point]
		center -- darkred [label = "0°/360°"]
		darkred [fillcolor = darkred]
		brown [fillcolor = brown]
		brown -- center [label = "30°"]
		olive [fillcolor = olive]
		olive -- center [label = "60°"]
		darkolivegreen [fillcolor = darkolivegreen fontsize = 10]
		darkolivegreen -- center [label = "90°"]
		darkgreen [fillcolor = darkgreen]
		darkgreen -- center [label = "120°"]
		"dark hue 0.416" [color = ".416 1 .6" fontcolor = white]
		"dark hue 0.416" -- center [label = "150°"]
		darkcyan [fillcolor = darkcyan]
		darkcyan -- center [label = "180°"]
		"dark hue 0.583" [color = ".583 1 .6" fontcolor = white]
		"dark hue 0.583" -- center [label = "210°"]
		darkblue [fillcolor = darkblue]
		darkblue -- center [label = "240°"]
		"dark hue 0.750" [color = ".750 1 .6"]
		"dark hue 0.750" -- center [label = "270°"]
		darkmagenta [fillcolor = darkmagenta]
		darkmagenta -- center [label = "300°"]
		"dark hue 0.916" [color = ".916 1 .6"]
		"dark hue 0.916" -- center [label = "330°"]
	}
	subgraph Tue {
		node [width = 1.3]
		"hue 0.083" -- brown
		"hue 0.083" [color = ".083 1 1"]
		"hue 0.125" [color = ".125 1 1"]
		"hue 0.166" -- olive
		"hue 0.166" [color = ".166 1 1"]
		"hue 0.208" [color = ".208 1 1"]
		"hue 0.250" -- darkolivegreen
		"hue 0.250" [color = ".250 1 1"]
		"hue 0.291" [color = ".291 1 1"]
		"hue 0.333" -- darkgreen
		"hue 0.333" [color = ".333 1 1"]
		"hue 0.375" [color = ".375 1 1"]
		"hue 0.416" -- "dark hue 0.416"
		"hue 0.416" [color = ".416 1 1"]
		"hue 0.458" [color = ".458 1 1"]
		"hue 0.500" -- darkcyan
		"hue 0.500" [color = ".500 1 1"]
		"hue 0.541" [color = ".541 1 1"]
		node [fontcolor = white]
		"hue 0.000" [color = ".000 1 1"]
		"hue 0.000" -- darkred
		"hue 0.041" [color = ".041 1 1"]
		"hue 0.583" -- "dark hue 0.583"
		"hue 0.583" [color = ".583 1 1"]
		"hue 0.625" [color = ".625 1 1"]
		"hue 0.666" -- darkblue
		"hue 0.666" [color = ".666 1 1"]
		"hue 0.708" [color = ".708 1 1"]
		"hue 0.750" -- "dark hue 0.750"
		"hue 0.750" [color = ".750 1 1"]
		"hue 0.791" [color = ".791 1 1"]
		"hue 0.833" -- darkmagenta
		"hue 0.833" [color = ".833 1 1"]
		"hue 0.875" [color = ".875 1 1"]
		"hue 0.916" -- "dark hue 0.916"
		"hue 0.916" [color = ".916 1 1"]
		"hue 0.958" [color = ".958 1 1"]
		edge [len = 1]
		"hue 0.000" -- "hue 0.041" -- "hue 0.083" -- "hue 0.125" -- "hue 0.166" -- "hue 0.208"
		"hue 0.208" -- "hue 0.250" -- "hue 0.291" -- "hue 0.333" -- "hue 0.375" -- "hue 0.416"
		"hue 0.416" -- "hue 0.458" -- "hue 0.500" --"hue 0.541" -- "hue 0.583" -- "hue 0.625"
		"hue 0.625" -- "hue 0.666" -- "hue 0.708" -- "hue 0.750" -- "hue 0.791" -- "hue 0.833"
		"hue 0.833" -- "hue 0.875" -- "hue 0.916" -- "hue 0.958" -- "hue 0.000"
	}
	subgraph Main_colors {
		node [width = 2 fontsize = 20]
		red [fillcolor = red fontcolor = white]
		orangered [fillcolor = orangered]
		orange [fillcolor = orange]
		gold [fillcolor = gold]
		yellow [fillcolor = yellow]
		yellowgreen [fillcolor = yellowgreen]
		deeppink [fillcolor = deeppink fontcolor = white]
		fuchsia [label = "fuchsia\nmagenta" fillcolor = fuchsia fontcolor = white]
		purple [fillcolor = purple fontcolor = white]
		blue [fillcolor = blue fontcolor = white]
		cornflowerblue [fillcolor = cornflowerblue]
		deepskyblue [fillcolor = deepskyblue]
		aqua [fillcolor = aqua label = "aqua\ncyan"]
		springgreen [fillcolor = springgreen]
		green [fillcolor = green]
		purple -- fuchsia -- deeppink -- red
		cornflowerblue -- blue -- purple
		cornflowerblue -- deepskyblue -- aqua [len = 1.7]
		aqua -- springgreen -- green -- yellowgreen -- yellow
		yellow -- gold -- orange -- orangered -- red [len = 1.6]
		orange -- "hue 0.083"
		deeppink -- "hue 0.916"
		deeppink -- "hue 0.875"
		red -- "hue 0.000"
		yellowgreen -- "hue 0.250"
		blue -- "hue 0.666"
		yellow -- "hue 0.166"
		gold -- "hue 0.125"
		green -- "hue 0.333"
		springgreen -- "hue 0.416"
		aqua -- "hue 0.500"
		cornflowerblue -- "hue 0.583"
		deepskyblue -- "hue 0.541"
		purple -- "hue 0.791"
		purple -- "hue 0.750"
		fuchsia -- "hue 0.833"
	}
	subgraph Light_colors {
		node [width = 2 fontsize = 20]
		node [shape = circle width = 1.8]
		edge [len = 2.1]
		pink [fillcolor = pink]
		pink -- red
		lightyellow [fillcolor = lightyellow]
		lightyellow -- yellow
		mediumpurple [fillcolor = mediumpurple]
		mediumpurple -- purple
		violet [fillcolor = violet]
		violet -- fuchsia
		hotpink [fillcolor = hotpink]
		hotpink -- deeppink
		"light hue 0.250" [color = ".250 .2 1"]
		"light hue 0.250" -- yellowgreen
		lightcyan [fillcolor = lightcyan]
		lightcyan -- aqua
		lightslateblue [fillcolor = lightslateblue]
		lightslateblue -- blue
		lightgreen [fillcolor = lightgreen]
		lightgreen -- green
		lightskyblue [fillcolor = lightskyblue]
		lightskyblue -- deepskyblue
		peachpuff [fillcolor = peachpuff]
		peachpuff -- orange
		"light hue 0.416" [color = ".416 .2 1"]
		"light hue 0.416" -- springgreen
	}
	subgraph Tints {
		node [width = 1]
		edge [len = 2.4]
		"hue 0 tint" -- pink
		"hue 0 tint" [color = "0 .1 1"]
		"hue 0.041 tint" [color = ".041 .1 1"]
		"hue 0.083 tint" -- peachpuff
		"hue 0.083 tint" [color = ".083 .1 1"]
		"hue 0.125 tint" [color = ".125 .1 1"]
		"hue 0.166 tint" -- lightyellow
		"hue 0.166 tint" [color = ".166 .1 1"]
		"hue 0.208 tint" [color = ".208 .1 1"]
		"hue 0.250 tint" -- "light hue 0.250"
		"hue 0.250 tint" [color = ".250 .1 1"]
		"hue 0.291 tint" [color = ".291 .1 1"]
		"hue 0.333 tint" -- lightgreen
		"hue 0.333 tint" [color = ".333 .1 1"]
		"hue 0.375 tint" [color = ".375 .1 1"]
		"hue 0.416 tint" -- "light hue 0.416"
		"hue 0.416 tint" [color = ".416 .1 1"]
		"hue 0.458 tint" [color = ".458 .1 1"]
		"hue 0.5 tint" -- lightcyan
		"hue 0.5 tint" [color = ".5 .1 1"]
		"hue 0.541 tint" -- lightskyblue
		"hue 0.541 tint" [color = ".541 .1 1"]
		"hue 0.583 tint" [color = ".583 .1 1"]
		"hue 0.625 tint" [color = ".625 .1 1"]
		"hue 0.666 tint" -- lightslateblue
		"hue 0.666 tint" [color = ".666 .1 1"]
		"hue 0.708 tint" [color = ".708 .1 1"]
		"hue 0.750 tint" -- mediumpurple
		"hue 0.750 tint" [color = ".750 .1 1"]
		"hue 0.791 tint" [color = ".791 .1 1"]
		"hue 0.833 tint" -- violet
		"hue 0.833 tint" [color = ".833 .1 1"]
		"hue 0.875 tint" [color = ".875 .1 1"]
		"hue 0.916 tint" -- hotpink
		"hue 0.916 tint" [color = ".916 .1 1"]
		"hue 0.958 tint" [color = ".958 .1 1"]
		edge [len = 2]
		"hue 0 tint" -- "hue 0.041 tint" -- "hue 0.083 tint" -- "hue 0.125 tint" -- "hue 0.166 tint" -- "hue 0.208 tint"
		"hue 0.208 tint" -- "hue 0.250 tint" -- "hue 0.291 tint" -- "hue 0.333 tint" -- "hue 0.375 tint" -- "hue 0.416 tint"
		"hue 0.416 tint" -- "hue 0.458 tint" -- "hue 0.5 tint" --"hue 0.541 tint" -- "hue 0.583 tint" -- "hue 0.625 tint"
		"hue 0.625 tint" -- "hue 0.666 tint" -- "hue 0.708 tint" -- "hue 0.750 tint" -- "hue 0.791 tint" -- "hue 0.833 tint"
		"hue 0.833 tint" -- "hue 0.875 tint" -- "hue 0.916 tint" -- "hue 0.958 tint" -- "hue 0 tint"
	}
	// © 2022 Costa Shulyupin, licensed under EPL
}
```

### Grid

```dot
graph grid
{
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	layout=dot
	label="grid"
	labelloc = "t"
	node [shape=plaintext]
	// arbitrary path on rigid grid
	A0 -- B1 -- C2 -- D3 -- E4 -- F5 -- G6 -- H7
	H0 -- G1 -- F2 -- E3 -- D4 -- C5 -- B6 -- A7

	edge [weight=1000 style=dashed color=dimgrey]

	// uncomment to hide the grid
	//edge [style=invis]

	A0 -- A1 -- A2 -- A3 -- A4 -- A5 -- A6 -- A7
	B0 -- B1 -- B2 -- B3 -- B4 -- B5 -- B6 -- B7
	C0 -- C1 -- C2 -- C3 -- C4 -- C5 -- C6 -- C7
	D0 -- D1 -- D2 -- D3 -- D4 -- D5 -- D6 -- D7
	E0 -- E1 -- E2 -- E3 -- E4 -- E5 -- E6 -- E7
	F0 -- F1 -- F2 -- F3 -- F4 -- F5 -- F6 -- F7
	G0 -- G1 -- G2 -- G3 -- G4 -- G5 -- G6 -- G7
	H0 -- H1 -- H2 -- H3 -- H4 -- H5 -- H6 -- H7

	rank=same {A0 -- B0 -- C0 -- D0 -- E0 -- F0 -- G0 -- H0}
	rank=same {A1 -- B1 -- C1 -- D1 -- E1 -- F1 -- G1 -- H1}
	rank=same {A2 -- B2 -- C2 -- D2 -- E2 -- F2 -- G2 -- H2}
	rank=same {A3 -- B3 -- C3 -- D3 -- E3 -- F3 -- G3 -- H3}
	rank=same {A4 -- B4 -- C4 -- D4 -- E4 -- F4 -- G4 -- H4}
	rank=same {A5 -- B5 -- C5 -- D5 -- E5 -- F5 -- G5 -- H5}
	rank=same {A6 -- B6 -- C6 -- D6 -- E6 -- F6 -- G6 -- H6}
	rank=same {A7 -- B7 -- C7 -- D7 -- E7 -- F7 -- G7 -- H7}
}
// grid.dot by Costa Shulyupin
```

### Mindmap

```dot
graph happiness {
	labelloc="t"
	label="Mind map of Happiness.\nTwopi radial graph."
	fontname="URW Chancery L, Apple Chancery, Comic Sans MS, cursive"
	layout=twopi; graph [ranksep=2];
	edge [penwidth=5 color="#f0f0ff"]
	node [fontname="URW Chancery L, Apple Chancery, Comic Sans MS, cursive"]
	node [style="filled" penwidth=0 fillcolor="#f0f0ffA0" fontcolor=indigo]
	Happiness [fontsize=50 fontcolor=red URL="https://en.wikipedia.org/wiki/Category:Happiness"]
	node [fontsize=40]
	Happiness -- {
		Peace
		Love
		Soul
		Mind
		Life
		Health
	}
	Life [fontcolor=seagreen]
	Health [fontcolor=mediumvioletred]
	node [fontsize=25]
	Love [fontcolor=orchid URL="https://en.wikipedia.org/wiki/Category:Love"]
	Love -- {
		Giving
		People
		Beauty
	}
	Success [fontcolor=goldenrod]
	Life -- {
		Nature
		Wellbeing
		Success
	}
	Peace [URL="https://en.wikipedia.org/wiki/Category:Peace"]
	Peace -- {
		Connection
		Relationship
		Caring
	}
	Health -- {
		Body
		Recreation
	}
	Mind [URL="https://en.wikipedia.org/wiki/Category:Mind"]
	Mind -- {
		Cognition
		Consciousness
		Intelligence
	}
	Soul [URL="https://en.wikipedia.org/wiki/Soul"]
	Soul -- {
		Emotions
		Self
		Meditation
	}
	node [fontsize=""]
	Beauty -- {
		Esthetics
		Art
	}
	People -- {
		Family
		Partner
		Hug
	}
	Giving -- {
		Feelings
		Support
	}
	Self -- {
		Delight
		Joy
		Expression 
	}
	Success -- {
		Creation
		Profit
		Win
		Career
	}
	Recreation -- {
		Leisure
		Sleep
	}
	Emotions [URL="https://en.wikipedia.org/wiki/Soul"]
	Emotions -- {
		Positiveness Tranquility
	}
	Self -- Emotions [weight=10 penwidth=1 style=dotted constraint=false]
	Body -- {
		Medicine Exercises Nutrition Water Heart
	}
	Wellbeing -- {
		Home Work Finance Clothes Transport
	}
	Relationship -- {
		Friends Community Society
	}
	Connection -- {
		Acceptance
		Forgiveness
		Gratitude
		Agreement
	}
	Caring -- {
		Respect
		Empathy
		Help
	}
	Consciousness -- {
		Awareness
	}
	Meditation -- {
		Contemplation Breath
	}
	Cognition -- {
		Imagination
		Perception
		Thinking
		Understanding
		Memory
	}
	Intelligence -- {
		Learning
		Experiment
		Education
	}
	Nature -- {
		Ocean
		Forest
		Pets
		Wildlife
	}
	c [label="© 2020-2022 Costa Shulyupin" fontsize=12 shape=plain style="" fontcolor=gray]
}
```

### UML Class diagram demo

```dot
digraph UML_Class_diagram {
	graph [
		label="UML Class diagram demo"
		labelloc="t"
		fontname="Helvetica,Arial,sans-serif"
	]
	node [
		fontname="Helvetica,Arial,sans-serif"
		shape=record
		style=filled
		fillcolor=gray95
	]
	edge [fontname="Helvetica,Arial,sans-serif"]
	edge [arrowhead=vee style=dashed]
	Client -> Interface1 [label=dependency]
	Client -> Interface2

	edge [dir=back arrowtail=empty style=""]
	Interface1 -> Class1 [xlabel=inheritance]
	Interface2 -> Class1 [dir=none]
	Interface2 [label="" xlabel="Simple\ninterface" shape=circle]

	Interface1[label = <{<b>«interface» I/O</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	Class1[label = <{<b>I/O class</b> | + property<br align="left"/>...<br align="left"/>|+ method<br align="left"/>...<br align="left"/>}>]
	edge [dir=back arrowtail=empty style=dashed]
	Class1 -> System_1 [label=implementation]
	System_1 [
		shape=plain
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>System</b> </td> </tr>
			<tr> <td>
				<table border="0" cellborder="0" cellspacing="0" >
					<tr> <td align="left" >+ property</td> </tr>
					<tr> <td port="ss1" align="left" >- Subsystem 1</td> </tr>
					<tr> <td port="ss2" align="left" >- Subsystem 2</td> </tr>
					<tr> <td port="ss3" align="left" >- Subsystem 3</td> </tr>
					<tr> <td align="left">...</td> </tr>
				</table>
			</td> </tr>
			<tr> <td align="left">+ method<br/>...<br align="left"/></td> </tr>
		</table>>
	]

	edge [dir=back arrowtail=diamond]
	System_1:ss1 -> Subsystem_1 [xlabel="composition"]

	Subsystem_1 [
		shape=plain
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>Subsystem 1</b> </td> </tr>
			<tr> <td>
				<table border="0" cellborder="0" cellspacing="0" >
					<tr> <td align="left">+ property</td> </tr>
					<tr> <td align="left" port="r1">- resource</td> </tr>
					<tr> <td align="left">...</td> </tr>
				</table>
				</td> </tr>
			<tr> <td align="left">
				+ method<br/>
				...<br align="left"/>
			</td> </tr>
		</table>>
	]
	Subsystem_2 [
		shape=plain
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>Subsystem 2</b> </td> </tr>
			<tr> <td>
				<table align="left" border="0" cellborder="0" cellspacing="0" >
					<tr> <td align="left">+ property</td> </tr>
					<tr> <td align="left" port="r1">- resource</td> </tr>
					<tr> <td align="left">...</td> </tr>
				</table>
				</td> </tr>
			<tr> <td align="left">
				+ method<br/>
				...<br align="left"/>
			</td> </tr>
		</table>>
	]
	Subsystem_3 [
		shape=plain
		label=<<table border="0" cellborder="1" cellspacing="0" cellpadding="4">
			<tr> <td> <b>Subsystem 3</b> </td> </tr>
			<tr> <td>
				<table border="0" cellborder="0" cellspacing="0" >
					<tr> <td align="left">+ property</td> </tr>
					<tr> <td align="left" port="r1">- resource</td> </tr>
					<tr> <td align="left">...</td> </tr>
				</table>
				</td> </tr>
			<tr> <td align="left">
				+ method<br/>
				...<br align="left"/>
			</td> </tr>
		</table>>
	]
	System_1:ss2 -> Subsystem_2;
	System_1:ss3 -> Subsystem_3;

	edge [xdir=back arrowtail=odiamond]
	Subsystem_1:r1 -> "Shared resource" [label=aggregation]
	Subsystem_2:r1 -> "Shared resource"
	Subsystem_3:r1 -> "Shared resource"
	"Shared resource" [
		label = <{
			<b>Shared resource</b>
			|
				+ property<br align="left"/>
				...<br align="left"/>
			|
				+ method<br align="left"/>
				...<br align="left"/>
			}>
	]
}
```

