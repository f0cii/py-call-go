package main

/*
#include <stdlib.h>
#include "callback.h"
*/
import "C"
import (
	"log"
	"unsafe"
)

//export add
func add(left, right int) int {
	return left + right
}

//export hello
func hello(c *C.char) *C.char {
	_s := C.GoString(c)
	log.Printf("%v\n", _s)

	// 调用回调函数
	cStr := C.CString("Hello from Go!")
	defer C.free(unsafe.Pointer(cStr))

	C.doCallback(cStr)

	return C.CString("Hello: " + _s)
}

func main() {

}

// CGO_ENABLED=1
// go build -buildmode=c-shared -o py-call-go.so .
