import java.util.Scanner;
public class HomeworkOOP0809 {
    class HCN {
        private int dai;
        private int rong;
        public HCN(int dai,int rong){
            if(dai <= 0 || rong <= 0){
                throw new  IllegalArgumentException("Lỗi giá trị đầu vào !");
            }
            this.dai=dai;
            this.rong=rong;
        }
        public int getDai(){
            return  dai;
        }
        public  int getRong(){
            return rong;
        }
        public int getTinhChuVi(){
            return  2*(dai+rong);
        }
        public void display(){
            System.out.println("Chiều dài bằng"+dai);
            System.out.println("Chiều rộng bằng"+rong);
            System.out.println("Chu vi bằng"+getTinhChuVi());}
        }
}
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhập chiều dài: ");
        int dai = sc.nextInt();

        System.out.print("Nhập chiều rộng: ");
        int rong = sc.nextInt();

        HCN hcn = new HCN(dai, rong);
        hcn.display();
    }
}