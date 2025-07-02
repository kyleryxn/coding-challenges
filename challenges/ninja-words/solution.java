import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NinjaWords {

    public int countNinjaWords(List<String> targetWords, String sentence) {
        if (targetWords.isEmpty() || sentence.isEmpty() || sentence.isBlank()) {
            return 0;
        }

        sentence = sentence.toLowerCase();
        int score = 0;

        // Eliminate matching words that are not ninja words
        for (String targetWord : targetWords) {
            String word = targetWord.toLowerCase();
            sentence = sentence.replace(word, "");
        }

        //sentence = sentence.replace(" ", "");
        System.out.println(sentence);

        for (String targetWord : targetWords) {
            String word = targetWord.toLowerCase();
            String pattern = "(?i)\\b[a-z*\\s]{2,}\\b";
            Pattern p = Pattern.compile(pattern);
            Matcher matcher = p.matcher(sentence);

            while (matcher.find()) {
                String group = matcher.group();
                int start = matcher.start();
                int end = matcher.end();
                System.out.println(group + " " + start + " " + end);
            }
        }

        return score;
    }
}
