package lab.eval.practice;

import java.util.HashMap;

public class Frequency {
    public static void main(String[] args) {
        HashMap<String, Integer> FreqMap = new HashMap<String, Integer>();
        for (String word : MikuLyrics.split(" ")) {
            if (FreqMap.get(word) != null) {
                FreqMap.put(word, FreqMap.get(word) + 1);
            } else {
                FreqMap.put(word, 1);

            }
        }
        java.util.List<java.util.Map.Entry<String, Integer>> entries = new java.util.ArrayList<>(FreqMap.entrySet());
        entries.sort((a, b) -> {
            int cmp = b.getValue().compareTo(a.getValue());
            return (cmp != 0) ? cmp : a.getKey().compareTo(b.getKey());
        });
        for (java.util.Map.Entry<String, Integer> e : entries) {
            System.out.println(e.getKey() + " : " + e.getValue() + " " + "=".repeat(e.getValue()));
        }
    }

    static String MikuLyrics = """
                                    [Intro]
                        Ooh-ee-ooh
                        Ooh-ee-ooh
                        Ooh-ee-ooh
                        Ooh-ee-ooh

                        [Verse 1]
                        Miku, Miku, you can call me Miku
                        Blue hair, blue tie, hiding in your Wi-Fi
                        Open secrets, anyone can find me
                        Hear your music running through my mind

                        [Chorus]
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)

                        [Post-Chorus]
                        I'm on top of the world because of you
                        All I wanted to do is follow you
                        I'll keep singing along to all of you
                        I'll keep singing along

                        [Chorus]
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        [Verse 2]
                        Miku, Miku, what's it like to be you?
                        20/20, looking in the rear view
                        Play me, break me, make me feel like Superman
                        You can do anything you want

                        [Instrumental Break]

                        [Post-Chorus]
                        I'm on top of the world because of you
                        All I wanted to do is follow you
                        I'll keep singing along to all of you
                        I'll keep singing along
                        I'm on top of the world because of you
                        I do nothing that they could never do
                        I'll keep playing along with all of you
                        I'll keep playing along

                        [Chorus]
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)
                        I'm thinking Miku, Miku (Ooh-ee-ooh)

                        [Instrumental Break]
                        [Bridge]
                        Where were we walking together?
                        I will see you in the end
                        I'll take you where you've never been
                        And bring you back again
                        Listen to me with your eyes
                        I'm watching you from in the sky
                        If you forget I'll fade away
                        I'm asking you to let me stay
                        So bathe me in your magic light
                        And keep it on in darkest night
                        I need you here to keep me strong
                        To live my life and sing along
                        I'm waiting with you wide awake
                        Like your expensive poison snake
                        You found me here inside a dream
                        Walk through the fire straight to me

                        [Outro]
                        Tsap eht morf dnuos tsal erutuf eht morf dnuos tsriF
            """;
}
