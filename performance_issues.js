/**
 * performance_issues.js - JavaScript code with performance problems
 */

// SYNTAX ERROR: Missing semicolon
var globalVariable = "Hello World"

function inefficientSearch(array, target) {
    // PERFORMANCE ERROR: Inefficient O(n²) search algorithm
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (array[i] === target && array[j] === target) {
                return i
            }
        }
    }
    return -1
}

function stringConcatenationLoop(items) {
    // PERFORMANCE ERROR: String concatenation in loop
    let result = ""
    for (let i = 0; i < items.length; i++) {
        result += items[i] + ", "  // SYNTAX ERROR: Missing semicolon
    }
    return result
}

// SYNTAX ERROR: Missing semicolon
function processLargeDataset(data) {
    let processed = []
    
    // PERFORMANCE ERROR: Nested loops with O(n³) complexity
    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data.length; j++) {
            for (let k = 0; k < data.length; k++) {
                processed.push(data[i] * data[j] * data[k])  // SYNTAX ERROR: Missing semicolon
            }
        }
    }
    
    return processed
}

// LOGIC ERROR: Infinite loop potential
function waitForCondition(condition) {
    while (true) {
        if (condition) {
            console.log("Condition met!")
            // Missing break statement - infinite loop!
        }
        // This could run forever
    }
}

// TODO: Optimize this function
// FIXME: Memory leak in this implementation
function memoryLeakDemo(size) {
    let largeArray = new Array(size).fill(0)
    // Array is never cleaned up
    return largeArray.length
}

// SYNTAX ERROR: Missing function parameter parentheses
function brokenFunction {
    return "This won't work"
}
