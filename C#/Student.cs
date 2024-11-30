class Student{
    public string Name;
    public string Major;
    public double Gpa;

    public Student(string aname,string amajor,double agpa){
        this.Name=aname;
        this.Major=amajor;
        this.Gpa=agpa;
    }
    public bool HasHonors(){
        if(Gpa>=3.5){return true;}
        return false;
    }
}