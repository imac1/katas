// function solution(number) {
// 	var sum = 0;

// 	if (number < 0) {
// 		console.log("number cannot be less than zero");
// 	} else {
// 		for (let i = 1; i < number; i++) {
// 			if (i % 5 === 0 || i % 3 === 0) {
// 				sum += i;
// 			}
// 		}
// 	}
// 	return sum;
// }

// function createPhoneNumber(numbers) {
// 	let prefix = "";
// 	let body = "";
// 	let ending = "";
// 	prefix = numbers.slice(0, 3).join("");
// 	body = numbers.slice(3, 6).join("");
// 	ending = numbers.slice(6, numbers.length).join("");
// 	return `"(${prefix}) ${body}-${ending}"`;
// }
// console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

// function deleteNth(arr, n) {
// 	// ...
// 	const entries = new Map(arr);

// 	const obj = Object.fromEntries(entries);
// 	console.log(obj);

// 	a = [];
// 	howMuch = [];
// 	for (let i = 0; i < arr.length; i++) {
// 		howMuch[arr[i]] = n;
// 	}
// 	console.log(howMuch);

// 	for (let i = 0; i < arr.length; i++) {
// 		if (howMuch[arr[i]] > 0) {
// 			a.push(arr[i]);
// 			howMuch[arr[i]]--;
// 		}
// 	}

// 	return a;
// }

// function findSmallestInt(args) {
// 	// let min = 0
// 	// let max = 0
// 	args.sort((min, max) => min - max);
// 	return args[0];
// }

// function order(words) {

// 	return words.split(' ').sort((a, b) => a.match(/\d/g) - b.match(/\d/g));

// }

// function high(x){
// 	alphabet = 'abcdefghijklmnopqrstuvwxz'

// 	// letter_value = alphabet.indexOf(letter)
// 	wordArr = []
// 	scoreArr = []
// 	const arrOfWords = x.split(' ').forEach(element => {
// 		let word = element.split("")
// 		wordArr.push(word)

// 	});

// 	for(let i = 0; i < wordArr.length; i++){
// 		let v = wordArr[i]
// 		let scores = v.reduce((a, b ) => a += alphabet.indexOf(b) + 1, 0)
// 		console.log(scores)
// 		scoreArr.push(scores)

// 	}

// 	console.log(scoreArr)

// 	console.log([...new Set(
// 		scoreArr.filter((value, index, self) => self.indexOf(value) !== index,

// 		console.log('me')))]
// 	  );

// 	let max = Math.max(...scoreArr)
// 	console.log(max)
// 	// console.log(Math.max(...scoreArr))
// 	maxIndex = scoreArr.indexOf(max)
// 	firstMaxIndex = scoreArr.findIndex(el => el === max)
// 	console.log(maxIndex)

// 	if (firstMaxIndex !== -1){
// 		return x.split(' ')[firstMaxIndex]
// 	  } else {
// 			return x.split(' ')[maxIndex]
// 	  }

// return x.split(' ')[maxIndex]

//   }
//   console.log(high("laguqwzloqpic wmjbwtyfoayjp qbuzykjjfgrki kcvyturnknhgv"))

// function diamond(n) {
// 	// if (n % 2 === 0) {
// 	// 	return null;
// 	// } else {
// 		// for (let i = 1; i < n; i++) {
// 		// 	let str = ' '.repeat(n - i);
// 		// 	let str2 = '*'.repeat(n-2*Math.abs((n-2*i-1)/2));
// 		// 	console.log(str + str2 + str);
// 		//  }
// 		// //  for (let i = 1; i < n-1; i++) {
// 		// // 	let str2 = '*'.repeat(i*2 - 1);
// 		// // 	let str = ' '.repeat(n - i);

// 		// // 	console.log(str + str2 + str);
// 		// //  }

// // Upside pyramid
// // for (let i = 1; i <= n; i++) {
// //   // printing spaces
// //   for (let j = 1; j <= n - i; j++) {
// //     process.stdout.write(' ')
// //   }
// //   // printing star
// //   for (let k = 0; k < 2 * i - 1; k++) {
// //     process.stdout.write('*')
// //   }
// //   console.log();
// // }

// // // downside pyramid
// // for (let i = 1; i <= n - 1; i++) {
// //   // printing spaces
// //   for (let j = 0; j < i; j++) {
// //      process.stdout.write(' ');
// //   }
// //   // printing star
// //   for (let k = (n - i) * 2 - 1; k > 0; k--) {
// //     process.stdout.write('*');
// //   }
// //   console.log();
// // }

// // 	}

// if (n % 2 == 0 || n < 3) return null;

//   let diamond = "";

//   let middle = (n + 1) / 2; // diamond center
//   console.log(middle)

//   for (let i = 1; i <= n; i++) {

//     let deviation = Math.abs(middle - i);
//     console.log(deviation)
//     diamond += " ".repeat(deviation);
//     diamond += "*".repeat(n - (deviation * 2)) + "\n";

//   }

//   return diamond;
// }

// console.log(diamond(3));

// function pattern(n) {
// 	var output = "";
// 	//being coder
// 	if (n === 1) {
// 		return (output = "1");
// 	} else {
// 		for (let i = 2; i <= n; i++) {
// 			output += `\n1${"*".repeat(i - 1)}${i}`;
// 		}
// 	}

// 	return "1" + "\n" + output;
// }

// console.log(pattern(2));
// const delayedWelcome = name => {setTimeout(() => {
//     console.log(`Welcome ${name}`)
// }, 2000);
// };
// delayedWelcome("Sam");
// delayedWelcome("Alex");

