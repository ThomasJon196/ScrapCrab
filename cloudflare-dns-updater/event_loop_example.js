// setTimeout sets a timeout on a given callback function.
// After timeout expiration the callback fuction is pushed into the Queue
// The Event-Loop continuously checks the queue and pushes finished tasks into the Call-Stack

const foo = () => console.log("First");
const bar = () => setTimeout(() => console.log("Second"), 500);
const baz = () => console.log("Third");

bar();
foo();
baz();