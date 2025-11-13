package lab.eval.practice;

import java.util.HashMap;

class First {
    public static void main(String[] args) {
        HashMap<String, Integer> map1 = new HashMap<>();
        map1.put("Nithian", 45);
        map1.put("Abhijit", 90);
        map1.put("Aditi", 92);
        map1.put("Mitran", 123);
        System.out.println("Map1 is: \n" + map1);

        int MaxMarks = Integer.MIN_VALUE;
        String MaxKey = "";
        for (String key : map1.keySet()) {
            if (map1.get(key) > MaxMarks) {
                MaxMarks = map1.get(key);
                MaxKey = key;
            }
        }
        System.out.println("Max marks is " + MaxMarks + " by " + MaxKey);

        HashMap<String, Integer> map2 = new HashMap<>();
        map2.put("Nithian", 35);
        map2.put("Madhumitha", 87);
        map2.put("Suwansh", 89);
        map2.put("Lohit", 107);
        System.out.println("\nMap 2 is: \n" + map2);

        AddMaps(map1,map2); //adds map2 to map1
        System.out.println("\nCombined Map is: " + map1);
    }

    static void AddMaps(HashMap<String, Integer> map1, HashMap<String, Integer> map2) {
        for (String Key2 : map2.keySet()) {
            if(map1.get(Key2) != null){
                map1.put(Key2, map1.get(Key2)+map2.get(Key2));
                continue;
            }
            map1.put(Key2,map2.get(Key2));
        }
    }
}