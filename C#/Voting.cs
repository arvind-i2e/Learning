class Voting{
    public void election(){
        Console.WriteLine("How old are you?");
        int input=Convert.ToInt32(Console.ReadLine());
        int presidents=CalculatePresidents(input);
        Console.WriteLine($"You've voted for {presidents} presidents");
        Console.ReadKey();
    }
    public static int CalculatePresidents(int age){
        int eligibleYears=age-18;
        int presidents=0;

        if(eligibleYears<=0){
            Console.WriteLine("Looks like you are not old enough to vote yet");
            return 0;
        }
        for(int i=1;i<=eligibleYears;i++){
            if(i%4==0){
                presidents++;
            }
        }
        return presidents;

    }
}