package blackjack
import (
	"fmt"
	"strings"
)

const ace = "ace"
const two = "two"

func getCardValue(card string) (int, int) {
	switch strings.ToLower(card) {
	case two:
		return 2, 2
	case "three":
		return 3, 3
	case "four":
		return 4, 4
	case "five":
		return 5, 5
	case "six":
		return 6, 6
	case "seven":
		return 7, 7
	case "eight":
		return 8, 8
	case "nine":
		return 9, 9
	case "ten":
		return 10, 10
	case "jack":
		return 10, 11
	case "queen":
		return 10, 12
	case "king":
		return 10, 13
	default:
		return 0, 0
	}
}

func blackjackHighest(strArr []string) string {
	if len(strArr) < 1 {
		return ""
	}
	highestCard := strArr[0]
	_, maxImportance := getCardValue(highestCard)
	var sum int
	var hasAnAce bool

	for _, card := range strArr {
		if strings.ToLower(card) == ace {
			hasAnAce = true
		} else {
			cardValue, hierarchy := getCardValue(card)
			sum += cardValue
			if hierarchy > maxImportance {
				highestCard = card
				maxImportance = hierarchy
			}
		}
	}
	if hasAnAce {
		if sum < 11 {
			sum += 11
			highestCard = "ace"
		} else {
			sum += 1
		}
	}
	result := "blackjack"
	if sum < 21 {
		result = "below"
	}
	if sum > 21 {
		result = "above"
	}
	return fmt.Sprintf("%s %s", result, highestCard)

}
