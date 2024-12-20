
# PlantUML Examples

## Sequence Diagram
```plantuml
@startuml
participant User
participant System
participant Database

User -> System: Request data
System -> Database: Query
Database --> System: Result set
System --> User: Display data
@enduml
```

## Use Case Diagram
```plantuml
@startuml
actor User
actor Admin
User --> (Login)
Admin --> (Manage Users)
(Login) --> (Dashboard)
@enduml
```

## Class Diagram
```plantuml
@startuml
class User {
  +String name
  +String email
  +void login()
  +void logout()
}

class Admin extends User {
  +void manageUsers()
}

User <|-- Admin
@enduml
```

## Object Diagram
```plantuml
@startuml
object User {
  name = "Alice"
  email = "alice@example.com"
}

object Admin {
  name = "Bob"
  email = "bob@example.com"
  role = "Admin"
}
@enduml
```

## Activity Diagram
```plantuml
@startuml
start
:User logs in;
if (Valid credentials?) then (yes)
  :Show dashboard;
else (no)
  :Show error;
endif
stop
@enduml
```

## Component Diagram
```plantuml
@startuml
package "Web Application" {
  [Frontend] --> [Backend]
  [Backend] --> [Database]
}
@enduml
```

## Deployment Diagram
```plantuml
@startuml
node "Client" {
  [Browser]
}
node "Server" {
  [Web Application]
}
[Browser] --> [Web Application]
@enduml
```

## State Diagram
```plantuml
@startuml
[*] --> LoggedOut
LoggedOut --> LoggedIn : Login
LoggedIn --> LoggedOut : Logout
@enduml
```

## Timing Diagram
```plantuml
@startuml
robust "Process" as P
concise "Thread" as T

@0
P is Active
T is Running

@100
P is Waiting
T is Suspended
@enduml
```

## JSON Diagram
```plantuml
@startjson
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": null
}
@endjson

```

## YAML Diagram
@startyaml
doe: "a deer, a female deer"
ray: "a drop of golden sun"
pi: 3.14159
xmas: true
french-hens: 3
calling-birds: 
	- huey
	- dewey
	- louie
	- fred
xmas-fifth-day: 
	calling-birds: four
	french-hens: 3
	golden-rings: 5
	partridges: 
		count: 1
		location: "a pear tree"
	turtle-doves: two
@endyaml

```

## EBNF Diagram
```plantuml
@startebnf
(* Example from §8.1 ISO-EBNF *)

h-tab = ? IS0 6429 character Horizontal Tabulation ? ;

new-line = { ? IS0 6429 character Carriage Return ? },
? IS0 6429 character Line Feed ?,
{ ? IS0 6429 character Carriage Return ? };

(* Other possible examples: *)
h-tab = ?Unicode U+0009?;
empty-special = ??;
@endebnf
```

## Regex Diagram
```plantuml
@startregex
title Regex example
/([a-zA-Z]+)\d+/
@enduml
```

## Nwdiag Diagram
```plantuml
@startuml
nwdiag {
  group {
    color = "#FFaaaa";
    web01;
    db01;
  }
  group {
    color = "#aaaaFF";
    web02;
    db02;
  }
  network dmz {
      address = "210.x.x.x/24"

      web01 [address = "210.x.x.1"];
      web02 [address = "210.x.x.2"];
  }
  network internal {
      address = "172.x.x.x/24";

      web01 [address = "172.x.x.1"];
      web02 [address = "172.x.x.2"];
      db01 ;
      db02 ;
  }
}
@enduml
```

## SDL Diagram
```plantuml
@startuml
start
if (condition A) then (yes)
  :Text 1;
elseif (condition B) then (yes)
  :Text 2;
  stop
(no) elseif (condition C) then (yes)
  :Text 3;
(no) elseif (condition D) then (yes)
  :Text 4;
else (nothing)
  :Text else;
endif
stop
@enduml

```

## WBS Diagram
```plantuml
@startwbs
* Project
** Task A
*** Subtask A1
*** Subtask A2
** Task B
@endwbs
```

## Mindmap Diagram
```plantuml
@startmindmap
* Root
** Branch A
*** Leaf A1
*** Leaf A2
** Branch B
*** Leaf B1
@endmindmap
```

## Entity Relationship Diagram
```plantuml
@startuml
entity User {
  *id
  *name
  *email
}
entity Order {
  *id
  *user_id
  *amount
}
User ||--o{ Order
@enduml
```

## Math Diagram
```doesntwork
@startuml
:<math>int_0^1f(x)dx</math>;
:<math>x^2+y_1+z_12^34</math>;
note right
Try also
<math>d/dxf(x)=lim_(h->0)(f(x+h)-f(x))/h</math>
<math>P(y|bb"x") or f(bb"x")+epsilon</math>
end note
@enduml

```

## C4 Diagram
```plantuml
@startuml
!include <C4/C4_Container>

Container(Browser, "Web Browser")
Container(WebApp, "Web Application")
ContainerDb(Database, "Database")

Browser -> WebApp: Uses
WebApp -> Database: Reads/Writes
@enduml
```

