class Solution {
    public boolean isPerfectSquare(int num) {
        boolean isSquare = false; 
        for (int i = 1; i <= num; i++){
            if (num % i == 0 && i * i == num){
                isSquare = true;
            }
        }
        return isSquare;
    }
}