// const sumAverage = (arr) => {
// 	let result;
// 	let sums = []
// 	// Your code here
// 	 arr.forEach(element => {
// 		//  element.reduce((sum, acc) =>  sum += acc, 0)
// 		console.log(element)
// 		let sum = element.reduce((sum, acc) =>  sum += acc, 0)
// 		sums.push(sum/element.length)

// 	});
// 	result = sums.reduce((s, ac) => s += ac, 0)

// 	return Math.floor(result);
//   }
//   console.log(sumAverage([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]))

// function maxTriSum(numbers){
// 	//your code here
// 	let uniqueItems = [...new Set(numbers)]
// 	uniqueItems.sort((a,b) => {
// 		if(a > b) return 1;
// 		if(a < b) return -1;
// 		return 0;
// 	})
// 	let sliced = uniqueItems.slice(uniqueItems.length-3, uniqueItems.length)
// 	console.log(sliced)
// 	return sliced.reduce((sum, acc) => sum += acc, 0)
//   }
//   console.log(maxTriSum([2,9,13,10,5,2,9,5]))

// function add() {

// 	arr= [...arguments]
// return arr.reduce((a, b) => a + b, 0)
// }

// function defaultArguments(func, params) {
// 	// TODO: Program me

// 	console.log(arguments)
// 	console.log(arguments[0])
// 	console.log(arguments[1])
// 	const {a, b} = params
// 	// console.log( 'first add ' + (a + b))
// 	// console.log('func ' + (func+ a + b))
// 	console.log('add ' + add())
// 	// func = () => {
// 	// 	console.log(arguments)

// 	// }
// 	console.log('func'  + func())

//   }
// console.log(defaultArguments(add(3)))

// function validParentheses(parens) {
// 	// your code here ..
// 	arr = [...parens];
// 	stack = [];

// 	for (let i = 0; i < arr.length; i++) {
// 		let lastBracket = stack[stack.length - 1];
// 		if (arr[i] == "(") {
// 			stack.push(arr[i]);
// 		} else if ((lastBracket === "(" && arr[i] === ")")) {
// 			stack.pop();
// 		} else {
// 			return false;
// 		}
// 	}
// 	return stack.length ? false : true;
// }
// console.log(validParentheses("(())("));
// var maxSequence = function(arr){
// 	if (arr.length === 0){
// 		return 0
// 	  } else if (arr.length === 1){
// 		return arr[0]
// 	  } else {
// 		 let max_so_far = arr[0];
// 	  let curr_max = arr[0];

// 	  for (let i = 1; i < arr.length; i++)
// 	  {
// 		  curr_max = Math.max(arr[i], curr_max+arr[i]);
// 		  max_so_far = Math.max(max_so_far, curr_max);
// 	  }
// 	  if (max_so_far < 0){
// 		  return 0
// 	  } else

// 	return max_so_far;

// 	  }
//   }
//   console.log(maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))

// function incrementString (strng) {
// 	// return incrementedString

// 	lastNumber = strng[strng.length-1]
// 	l = parseInt(lastNumber);
// 	if (isNaN(l)){
// 		return strng + 1;
// 	} else {
// 		s = strng.slice(strng.length-3, strng.length)
// 		console.log(s)
// 		fisrtS = parseInt(s[0])
// 		secondS = parseInt(s[1, 2])
// 		if ( fisrtS == 0 &&  secondS == 9) {
// 			return strng.slice(0, strng.length-3) + 100
// 		} else if (isNaN(fisrtS) && secondS == 9){
// 		return strng.slice(0, strng.length-2) + 100

// 		} else if(parseInt(secondS) == 0){
// 			return strng.slice(0, strng.length-1) + 1
// 		}

// 		else {
// 			return s + (l + 1)
// 		}
// 	}

//   }
//   console.log(incrementString('fo001'))

// function nthEven(n) {
// 	// your code here
// return (n*2) -2
// }
// console.log(nthEven(2))

// function sortByLength (array) {
// 	arr =[]
// 	// Return an array containing the same strings, ordered from shortest to longest

// array.sort((a,b) => a.length - b.length);
// 	return array
//   };
//   console.log(sortByLength(["", "Moderately", "Brains", "Pizza"]))
// function isSortedAndHow(array) {
	
// 	const asc = array.slice().sort((a, b)=> a - b)
// 	console.log(asc)
// 	for(let i=0; i<=array.length; i++) {

// 		if(array[i] === asc[i]) {
// 			console.log('array' + array[i])
// 			console.log(asc[i])
// 			return 'asc';
// 		}
// 		else {
// 			return 'des';
// 		}
// 	}
// }
  
//   console.log(isSortedAndHow([3,1,2]))
// function solution(numbers){
// 	arr = []
// 	numbers.sort((a, b) => a - b)
// 	for (let i = 0; i < numbers.length; i++){
// 	  let temp = numbers[i+1] - numbers[i]
// 	  arr.push(temp)
// 	}
// 	const newArray = arr.filter(function (value) {
// 		return !Number.isNaN(value);
// 	});
// 	  return  Math.max(...newArray)
  
// }
// console.log(solution([13,10,2,9,5]))

function apparently(string) {
	modifiedString = string.split(' ')
	// console.log(modifiedString)
	for (let i = 0; i <= modifiedString.length; i++){
		if (modifiedString[i] === 'and' && modifiedString[i + 1] != 'apparently'){
		 modifiedString.splice(i + 1, 0, 'apparently')
		} else if (modifiedString[i] === 'but' && modifiedString[i + 1] != 'apparently'){
			modifiedString.splice(i + 1, 0, 'apparently')
		}
		
	}
	return modifiedString.join(' ')
  }

  console.log(apparently(`and and but but`))