package JavaFiles;
// Client.java
public class ClientPOOL {
    public static void main(String[] args) {
        RideFacade rideFacade = new RideFacade();

        double carPOOLFare = rideFacade.getFare("carpool", 10);
        System.out.println("carPOOL Fare for 10 km: $" + carPOOLFare);

        double carXFare = rideFacade.getFare("carx", 10);
        System.out.println("carX Fare for 10 km: $" + carXFare);

        double carBlackFare = rideFacade.getFare("carblack", 10);
        System.out.println("carBlack Fare for 10 km: $" + carBlackFare);
    }
}
