package others;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WikipediaArticle {

    // O(n) time complexity
    public int getTopicCount(String topic) {
        String url = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + topic;
        int count = 0;

        try {
            URL link = new URL(url);
            HttpURLConnection connection = (HttpURLConnection) link.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            int responseCode = connection.getResponseCode();

            if (responseCode != 200) {
                throw new RuntimeException("HttpResponseCode: " + responseCode);
            } else {
                try (BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                    JsonElement jsonElement = JsonParser.parseReader(bufferedReader);

                    // Get root object
                    JsonObject rootObject = jsonElement.getAsJsonObject();

                    // Extract nested objects
                    JsonObject parseChildObject = rootObject.getAsJsonObject("parse"); // 'parse' is child of root
                    JsonObject textChildObject = parseChildObject.getAsJsonObject("text"); // 'text' is child of parse
                    String asterisk = textChildObject.get("*").toString().toLowerCase(); // Convert to lowercase because matcher is case-sensitive

                    Pattern pattern = Pattern.compile(topic);
                    Matcher matcher = pattern.matcher(asterisk);

                    // Search text for topic string
                    // Increment count when match occurs
                    while (matcher.find()) {
                        count++;
                    }
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        return count;
    }

    // this is a test comment
}