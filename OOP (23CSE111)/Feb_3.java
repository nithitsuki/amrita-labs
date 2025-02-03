public class Feb_3
{
    public static void main(String[] args)
    {
        //These are the primitive types
        
        /*Byte is 1 byte long */
        System.out.println("min value of byte = " + ((byte)0x80)); //10000000
        System.out.println("max value of byte = " + ((byte)0x7F) + "\n"); //01111111
        /*Short is 2 bytes big */
        System.out.println("min value of short = " + ((short)0x8000)); //1000000000000000
        System.out.println("max value of short = " + ((short)0x7FFF) + "\n"); //0111111111111111
        /*Int is 4 bytes long */
        System.out.println("min value of int = " + ((int)0x80000000));
        System.out.println("max value of int = " + ((int)0x7FFFFFFF) + "\n");
        /*Long is 8 Bytes */
        System.out.println("min value of long = " + ((long)0x8000000000000000L));
        System.out.println("max value of long = " + ((long)0x7FFFFFFFFFFFFFFFL)  + "\n");
        /* Double is 8 bytes */
        System.out.println("min value of double = " + (double)0x8000000000000000L);
        System.out.println("max value of double = " + (double)0x7FFFFFFFFFFFFFFFL + "\n");

        for(int i = 49; i < 128; i++)
        {
            //print the ASCII table lol
            System.out.print((char)i);
        }
    }
}