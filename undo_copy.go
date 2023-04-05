package main

import (
	"fmt"
	"os"
	path "path/filepath"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	source := "/tmp/test/source" // os.Argv[1]
	target := "/tmp/test/target" // os.Argv[1]
	files, err := os.ReadDir(source)
	check(err)

	for _, file := range files {
		to_del := path.Join(target, file.Name())
		if file.IsDir() {
			fmt.Printf("Removing Directory: %v\n", to_del)
			err := os.RemoveAll(to_del)
			check(err)
		} else {
			fmt.Printf("Removing File: %v\n", to_del)
			err := os.Remove(to_del)
			check(err)
		}

	}
}