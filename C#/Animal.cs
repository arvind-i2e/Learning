//Encapsulation,multiple inheritance and abstraction.
//interface and abstract classes.
public interface IAnimal{
    public string? Name {get;set;}
    void Makesound();
}
// public interface IAnimal2{
//     public string? Name {get;set;}
//     void Makesound2();
// // }
// class I : IAnimal, IAnimal2    // here we r implementing inheritance(multiple)
// {
//     public string? Name { get;set;}

//     public void Makesound()
//     {
//     }

//     public void Makesound2()
//     {
//     }
// }
public abstract class Animal:IAnimal{               //since we are using abstract class we r implementing abstraction process.Similarly for the interface also.... 
public string? Name{get;set;}
public abstract void Makesound();
}
public class Dog : Animal                          // here we r implementing inheritance(single one)
{
    public override void Makesound()
    {
        Console.WriteLine("Woof!");
    }
}
public class Cat : Animal
{
    public override void Makesound()
    {
        Console.WriteLine("Meow!");
    }
}