public class Person{
    public int Id;
    public string FirstName="";
    public string LastName="";
    // public Person()
    // {
    //    //Doubt About parameterless constructor{need to use this for object initializer}.
    // }
    public Person(int id)
    {
        this.Id=id;
    }
    public Person(int id,string firstName)
    :this(id)
    {
        this.FirstName=firstName;
    }
    public Person(int id,string firstName,string lastName)
    :this(id,firstName)
    {
      this.LastName=lastName;  
    }
}