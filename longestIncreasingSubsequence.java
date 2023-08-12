class Solution 
{
    static int binarySearch(int l, int h, int[] ans, int num)
    {
        while(l <= h)
        {
            int mid = (h-l)/2+l;
            if(ans[mid] == num)
            return mid;
            else if(ans[mid] > num)
            h = mid-1;
            else
            l = mid+1;
        }
        return l;
    }
   static int longestSubsequence(int n, int a[])
    {
        int ans[] = new int[n];
        Arrays.fill(ans, -1);
        int high = 0;
        ans[0] = a[0];
        for(int i=1; i<n; i++)
        {
            int index = binarySearch(0, high, ans, a[i]);
            if(index > high)
            high = index;
            ans[index] = a[i];
        }
        return high+1;
    }
} 