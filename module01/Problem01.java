import java.io.*;

public class Problem01 {
        public static void main(String[] args) throws Exception{
                // this is equivalent to python: input()
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                String  line = br.readLine();
                
                // py: strs = line.split(" ")
                String[] strs = line.trim().split("\\s+");
                
                // py: num = int(strs[0])
                int num = Integer.parseInt(strs[0]);  
                
                /*
                x1 = []
                y1 = []
                for i in range(0,num):
                d1,d2 = input().split(" ")
                x1.append(int(d1))
                y1.append(int(d2))
                */
                int[] x = new int[num];
                int[] y = new int[num];
                
                for(int i = 0; i < num; ++i){
                        line = br.readLine();
                        strs = line.trim().split("\\s+");
                        x[i] = Integer.parseInt(strs[0]);
                        y[i] = Integer.parseInt(strs[1]);
                }
                
                System.out.println(java.util.Arrays.toString(x));
                System.out.println(java.util.Arrays.toString(y));
                
                /*
                max_dist = 0
                for i in range(0,num):
                for j in range(0,num):
                e = cartesian_distance(x1[i],y1[i],x1[j], y1[j])
                if e > max_dist:
                max_dist = e
                nu = i + 1
                du = j + 1
                print(nu,du)
                */
                double max_dist = 0;
                int nu = 0;
                int du = 0;
                for(int i = 0; i < num; ++i){
                        for(int j = 0; j < num; j++){
                                double e = cartesian_distance(x[i], y[i], x[j], y[j]);
                                if (e > max_dist) {
                                        max_dist = e;
                                        nu = i + 1;
                                        du = j + 1;	
                                }
                        }
                }
                System.out.println(nu +" " +du);
        }
        
        /*
        * def cartesian_distance(x1, y1, x2, y2):
        op_1 = (x1 - x2)**2 + (y1 - y2)**2
        ans = math.sqrt(op_1)
        return(ans)
        */
        public static double cartesian_distance(int x1, int y1, int x2, int y2) {
                double op_1 = Math.pow((x1 -x2),2) + Math.pow((y1 - y2),2);
                
                return Math.sqrt(op_1);
        }
}
