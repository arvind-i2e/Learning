//// using System.Diagnostics;
//// using System.Runtime.InteropServices;

//// namespace Hello
//// {
////     internal class Program
////     {
////         // public class Person{
////         //     public string name="";
////         //     public void Introduce(string to){
////         //         Console.WriteLine("Hi {0}, I am {1}",to,name);
////         //     }
////         //     //Creating a personal Object
////         //     public static Person Parse(string str){
////         //         var person=new Person();
////         //         person.name=str;
////         //         return person;
////         //     }
////         // }
////         static void Main(string[] args)
////         {
////             // var person=new Person();
////             // var person=Person.Parse("Arvind");//personal object for accessing static member using class.
////             // person.Introduce("Elliot");
////             // This is my first c# Programe.
////             // int num = 6;
////             // String inp = Console.ReadLine();
////             // Console.WriteLine("The string u have given: " + inp);
////             // Console.WriteLine("Hello World! I am Arvind!!");
////             // Console.WriteLine("This is the number:" + num);
////             /* Data types in C#:
////              * Integer - int num; --> 4 bytes
////              * Long -long num --> 8 bytes
////              * Floating point number - float that; --> 4 bytes
////              * Double -double num --> 8 bytes(upto 15 decimal digit precision)
////              * Character -char a='A'; --> 2 bytes
////              * Boolean -bool isGreat = true; --> 1 bit
////              * String inp = "Arvind";--> 2 bytes * characters.
////              */
////             // Data Type Examples.
////             //int a = 34;
////             //float b = 34.4F;
////             //double c = 34.4D;
////             //bool isGreat = true;
////             //char d = 'r';
////             //string s = "This is a string";
////             //Console.WriteLine(a.GetType());
////             //Console.WriteLine(b);
////             //Console.WriteLine(c);
////             //Console.WriteLine(d);
////             //Console.WriteLine(isGreat);
////             //Console.WriteLine(s)//;

////             //Type casting
////             //1.Implicit casting:char=>int=>long=>float=>double.
////             //int x = 3;
////             //double y = x;
////             //int z = 'y';
////             //Console.WriteLine(x);
////             //Console.WriteLine(y);
////             //Console.WriteLine(z); It will return Ascii value of 'y'.
////             ////2.Explicit casting
////             //int a=(int)3.5;
////             //double b = (double)3.5;
////             //Console.WriteLine(a);
////             //Console.WriteLine(b);
////             //BuiltIn Methods for typecasting:Convert.ToInt32,Convert.ToDouble,Convert.ToString
////             //User input=>
////             //Console.WriteLine("Enter your Name:");
////             //string name=Console.ReadLine();
////             //Console.WriteLine("Hey hello:"+name);
////             //Console.WriteLine("How many fingers u have?");
////             //string num = Console.ReadLine();
////             //Console.WriteLine("u have:"+(Convert.ToInt32(num)+5));
////             //Operators in C#:
//             //int a = 4;
//             //int b = 2;
//             //Console.WriteLine(a + b);
//             //Console.WriteLine(a * b);
//             //Console.WriteLine(a - b);
//             //Console.WriteLine(a / b);
//             //Console.WriteLine(a % b);
//             //Console.WriteLine(a+=4);
//             //Console.WriteLine(b+=2);
//             //Console.WriteLine(true && false);
//             //Console.WriteLine(true || false);
//             //Console.WriteLine(!false);
//             //Console.WriteLine(!true);
//             //Console.WriteLine(232 > 444);
//             //Console.WriteLine(232 < 444);
//             //Console.WriteLine(232 >= 444);
//             //Console.WriteLine(232 <= 444);
//             //Console.WriteLine(232 == 232);
////             //Math class in c#:
////             //int a = Math.Max(555, 999);
////             //int x = Math.Min(555, 999);
////             //double b = Math.Sqrt(39.9);
////             //int z = Math.Abs(-999);
////             //Console.WriteLine(x);
////             //Console.WriteLine(a);
////             //Console.WriteLine(b);
////             //Console.WriteLine(z);
////             // String methods:
////             //string hello = "Hello universe I'm Arvind";
////             //Console.WriteLine(hello.Length);
////             //Console.WriteLine(hello.ToLower());
////             //Console.WriteLine(hello.ToUpper());
////             //Console.WriteLine(string.Concat(hello, "You are good."));
////             //string name=Console.ReadLine();
////             //string bucks=Console.ReadLine();
////             //Console.WriteLine($"your name is {name} and you will get this much bucks {bucks}.");//string interpolation.
////             //Console.WriteLine(hello.IndexOf("l"));
////             //Console.WriteLine(hello.Substring(6));
////             //Console.WriteLine("hello\"Universe");(Escape Sequence Character).
////             //Conditional statement(if-else):
////             //int age = 56;
////             //if (age > 18)
////             //{
////             //    Console.WriteLine("You can drive");
////             //}
////             //else
////             //{
////             //    Console.WriteLine("You can't drive");
////             //}
//             //Console.WriteLine("Enter your age:");
//             //string agestr=Console.ReadLine();
//             //int age=Convert.ToInt32(agestr);
//             //if (age < 2)
//             //{
//             //    Console.WriteLine("you are just born");
//             //}
//             //else if (age < 10)
//             //{
//             //    Console.WriteLine("complete your high school");
//             //}
//             //else if (age < 18)
//             //{
//             //    Console.WriteLine("you are below 18");
//             //}
//             //else if (age < 75)
//             //{
//             //    Console.WriteLine("you can drive");
//             //}
//             //else
//             //{
//             //    Console.WriteLine("you can not drive");
//             //}
////             //Switch-case
////             //switch (age)
////             //{
////             //    case 18:
////             //        Console.WriteLine("Wait for an year");
////             //        break;

