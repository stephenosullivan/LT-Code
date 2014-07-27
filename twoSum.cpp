class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        typedef std::unordered_map<int,int> stringmap;
        int difference;
        stringmap mymap;
        int cnt = 0;
        //Fill the mapping
        for(vector<int>::iterator iter = numbers.begin();iter!=numbers.end();++iter){
               mymap[*iter]= ++cnt;
        }
        //Not zero-based indexing
        cnt=1;
        //Iterate through the input vector
        for(vector<int>::iterator iter = numbers.begin();iter!=numbers.end();++iter,++cnt){
            //Find the remainder
            difference = target - *iter;
            //Check if it exists in the keyset and ensure we are not using two instances of the same key
      	    if(mymap.count(difference)!=0 && mymap[difference]!=cnt){	    
	      	      return vector<int>{cnt,mymap[difference]};
            }
        }
    }
 
};
 
