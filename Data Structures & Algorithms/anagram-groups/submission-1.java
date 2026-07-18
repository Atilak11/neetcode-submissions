class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> find = new HashMap<>();
        String key = "";

        for (String s : strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            key = new String(chars);

            if (!find.containsKey(key)){
                find.put(key, new ArrayList<>());
            }
            find.get(key).add(s);
        }

        ArrayList<List<String>> answer = new ArrayList<>(find.values());
        return answer;
           
    }
}
