# Typescript

# Setup. Compile & Run

```bash
$ npm i -D typescript       # Install typescript package in dev-dependencies.

$ npx tsc testing.ts        # Compile into javascript (Node package execute typescript compiler)

$ nodejs testing.js         # Run generated javaScript file
```

# Fetch

```
$ npm i -D node-fetch
```




# Basics

# Data Types

- number    - 64-bit float. no integers in javascript
- string    - sequence of unicode char
- boolean
- void      - represent non-returning functions
- null
- undefined

> Because javascript is only intepreted there are no type declarations. Variable types are infered from the assigned values.

# Variables

```ts
var name:string = ”jana”

var name = ”jana”
```

```ts
var global_num = 12          //global variable 
class Numbers { 
   num_val = 13;             //class variable 
   static sval = 10;         //static field 
   
   storeNum():void { 
      var local_num = 14;    //local variable 
   } 
} 
```

# Build-in Classes

Classes contain additional functionality.

## Numbers, Strings, Arrays

```ts
var var_name = new Number(value)

var str_name = new String(value)

var array_name[:datatype]           // Array declaration
array_name = [val1,val2,valn..]     // initialization

var tuple_name = [value1,value2,value3,…value n]    // Init tuple with mixed types

```

# Interface

Syntactical contract that an entity should conform to.

```ts
interface IPerson { 
   name:string, 
   address:string, 
   method: ()=>string 
} 
```

# Namespace

Logically group related code & multiple files.
In JavaScript variable declarations go into global scope and might overwrite each other.

```ts
// Create namespace with code inside
namespace SomeNameSpaceName { 
   export interface Example_interface {      }  
   export class Class_Name {      }  
} 

// Import interface into another namespace
SomeNameSpaceName.Class_Name;

// Import namespace from another Typescript file
/// <reference path = "SomeFileName.ts" />
```

# External modules

Load dependencies between multiple external js files.

```ts
//FileName : SomeInterface.ts 
export interface SomeInterface { 
   //code declarations 
}

// Import in another file
import someInterfaceRef = require(“./SomeInterface”);
import someClass        = require(“./SomeClass”);

// Compile with external modules
tsc --module amd TestShape.ts
```

# Ambient

Telling typescript that the actual source code lies elsewere.