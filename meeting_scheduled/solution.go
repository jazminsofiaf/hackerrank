package meeting_scheduled

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
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

const YYYY = 2009
const MM = time.November
const dd = 28
const sec = 00
const nsec = 00
const layout = "15 04"

//solution returns start and end of substring
func solution(arguments []string) [][4]int {
	result := make([][4]int, 0)
	if len(arguments) < 1 {
		log.Println("error args len < 1")
		return result
	}
	line1 := strings.Split(arguments[0], " ")
	if len(line1) < 2 {
		log.Println("len(line1) < 2")
		return result
	}
	size, err := strconv.Atoi(line1[0])
	if err != nil {
		log.Println("error parsing size")
		return result
	}
	k, err := strconv.Atoi(line1[1])
	if err != nil {
		log.Println("error parsing k")
		return result
	}

	busySlots := make([]slot, 0)
	for i := 1; i < size+1; i++ {
		line := strings.Split(arguments[i], " ")
		if len(line) < 4 {
			log.Println("len(line) < 4")
			return result
		}
		hourStart, err := strconv.Atoi(line[0])
		if err != nil {
			log.Println("error parsing hour")
			return result
		}
		minStart, err := strconv.Atoi(line[1])
		if err != nil {
			log.Println("error parsing min")
			return result
		}

		hourEnd, err := strconv.Atoi(line[2])
		if err != nil {
			log.Println("error parsing hour")
			return result
		}
		minEnd, err := strconv.Atoi(line[3])
		if err != nil {
			log.Println("error parsing min")
			return result
		}
		start := time.Date(YYYY, MM, dd, hourStart, minStart, sec, nsec, time.UTC)
		end := time.Date(YYYY, MM, dd, hourEnd, minEnd, sec, nsec, time.UTC)
		s := slot{start, end}
		busySlots = append(busySlots, s)
	}
	matchingSlots := getMatchingSlides(k, busySlots)
	for i := 0; i < len(matchingSlots); i++ {
		s := matchingSlots[i]
		fmt.Printf("%v %v\n", s.Init.Format(layout), s.Finish.Format(layout))
		result = append(result, [4]int{s.Init.Hour(), s.Init.Minute(), s.Finish.Hour(), s.Finish.Minute()})
	}
	return result
}

func getMatchingSlides(k int, busySlots []slot) []slot {
	freeSlots := make([]slot, 0)
	allDay := slot{
		Init:   time.Date(YYYY, MM, dd, 00, 00, sec, nsec, time.UTC),
		Finish: time.Date(YYYY, MM, dd+1, 00, 00, sec, nsec, time.UTC),
	}
	freeSlots = append(freeSlots, allDay)
	for i := 0; i < len(busySlots); i++ {
		newFreeSlots := make([]slot, 0)
		for j := 0; j < len(freeSlots); j++ {
			newFreeSlots = append(newFreeSlots, getFreeKMinSlot(k, freeSlots[j], busySlots[i])...)
		}
		freeSlots = newFreeSlots
	}
	return freeSlots
}

func getFreeKMinSlot(k int, freeSlot slot, busySlot slot) []slot {
	freeSlots := make([]slot, 0)

	freeSlotInit := freeSlot.Init
	freeSlotEnd := freeSlot.Finish
	busySlotInit := busySlot.Init
	busySlotEnd := busySlot.Finish
	if afterOrEquals(busySlotInit, freeSlotInit) && busySlotInit.Before(freeSlotEnd) {
		previousFreeSlot := busySlotInit.Sub(freeSlotInit)
		if previousFreeSlot.Minutes() >= float64(k) {
			freeSlots = append(freeSlots, slot{freeSlotInit, busySlotInit})
		}
	}
	if busySlotEnd.After(freeSlotInit) && busySlotEnd.Before(freeSlotEnd) {
		followingFreeSlot := freeSlotEnd.Sub(busySlotEnd)
		if followingFreeSlot.Minutes() >= float64(k) {
			freeSlots = append(freeSlots, slot{busySlotEnd, freeSlotEnd})
		}
	}
	if beforeOrEquals(busySlotEnd, freeSlotInit) || afterOrEquals(busySlotInit, freeSlotEnd) {
		//no intersection
		freeSlots = append(freeSlots, freeSlot)
	}
	return freeSlots
}
func afterOrEquals(d1 time.Time, d2 time.Time) bool {
	return d1.After(d2) || d1.Equal(d2)
}

func beforeOrEquals(d1 time.Time, d2 time.Time) bool {
	return d1.Before(d2) || d1.Equal(d2)
}

type slot struct {
	Init   time.Time
	Finish time.Time
}

// HH/mm 00 01  02.....58 59
//    00  X  X  X
//    01
//    ..
//    ..
//    22
//    23
