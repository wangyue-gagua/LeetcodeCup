// 请输出执行结果，例如1-2-3-4-5-6-7-8
// 1 8 3 7 4 2 6 5
console.log('1: script start')

setImmediate(function() {
  console.log('2: setTimeout')
}, 0)

Promise.resolve()
  .then(function() {
    console.log('3: promise1')
    process.nextTick(() => {
      console.log('4: nextTick in promise')
    })
    setTimeout(function() {
      console.log('5: setTimeout in promise')
    }, 0)
  })
  .then(function() {
    console.log('6: promise2')
  })

process.nextTick(() => {
  console.log('7: nextTick')
})

console.log('8: script end')

/* setImmediate(function(){
    console.log(1);
  },0);
  setTimeout(function(){
    console.log(2);
  },0);
  new Promise(function(resolve){
    console.log(3);
    resolve();
    console.log(4);
  }).then(function(){
    console.log(5);
  });
  console.log(6);
  process.nextTick(function(){
    console.log(7);
  });
  console.log(8); */