////             //    case 20:
////             //        Console.WriteLine("You are 20");
////             //        break;

////             //    default:
////             //        Console.WriteLine("Enjoy");
////             //        break;
////             //}
////             //Loops in C#: 1.While-loop 2.Do-while 3.For-loop
////             //int i = 0;
////             //while (i < 5)
////             //{
////             //    Console.WriteLine(i+1);
////             //    i++;
////             //}
////             //do
////             //{
////             //    Console.WriteLine(i + 2);
////             //    i++;
////             //} while (i < 5);
////             //for (int i = 0; i < 5; i++) {
////             //    Console.WriteLine(i+1);
////             //}
////             //break and continue(break leave entire loop where continue leave particular iteration).
////             //for (int i = 0; i < 6; i++)
////             //{
////             //    if (i == 0)
////             //    {
////             //        continue;
////             //    }
////             //    Console.WriteLine(i+1);
////             //}
////             //Method call up.
////             //Greet("Arvind");
////             //Console.WriteLine(avg(5, 5, 5));
////             //Oops in C#:
////             // Player tommy = new Player();
////             // Console.WriteLine(tommy.health);
////             // tommy.setHealth(50);
////             // Console.Write(tommy.health);
////             // Voting game=new();
////             // game.election();
////             // emailValidation user=new();
////             // user.Validation("Arvind@gmail");
////             // Url test=new();
////             // test.UrlValidation("www.w3schools.com/cs/cs_arrays.php");
////             // pattern();
////             // Console.ReadLine();
////             // IShape circle = new Circle(5);
////             // IShape rectangle=new Rectangle{Length = 4,Breadth=5};
////             // calculateArea(circle); //Single responsibilty principle
////             // new Printer().Print(circle); //Single responsibilty principle
////             // var customer=new Customer(1,"Elliot");
////             // Console.WriteLine(customer.Id);
////             // Console.WriteLine(customer.Name);
////             var person=new Person(101){FirstName="Elliot",LastName="Alderson"};
////             Console.WriteLine("ID: {0},Firstname: {1},LastName:{2}",person.Id,person.FirstName,person.LastName);
////         }
////         // private static void calculateArea(IShape circle){
////         //     Console.WriteLine(circle.getArea());
////         // }
////         // Methods or Functions(fun):
////         //static float avg(int x, int y,int z)
////         //{
////         //    float sum=x+y+z;
////         //    return sum / 3;
////         //}
////         //method overloading
////         //static float avg(int x, int y)
////         //{
////         //    float sum = x + y;
////         //    return sum / 2;
////         //}

////         //static void Greet(String name)
////         //{
////         //    Console.WriteLine($"Good morning {name}");
////         //}
////         // static void pattern(){
////         //     for(int i=0;i<6;i++){
////         //         for(int j=0;j<=i;j++){
////         //             Console.Write("*");
////         //         }
////         //         Console.WriteLine();
////         //     }
////         // }
////     }
//// }
//// class Program{
////     public static void Main(string[] args)
////     {
////         Level myLevel=Level.feb;
////         switch(myLevel)
////         {
////             case Level.jan:
////             Console.WriteLine("Hello January");
////             break;
////             case Level.feb:
////             Console.WriteLine("Hello feb");
////             break;
////         }
////     }
//// }
//class Program{
//    public static void Main(string[] args){
//        // var myAnimal=new Animal{Name="Lion"};
//        // myAnimal.Name="Lion";
//        // Console.WriteLine(myAnimal.Name);
//        // var student1=new Student("Elliot","Computer-sci",4.5);
//        // var student2=new Student("Pam","Art",2.9);
//        // Console.WriteLine(student1.HasHonors());
//        // Console.WriteLine(student2.HasHonors());
//        // var avengers=new Movie("The Avengers","Joss Whedon","PG-13");
//        // var shrek=new Movie("Shrek","Adam Adamson","PG");
//        // avengers.Rating="Dog";
//        // Console.WriteLine(avengers.Rating);
//        // Console.WriteLine(shrek.Rating);
//        //    var holiday=new Song("Holiday","Green Day",200);
//        //    Console.WriteLine(Song.songCount);
//        //    var kashmir=new Song("Kashmir","Led Zepppelin",150);
//        //    Console.WriteLine(kashmir.getSongCount());
//        // UseFullTool.SayHi("Arvind");
//        // var chef=new Chef();
//        // chef.MakeChicken();
//        // var italianchef=new ItalianChef();
//        // italianchef.MakeSalad();
//        // italianchef.MakePasta();
//        // chef.MakeSpecialDish();
//        // italianchef.MakeSpecialDish();
//        // Animal dog=new Dog();
//        // dog.Makesound();
//        // Animal cat=new Cat();
//        // cat.Makesound();
//        //# Exception Handling.
//        try{
//            Console.WriteLine("Enter a first number:");
//        int num1=Convert.ToInt32(Console.ReadLine());
//        Console.WriteLine("Enter a second number:");
//        int num2=Convert.ToInt32(Console.ReadLine());
//        Console.WriteLine(num1/num2);
//        }
//        // catch(Exception e){
//        //     Console.WriteLine(e.Message);
//        // }
//        //Multiple catch for specific exception handling design.
//        catch(DivideByZeroException e){
//            Console.WriteLine(e.Message);
//        }
//        catch(FormatException e){
//            Console.WriteLine(e.Message);
//        }

//    }
//}