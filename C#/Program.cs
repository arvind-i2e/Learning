namespace Hello
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // This is my first c# Programe.
            // int num = 6;
            // String inp = Console.ReadLine();
            // Console.WriteLine("The string u have given: " + inp);
            // Console.WriteLine("Hello World! I am Arvind!!");
            // Console.WriteLine("This is the number:" + num);
            /* Data types in C#:
             * Integer - int num; --> 4 bytes
             * Long -long num --> 8 bytes
             * Floating point number - float that; --> 4 bytes
             * Double -double num --> 8 bytes(upto 15 decimal digit precision)
             * Character -char a='A'; --> 2 bytes
             * Boolean -bool isGreat = true; --> 1 bit
             * String inp = "Arvind";--> 2 bytes * characters.
             */
            // Data Type Examples.
            //int a = 34;
            //float b = 34.4F;
            //double c = 34.4D;
            //bool isGreat = true;
            //char d = 'r';
            //string s = "This is a string";
            //Console.WriteLine(a.GetType());
            //Console.WriteLine(b);
            //Console.WriteLine(c);
            //Console.WriteLine(d);
            //Console.WriteLine(isGreat);
            //Console.WriteLine(s)//;

            //Type casting
            //1.Implicit casting:char=>int=>long=>float=>double.
            //int x = 3;
            //double y = x;
            //int z = 'y';
            //Console.WriteLine(x);
            //Console.WriteLine(y);
            //Console.WriteLine(z); It will return Ascii value of 'y'.
            ////2.Explicit casting
            //int a=(int)3.5;
            //double b = (double)3.5;
            //Console.WriteLine(a);
            //Console.WriteLine(b);
            //BuiltIn Methods for typecasting:Convert.ToInt32,Convert.ToDouble,Convert.ToString
            //User input=>
            //Console.WriteLine("Enter your Name:");
            //string name=Console.ReadLine();
            //Console.WriteLine("Hey hello:"+name);
            //Console.WriteLine("How many fingers u have?");
            //string num = Console.ReadLine();
            //Console.WriteLine("u have:"+(Convert.ToInt32(num)+5));
            //Operators in C#:
            //int a = 4;
            //int b = 2;
            //Console.WriteLine(a + b);
            //Console.WriteLine(a * b);
            //Console.WriteLine(a - b);
            //Console.WriteLine(a / b);
            //Console.WriteLine(a % b);
            //Console.WriteLine(a+=4);
            //Console.WriteLine(b+=2);
            //Console.WriteLine(true && false);
            //Console.WriteLine(true || false);
            //Console.WriteLine(!false);
            //Console.WriteLine(!true);
            //Console.WriteLine(232 > 444);
            //Console.WriteLine(232 < 444);
            //Console.WriteLine(232 >= 444);
            //Console.WriteLine(232 <= 444);
            //Console.WriteLine(232 == 232);
            //Math class in c#:
            //int a = Math.Max(555, 999);
            //int x = Math.Min(555, 999);
            //double b = Math.Sqrt(39.9);
            //int z = Math.Abs(-999);
            //Console.WriteLine(x);
            //Console.WriteLine(a);
            //Console.WriteLine(b);
            //Console.WriteLine(z);
            // String methods:
            //string hello = "Hello universe I'm Arvind";
            //Console.WriteLine(hello.Length);
            //Console.WriteLine(hello.ToLower());
            //Console.WriteLine(hello.ToUpper());
            //Console.WriteLine(string.Concat(hello, "You are good."));
            //string name=Console.ReadLine();
            //string bucks=Console.ReadLine();
            //Console.WriteLine($"your name is {name} and you will get this much bucks {bucks}.");//string interpolation.
            //Console.WriteLine(hello.IndexOf("l"));
            //Console.WriteLine(hello.Substring(6));
            //Console.WriteLine("hello\"Universe");(Escape Sequence Character).
            //Conditional statement(if-else):
            //int age = 56;
            //if (age > 18)
            //{
            //    Console.WriteLine("You can drive");
            //}
            //else
            //{
            //    Console.WriteLine("You can't drive");
            //}
            //Console.WriteLine("Enter your age:");
            //string agestr=Console.ReadLine();
            //int age=Convert.ToInt32(agestr);
            //if (age < 2)
            //{
            //    Console.WriteLine("you are just born");
            //}
            //else if (age < 10)
            //{
            //    Console.WriteLine("complete your high school");
            //}
            //else if (age < 18)
            //{
            //    Console.WriteLine("you are below 18");
            //}
            //else if (age < 75)
            //{
            //    Console.WriteLine("you can drive");
            //}
            //else
            //{
            //    Console.WriteLine("you can not drive");
            //}
            //Switch-case
            //switch (age)
            //{
            //    case 18:
            //        Console.WriteLine("Wait for an year");
            //        break;

            //    case 20:
            //        Console.WriteLine("You are 20");
            //        break;

            //    default:
            //        Console.WriteLine("Enjoy");
            //        break;


            //}
            //Loops in C#: 1.While-loop 2.Do-while 3.For-loop
            //int i = 0;
            //while (i < 5)
            //{
            //    Console.WriteLine(i+1);
            //    i++;
            //}
            //do
            //{
            //    Console.WriteLine(i + 2);
            //    i++;
            //} while (i < 5);
            //for (int i = 0; i < 5; i++) {
            //    Console.WriteLine(i+1);
            //}
            //break and continue(break leave entire loop where continue leave particular iteration).
            //for (int i = 0; i < 6; i++)
            //{
            //    if (i == 0)
            //    {
            //        continue;
            //    }
            //    Console.WriteLine(i+1);
            //}
            //Method call up.
            //Greet("Arvind");
            //Console.WriteLine(avg(5, 5, 5));
            //Oops in C#:
            // Player tommy = new Player();
            // Console.WriteLine(tommy.health);
            // tommy.setHealth(50);
            // Console.Write(tommy.health);
            Voting game=new();
            game.election();
            // Console.ReadLine();
        }
        // Methods or Functions(fun):
        //static float avg(int x, int y,int z)
        //{
        //    float sum=x+y+z;
        //    return sum / 3;
        //}
        //method overloading
        //static float avg(int x, int y)
        //{
        //    float sum = x + y;
        //    return sum / 2;
        //}

        //static void Greet(String name)
        //{
        //    Console.WriteLine($"Good morning {name}");
        //}

    }
}
