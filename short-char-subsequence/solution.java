
import java.util.*;
import java.util.stream.Collectors;
import org.testng.Assert;
import org.testng.annotations.Test;

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

    public static SubSequence solution(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        if(args.length < 2){
            System.out.println("error args len < 2");
            return null;
        }
        String[] completeList = args[0].replaceAll("[^a-zA-Z\\s+]", "").split(" ");
        int patternSize = Integer.parseInt(args[1]);
        if(args.length < 2 + patternSize){
            System.out.println("error args len < 2 + pattern");
            return null;
        }
        String[] pattern = Arrays.copyOfRange(args, 2, 2 + patternSize);

        SubSequence smallestSubsequence = getSmallestSubsequence(completeList,0, pattern);
        //System.out.println("start "+ smallestSubsequence.start + " end: " + smallestSubsequence.end );
        if(smallestSubsequence.end < 0){
            return null;
        }
        String[] solution = Arrays.copyOfRange(completeList, smallestSubsequence.start, smallestSubsequence.end + 1);
        System.out.println(concatenateArray(solution));
        return smallestSubsequence;
    }
    private static String concatenateArray(String[] array) {
        String result = "";
        for(int i =0; i < array.length; i++){
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

        /*debug
        String[] thisSubsequenceArray = Arrays.copyOfRange(completeList, start, end + 1);
        System.out.println("thisSubsequence: "+ concatenateArray(thisSubsequenceArray));
        String[] nextSmallestSubsequenceArray = Arrays.copyOfRange(completeList, start, end + 1);
        System.out.println("nextSmallestSubsequence: "+ concatenateArray(nextSmallestSubsequenceArray));
        */
        if(nextSmallestSubsequence.end < 0){
            return thisSubsequence;
        }
        if (thisSubsequence.length() < nextSmallestSubsequence.length()){
            return thisSubsequence;
        }
        return nextSmallestSubsequence;
    }


    private static int getSubsequenceEnd(String[] completeList, int start, String[] pattern) {
        List<String> patternList = new ArrayList<>(Arrays.asList(pattern));
        for (int i = start; i < completeList.length; i++) {
            patternList.remove(completeList[i]);
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
    public void testMain1() {
        String[] args = {"b a d e a e b c a a e", "4","a", "a", "b", "c"};
        ShorterCharSubsequence.solution(args);
        SubSequence result = ShorterCharSubsequence.solution(args);
        Assert.assertEquals(result.start, 6);
        Assert.assertEquals(result.end, 9);
    }

    @Test
    public void testMain2() {
        String[] args = {"e a a c b e a e d a b", "4","a", "a", "b", "c"};
        SubSequence result = ShorterCharSubsequence.solution(args);
        Assert.assertEquals(result.start, 1);
        Assert.assertEquals(result.end, 4);
    }

}







