using System.Net.NetworkInformation;
using System.Runtime.InteropServices;
public interface IShape{
    double getArea();
}
public class Circle:IShape
{
   public Circle(double radius){
       Radius=radius;
   }
   public double Radius{get;set;}
   public double getArea(){
    return Math.PI*Radius*Radius;
   }
}
public class Rectangle:IShape
{
    public double Length{get;set;}
    public double Breadth{get;set;}
    public double getArea(){
        return Length*Breadth;
    }
}