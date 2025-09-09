import java.util.Scanner;
public class Ex0909 {
    public class sinhVien{
        private String name;
        private  int age;
        private String id_Stu;

        private static int Tong = 0;
        public sinhVien( String name,int age, String id_Stu) {
            this.name = name;
            this.age = age;
            this.id_Stu = id_Stu;
        }
        public  void  gan(String name, int age, String id_Stu){
            this.name = name;
            this.age = age;
            this.id_Stu =id_Stu;
        }
        public void input(){
            Scanner sc = new Scanner(System.in);
            System.out.println("Nhan ma sinh vien:");
                    id_Stu = sc.nextLine();
            System.out.println("Nhan Ho Ten:");
        }
        }


    }


