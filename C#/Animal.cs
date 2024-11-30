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
// class I : IAnimal, IAnimal2
// {
//     public string? Name { get;set;}

//     public void Makesound()
//     {
//     }

//     public void Makesound2()
//     {
//     }
// }
public abstract class Animal:IAnimal{
public string? Name{get;set;}
public abstract void Makesound();
}
public class Dog : Animal
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