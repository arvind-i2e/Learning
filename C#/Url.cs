class Url{
    public void UrlValidation(string url){
      string noWWW=url.Remove(0,4);
      string noDashes=noWWW.Replace("-"," ");
      string[] components=noDashes.Split('/');
      for(int i=0;i<components.Length;i++){
        Console.WriteLine($"-->{components[i]}");
      }
       
    }
}