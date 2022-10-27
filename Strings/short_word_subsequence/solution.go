package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
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
func solution(arguments []string) (int, int) {
	if len(arguments) < 2 {
		log.Println("error args len < 1")
		return -1, -1
	}
	paragraph := arguments[0]
	reg := regexp.MustCompile(`[^a-zA-Z\s+]`)
	paragraph = reg.ReplaceAllString(paragraph, "${1}")
	//log.Println("paragraph: " + paragraph)
	completeList := strings.Split(paragraph, " ")

	patternSize, err := strconv.Atoi(arguments[1])
	if err != nil {
		log.Println("error parsing pattern size")
		return -1, -1
	}
	if len(arguments) < 2+patternSize {
		log.Println("error args len < 2 + pattern size")
		return -1, -1
	}
	patternList := arguments[2:]
	if len(patternList) < 1 {
		log.Println("pattern list < 1")
		return -1, -1
	}
	start, end := getSmallestSubsequence(completeList, 0, patternList)
	if end < 0 {
		fmt.Println("NO SUBSEGMENT FOUND")
		return -1, -1
	}
	result := completeList[start : end+1]
	for i := 0; i < len(result); i++ {
		fmt.Printf("%s ", result[i])
	}
	return start, end
}

func getSmallestSubsequence(completeList []string, start int, patternList []string) (int, int) {
	if start > len(completeList)-1 {
		//log.Printf("start > len(completeList)-1")
		return -1, -1
	}
	end := getSubsequenceEnd(completeList, start, patternList)
	if end < start {
		//log.Printf("end < start")
		return -1, -1
	}
	/*
		log.Printf("this subsequence: ")
		result := completeList[start : end+1]
		for i := 0; i < len(result); i++ {
			log.Printf("{%s} ", result[i])
		}
	*/

	nextStart, nextEnd := getSmallestSubsequence(completeList, start+1, patternList)
	if nextEnd < 0 {
		return start, end
	}
	/*
		log.Printf("next subsequence: ")
		nextResult := completeList[nextStart : nextEnd+1]
		for i := 0; i < len(nextResult); i++ {
			log.Printf("{%s} ", nextResult[i])
		}
	*/

	if end-start < nextEnd-nextStart {
		return start, end
	}
	return nextStart, nextEnd

}

func getSubsequenceEnd(completeList []string, start int, patternSize []string) int {
	patterSet := toMap(patternSize)
	for i := start; i < len(completeList); i++ {
		delete(patterSet, strings.ToLower(completeList[i]))
		if len(patterSet) == 0 {
			return i
		}
	}
	return -1
}

func toMap(list []string) map[string]bool {
	mapSet := make(map[string]bool, 0)
	for i := 0; i < len(list); i++ {
		mapSet[strings.ToLower(list[i])] = true
	}
	return mapSet
}
