/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point> &points) {
      //variables and objects needed
        vector<Point>::iterator vec_iter1,vec_iter2;
        string m_tmp;
        map<string,int> mapCnter;
        map<string,int>::iterator it;
        
        //set counter to zero
        int cnt=0;

	//set same point counter to zero
        int cnt_samept=0;

	//initialize the map so that it is non-zero for the single point case   
	mapCnter["same"]=0;
      
      //Calculate the slopes between points and increase the map of each slope by one
      //double loop using vector iterator to run over all points
      //Inner loop avoids repeated calculations so that we have N^2/2 calculations
        for(vec_iter1=points.begin(); vec_iter1<points.end();++vec_iter1){
            cnt_samept=0;
            for(vec_iter2=vec_iter1; vec_iter2<points.end();++vec_iter2){
                
                //exception case: identical points
                //count the base point so that it contributes to the counter
                if((vec_iter2->x == vec_iter1->x) && (vec_iter2->y == vec_iter1->y))
                   cnt_samept++;
                
                //exception: slope infinity
                else if(vec_iter2->x == vec_iter1->x){
                    mapCnter["INF"]+=1;
                }
                
                //exception:slope zero
                else if(vec_iter2->y == vec_iter1->y){
	                 mapCnter["0"]+=1;
	            }
	            
	            //calculate slope
                else{
                    //(double) the int values below so the slope does not underflow, and remain an int
		            m_tmp = to_string(((double)vec_iter2->y - (double)vec_iter1->y)/((double)vec_iter2->x - (double)vec_iter1->x));
                    mapCnter[m_tmp]+=1;
                }
            }
            //find the maximum number of points in a line and save it if it is larger than the previous saved value
            for(it=mapCnter.begin();it!=mapCnter.end();++it){
                if((it->second + cnt_samept)>cnt)
                    cnt = it->second+cnt_samept;   
            }
            //clear the map counter and repeat the calculation for the next point
            mapCnter.clear();
        }
        return cnt;
    }
};
