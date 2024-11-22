package JavaFiles;

public class ClientGo {
    public static void main(String[] args) {
        // Create prototypes
        RideServiceGo carGoPrototype = new CarGoService();
        carGoPrototype.setServiceDetails("Hatchback rides for affordable travel.");

        RideServiceGo carEATSPrototype = new CarEATSService();
        carEATSPrototype.setServiceDetails("Food delivery from local restaurants.");

        // Setup City Service Manager
        CityServiceManager mumbaiServiceManager = new CityServiceManager();
        mumbaiServiceManager.addService("carGo", carGoPrototype);
        mumbaiServiceManager.addService("carEATS", carEATSPrototype);

        // Clone services for Mumbai with specific details
        RideServiceGo mumbaiCarGo = mumbaiServiceManager.getService("carGo");
        mumbaiCarGo.setServiceDetails("Exclusive Mumbai hatchback service for short trips.");

        RideServiceGo mumbaiCarEATS = mumbaiServiceManager.getService("carEATS");
        mumbaiCarEATS.setServiceDetails("Mumbai-specific food delivery with top-rated restaurants.");

        // Display customized services for Mumbai
        System.out.println(mumbaiCarGo.getServiceDetails());
        System.out.println(mumbaiCarEATS.getServiceDetails());

        // Set up another city, New Delhi, and reuse the prototypes
        CityServiceManager delhiServiceManager = new CityServiceManager();
        delhiServiceManager.addService("carGo", carGoPrototype);
        delhiServiceManager.addService("carEATS", carEATSPrototype);

        // Clone and customize for New Delhi
        RideServiceGo delhiCarGo = delhiServiceManager.getService("carGo");
        delhiCarGo.setServiceDetails("New Delhi's premium hatchback service.");

        System.out.println(delhiCarGo.getServiceDetails());
    }
}