using System.ComponentModel;

//Inheritance:Super Class Chef.
class Chef{
    public void MakeChicken(){
        Console.WriteLine("The Chef makes chicken");
    }
    public void MakeSalad(){
        Console.WriteLine("The Chef makes salad");
    }
    public virtual void MakeSpecialDish(){
        Console.WriteLine("The Chef makes bbq ribs");
    }

}
//Sub-class of superclass Chef.
class ItalianChef:Chef{
    public void MakePasta(){
        Console.WriteLine("The Chef makes pasta");
    }
    public override void MakeSpecialDish(){
        Console.WriteLine("The Chef makes Pizza Margherita");//This subclass method Override the SuperClass Method
    }
}