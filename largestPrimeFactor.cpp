long long int largestPrimeFactor(int N){
        // code here
        long long res=0;
        
        
        for(int i=2;i*i<=N;i++)
        {
            while(N%i==0)
            {
                res=i;
                N=N/i;
                
            }
        }
        if(N>1)
        res=N;
        
        return res;
        
        
        
    }