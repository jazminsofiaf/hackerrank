package merge_lists

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	arguments := make([]string, 0)
	scanner := bufio.NewScanner(os.Stdin)
	if err := scanner.Err(); err != nil {
		log.Println(err)
		return
	}
	for scanner.Scan() {
		arguments = append(arguments, scanner.Text())
	}
	solution(arguments)
}

//solution returns start and end of substring
func solution(arguments []string) *node {
	var result *node
	if len(arguments) < 1 {
		log.Println("error args len < 1")
		return result
	}

	t, err := strconv.Atoi(arguments[0])
	if err != nil {
		log.Println("error parsing pattern size")
		return result
	}

	index := 1
	for i := 0; i < t; i++ {
		listASize, err := strconv.Atoi(arguments[index])
		index++
		if err != nil {
			log.Println("error parsing list a size")
		}
		listA := getLinkedList(arguments, index, listASize)

		index = index + listASize
		listBSize, err := strconv.Atoi(arguments[index])
		index++
		if err != nil {
			log.Println("error parsing list b size")
		}
		listB := getLinkedList(arguments, index, listBSize)
		mergedList := merge(listA, listB, nil, nil)
		result = mergedList
	}
	current := result
	for current != nil {
		println(current.Value)
		current = current.Next
	}
	return result
}

func getLinkedList(arguments []string, indexInit int, size int) *node {
	var list *node
	var previousNode *node
	index := indexInit
	for index < indexInit+size {
		val, err := strconv.Atoi(arguments[index])
		if err != nil {
			log.Println("error parsing list A size")
		}
		currentNode := node{val, nil}
		if previousNode != nil {
			previousNode.Next = &currentNode
		}
		if index == indexInit {
			list = &currentNode
		}
		index++
		previousNode = &currentNode
	}
	return list
}

type node struct {
	Value int
	Next  *node
}

func merge(a *node, b *node, merged *node, mergedHead *node) *node {
	if a == nil {
		merged.Next = b
		return mergedHead
	}
	if b == nil {
		merged.Next = a
		return mergedHead
	}
	if merged == nil {
		if a.Value < b.Value {
			merged = a
			return merge(a.Next, b, merged, merged)
		}
		merged = b
		return merge(a, b.Next, merged, merged)
	}

	if a.Value < b.Value {
		merged.Next = a
		return merge(a.Next, b, merged.Next, mergedHead)
	}
	merged.Next = b
	return merge(a, b.Next, merged.Next, mergedHead)

}
