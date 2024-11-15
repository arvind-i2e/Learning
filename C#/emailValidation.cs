class emailValidation{
    public void Validation(string email){
      char first=email[0];
      string atSymbol="@";
      string dotCom=".com";

      if(char.IsNumber(first)||char.IsSymbol(first)){
        Console.WriteLine("\n Sorry mail can't start with number or symbols.");
        return;
      }
      if(!email.Contains(atSymbol)){
        Console.WriteLine("\n You have to include '@' symbol...");
        return;
      }
      if(email.Substring(email.Length-4)!=dotCom){
        Console.WriteLine("\n Gotta have a '.com' at the end..." );
        // Console.WriteLine($"\n{email.Substring(0,4)}");
        return;
      }
      Console.WriteLine("Valid-email");
    }
}