import java.util.Arrays;

class ThreeSumClosest {
    class Solution {
        public int threeSumClosest(int[] nums, int target) {
            int ans=0,result=Integer.MAX_VALUE,n=nums.length;
            Arrays.sort(nums);
            for(int i=0;i<n-2;i++){
                for(int j=i+1;j<n-1;j++){
                    for(int k=j+1;k<n;k++){
                        int temp=nums[k]+nums[j]+nums[i];
                        int diff=Math.abs(temp-target);
                        if(diff<result){
                            result=diff; 
                            ans=temp;
                        }
                    }
                }
            }
            return ans;
        }
    }
}