
import org.testng.Assert;
import org.testng.annotations.Test;
import java.util.*;
import java.util.stream.Collectors;
    


public class Solution {
    
    public static void main(String[] args){
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        List<String> argumentsList = new ArrayList<>();

        Scanner input = new Scanner(System.in);
        while (input.hasNext()) {
            argumentsList.add(input.nextLine());
        }

        String[] arguments = new String[argumentsList.size()];

        for (int i = 0; i < argumentsList.size(); i++)
            arguments[i] = argumentsList.get(i);

        solution(arguments);
    }

    public static SubSequence solution(String[] arguments) {
        if(arguments.length < 1){
            System.out.println("error args len < 1");
            return null;
        }
        String paragraph = arguments[0].replaceAll("[^a-zA-Z\\s+]", "");
        //System.out.println("paragraph: "+ paragraph);
        String[] completeList = paragraph.split(" ");
        int patternSize = Integer.parseInt(arguments[1]);
        if(arguments.length < 2 + patternSize){
            System.out.println("error args len < 2 + pattern");
            return null;
        }
        String[] pattern = Arrays.copyOfRange(arguments, 2, 2 + patternSize);
        if(pattern.length < 1){
            return null;
        }

        SubSequence smallestSubsequence =  getSmallestSubsequence(completeList, 0, pattern);
        //System.out.println("start "+ smallestSubsequence.start + " end: " + smallestSubsequence.end );
        if(smallestSubsequence.end < 0){
            System.out.println("NO SUBSEGMENT FOUND");
            return null;
        }
        String[] solution = Arrays.copyOfRange(completeList, smallestSubsequence.start, smallestSubsequence.end + 1);
        System.out.println(concatenateArray(solution));
        return smallestSubsequence;
    }
    private static String concatenateArray(String[] array) {
        String result = "";
        for(int i =0; i < array.length; i++){
            if(i == array.length){
                result = result + array[i];
                break;
            }
            result = result + array[i]+" ";
        }
        return result;
    }

    private static SubSequence getSmallestSubsequence(String[] completeList,int start, String[] pattern) {
        if(start > completeList.length - 1){
            return new SubSequence(-1,-1);
        }
        int end = getSubsequenceEnd(completeList, start, pattern);
        //pattern not found
        if(end < start){
            return new SubSequence(-1,-1);
        }
        SubSequence thisSubsequence = new SubSequence(start, end);
        SubSequence nextSmallestSubsequence = getSmallestSubsequence(completeList,start+1, pattern );

        /* debug
        String[] thisSubsequenceArray = Arrays.copyOfRange(completeList, start, end + 1);
        System.out.println("thisSubsequence: "+ concatenateArray(thisSubsequenceArray));
        String[] nextSmallestSubsequenceArray = Arrays.copyOfRange(completeList, start, end + 1);
        System.out.println("nextSmallestSubsequence: "+ concatenateArray(nextSmallestSubsequenceArray));
        */
        if(nextSmallestSubsequence.end == -1){
            return thisSubsequence;
        }
        if (thisSubsequence.length() < nextSmallestSubsequence.length()){
            return thisSubsequence;
        }
        return nextSmallestSubsequence;
    }


    private static int getSubsequenceEnd(String[] completeList, int start, String[] pattern) {
        //this is a set if the pattern words can be duplicated but we need to match them at least once
        //this should be a list if a specific frequency of each word is required
        Set<String> patternList = new HashSet<>(Arrays.asList(pattern)).stream().map(String::toLowerCase).collect(Collectors.toSet());
        for (int i = start; i < completeList.length; i++) {
            patternList.remove(completeList[i].toLowerCase());
            if (patternList.size() == 0) {
                return i;
            }
        }
        return -1;
    }

    public static class SubSequence{
        public int start;
        public int end;

        SubSequence(int start, int end){
            this.start = start;
            this.end = end;
        }

        public int length() {
            return end - start + 1;
        }
    }

    @Test
    public void test1() {
        String[] args = {"This is a test. This is a programming test. This is a programming test in any language.", "0"};
        SubSequence result = ShortestWordSubsequence.solution(args);
        Assert.assertEquals(result, null);
    }

    @Test
    public void test2() {
        String[] args = {"This is a test. This is a programming test. This is a programming test in any language","4","this","a","test","programming"};
        SubSequence result = ShortestWordSubsequence.solution(args);
        Assert.assertEquals(result.start, 9);
        Assert.assertEquals(result.end, 13);
    }

    @Test
    public void test3() {
        String[] args = {"thlojvep yetogrwlww rrsozup z nddd gyovqy bf mm nudobxuizx h bttaa fxqyo y mfefgz efhzliog steqob fklht rpg ecswbtpzrn hoz anlkjvtas xedtluu unv afs p dcfrksg xdaozfhvd gowfkvuvg d bxz pgiy ecswbtpzrn gbds dj sdvlnwz ntc rhbvna cc xiqi jo zvzd p wisocd juwcn wzsbmog qhpnchaf judwgz ehcui beacjlx mfefgz flp cshg a tjzl xpzkp bttaa einfepsew cajhc qll knxlq nitp ckwxkmmxr.", "43", "ntc", "sdvlnwz", "zvzd", "unv", "d", "bttaa", "mfefgz", "yetogrwlww", "nitp", "xiqi", "z", "nudobxuizx", "mfefgz", "cajhc", "ehcui", "einfepsew", "dcfrksg", "ecswbtpzrn", "mm", "ecswbtpzrn", "xpzkp", "steqob", "flp", "rpg", "p", "beacjlx", "ehcui", "xpzkp", "jo", "nudobxuizx", "sdvlnwz", "bttaa", "wisocd", "y", "gbds", "nudobxuizx", "bf", "juwcn", "bttaa", "rrsozup", "hoz", "fxqyo", "nudobxuizx"};
        SubSequence result = ShortestWordSubsequence.solution(args);
        Assert.assertEquals(result.start, 1);
        Assert.assertEquals(result.end, 60);
    }

    @Test
    public void test4() {
        String[] args = {"This is a test. This is a programming test. This is a programming test in any language","4","this","a","test","program"};
        SubSequence result = ShortestWordSubsequence.solution(args);
        Assert.assertEquals(result, null);
    }
}
    
    
    
    
    
    
    
    